#!/usr/bin/env python3
"""Validate a multichannel external business-model evidence diagnostic.

Usage:
    python validate_diagnostic.py [--strict|--legacy] <diagnostic_directory>

The strict gate (default) checks structure, provenance, source independence,
freshness, cross-references, and whether the report's verdict is stronger than
its evidence. It still cannot verify source truth, demand, causality, PMF, or
commercial success.
"""
from __future__ import annotations

import argparse
import csv
import re
import sys
from collections import Counter, defaultdict
from datetime import date, datetime
from pathlib import Path
from urllib.parse import urlsplit, urlunsplit

REQUIRED_AREAS = {
    "P_problem", "S_segment", "V_value_exchange", "U_useful_outcome",
    "C_customer_access", "M_money_delivery", "R_resilience",
}
ALLOWED_STATUSES = {
    "untested", "weakly_supported", "supported", "contradictory",
    "disproven", "unknown", "external_evidence_missing",
}
ALLOWED_VERDICTS = {
    "market_research_required", "problem_and_alternatives_mapped",
    "switch_hypothesis_testable", "limited_market_entry_supported",
    "channel_or_economics_evidence_required", "scale_evidence_required",
    "insufficient_evidence",
}
ALLOWED_MARKET_REALITY = {
    "market_unmapped", "job_observed", "alternatives_mapped",
    "switch_reason_plausible", "external_demand_observed",
}
ALLOWED_OBJECT_PROOF = {
    "self_claim_only", "early_object_signal", "independent_object_proof",
    "private_evidence_required",
}
ALLOWED_CONFIDENCE = {"low", "medium", "high"}
ALLOWED_ALTERNATIVE_TYPES = {
    "DIY", "doing_nothing", "incumbent", "direct_competitor", "service_alternative",
}
ALLOWED_SOURCE_CLASSES = {
    "independent_behavior", "independent_account", "competitor_docs",
    "object_self_claim", "owner_operational_data",
}
ALLOWED_SIDES = {"object_side", "buyer_side", "alternative_side", "owner_private"}
ALLOWED_ACCESS_MODES = {"public_web", "user_file_export", "authorized_connector"}
ALLOWED_INDEPENDENCE = {"low", "medium", "high"}
ALLOWED_CHANNEL_STATUS = {"checked", "not_available", "optional"}
AREA_CODES = {
    "P_problem": {"J"},
    "S_segment": {"J", "A"},
    "V_value_exchange": {"T", "F"},
    "U_useful_outcome": {"G", "O"},
    "C_customer_access": {"A", "T"},
    "M_money_delivery": {"T", "O"},
    "R_resilience": {"O", "T"},
}
CLAIM_CODES = {"J", "A", "G", "T", "F", "O", "C", "M", "R"}
PLACEHOLDER_RE = re.compile(
    r"\[(?:число|дата|что|какой|почему|граница|источник|за什么|за что|"
    r"high\|medium\|low|YYYY-MM-DD)[^\]]*\]|TODO|TBD|lorem ipsum",
    re.IGNORECASE,
)
REQUIRED_MAP_HEADERS = {
    "id", "area", "comparative_hypothesis", "current_status",
    "external_evidence_summary", "external_evidence_id", "alternative_ids",
    "object_specific_evidence", "private_evidence_needed", "contradiction_or_risk",
    "minimum_evidence_needed", "blocks_verdict", "notes",
}
REQUIRED_ALTERNATIVE_HEADERS = {
    "alternative_id", "alternative_name", "alternative_type", "role_or_buyer",
    "situation_or_job", "why_relevant", "pricing_or_exchange_unit",
    "switching_friction", "source_url", "source_date", "source_class", "notes",
}
REQUIRED_CHANNEL_HEADERS = {
    "channel_id", "side", "channel_type", "access_mode", "locator_or_query",
    "purpose", "observed_signal", "claim_codes_supported", "does_not_prove",
    "status", "source_date", "notes",
}
REQUIRED_LEDGER_HEADERS = {
    "evidence_id", "channel_id", "side", "access_mode", "market_claim_code",
    "claim_supported", "observation_or_quote", "source_name", "source_url_or_locator",
    "source_date", "source_class", "independence_level", "alternative_explanation",
    "what_it_does_not_prove", "object_or_alternative",
}
REQUIRED_LEGACY_SECTIONS = (
    "## 1. Короткий вывод",
    "## 2. Объект исследования и текущая альтернатива",
    "## 3. Проверенные коммуникационные каналы",
    "## 4. Карта альтернатив и прямых конкурентов",
    "## 5. Внешние следы спроса и переключения",
    "## 6. Сравнительная карта claims бизнес-модели",
    "## 7. Блокирующие evidence gaps",
    "## 8. Требования для смены verdict",
    "## 9. Ограничения вывода",
)
REQUIRED_SECTIONS = REQUIRED_LEGACY_SECTIONS + ("## 10. Adversarial self-check",)


def headers_or_error(path: Path, expected: set[str]) -> tuple[list[dict[str, str]], list[str]]:
    with path.open(encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        missing = expected - set(reader.fieldnames or [])
        if missing:
            return [], [f"{path.name}: missing header(s): {', '.join(sorted(missing))}"]
        return list(reader), []


def parse_date(value: str) -> date | None:
    text = (value or "").strip()
    if not text:
        return None
    try:
        return datetime.strptime(text[:10], "%Y-%m-%d").date()
    except ValueError:
        return None


def normalise_locator(value: str) -> str:
    text = (value or "").strip().lower()
    if not text or text in {"not_available", "n/a", "na"}:
        return ""
    if text.startswith(("http://", "https://")):
        parts = urlsplit(text)
        path = parts.path.rstrip("/") or "/"
        return urlunsplit((parts.scheme, parts.netloc, path, "", ""))
    return re.sub(r"\s+", " ", text)


def unique_nonempty(values: list[str]) -> set[str]:
    return {normalise_locator(value) for value in values if normalise_locator(value)}


def is_independent(row: dict[str, str]) -> bool:
    return (row.get("source_class") or "").strip() != "object_self_claim"


def is_positive_independent(row: dict[str, str]) -> bool:
    source_class = (row.get("source_class") or "").strip()
    independence = (row.get("independence_level") or "").strip()
    return source_class in {"independent_behavior", "independent_account"} and independence in {"medium", "high"}


def placeholder_errors(value: str, location: str) -> list[str]:
    return [f"{location}: unresolved placeholder {match.group(0)!r}"] if PLACEHOLDER_RE.search(value or "") else []


def validate_object_card(path: Path) -> list[str]:
    text = path.read_text(encoding="utf-8")
    required = (
        "## Исследовательская единица", "| Объект |", "| Роль / buyer |",
        "| Ситуация |", "| Current alternative |", "| Claim объекта |",
    )
    errors = [f"object-card.md: missing required field/section {item!r}" for item in required if item not in text]
    errors.extend(placeholder_errors(text, "object-card.md"))
    return errors


def validate_channels(path: Path) -> tuple[list[str], set[str], list[dict[str, str]]]:
    rows, errors = headers_or_error(path, REQUIRED_CHANNEL_HEADERS)
    if errors:
        return errors, set(), []
    ids: set[str] = set()
    checked_sides: set[str] = set()
    today = date.today()
    for row_num, row in enumerate(rows, start=2):
        identifier = (row.get("channel_id") or "").strip()
        side = (row.get("side") or "").strip()
        mode = (row.get("access_mode") or "").strip()
        status = (row.get("status") or "").strip()
        source_date = parse_date(row.get("source_date") or "")
        for field in (
            "channel_id", "side", "channel_type", "access_mode", "locator_or_query",
            "purpose", "does_not_prove", "status", "source_date",
        ):
            if not (row.get(field) or "").strip():
                errors.append(f"channel-inventory.csv:{row_num}: missing {field}")
        if identifier in ids:
            errors.append(f"channel-inventory.csv:{row_num}: duplicate channel_id {identifier!r}")
        ids.add(identifier)
        if side not in ALLOWED_SIDES:
            errors.append(f"channel-inventory.csv:{row_num}: invalid side {side!r}")
        if mode not in ALLOWED_ACCESS_MODES:
            errors.append(f"channel-inventory.csv:{row_num}: invalid access_mode {mode!r}")
        if status not in ALLOWED_CHANNEL_STATUS:
            errors.append(f"channel-inventory.csv:{row_num}: invalid status {status!r}")
        if source_date is None:
            errors.append(f"channel-inventory.csv:{row_num}: invalid source_date")
        elif source_date > today:
            errors.append(f"channel-inventory.csv:{row_num}: source_date is in the future")
        if status == "checked":
            checked_sides.add(side)
        errors.extend(placeholder_errors(row.get("does_not_prove") or "", f"channel-inventory.csv:{row_num}"))
    for required_side in ("object_side", "buyer_side", "alternative_side"):
        if required_side not in checked_sides:
            errors.append(f"channel-inventory.csv: requires one checked {required_side} channel")
    return errors, ids, rows


def validate_alternatives(path: Path) -> list[str]:
    rows, errors = headers_or_error(path, REQUIRED_ALTERNATIVE_HEADERS)
    if errors:
        return errors
    if len(rows) < 3:
        errors.append("alternative-map.csv: requires at least 3 current alternatives/direct competitors")
    seen: set[str] = set()
    today = date.today()
    for row_num, row in enumerate(rows, start=2):
        identifier = (row.get("alternative_id") or "").strip()
        kind = (row.get("alternative_type") or "").strip()
        source_class = (row.get("source_class") or "").strip()
        source_date = parse_date(row.get("source_date") or "")
        for field in (
            "alternative_id", "alternative_name", "role_or_buyer", "situation_or_job",
            "why_relevant", "source_url", "source_date", "source_class",
        ):
            if not (row.get(field) or "").strip():
                errors.append(f"alternative-map.csv:{row_num}: missing {field}")
        if identifier in seen:
            errors.append(f"alternative-map.csv:{row_num}: duplicate alternative_id {identifier!r}")
        seen.add(identifier)
        if kind not in ALLOWED_ALTERNATIVE_TYPES:
            errors.append(f"alternative-map.csv:{row_num}: invalid alternative_type {kind!r}")
        if source_class not in ALLOWED_SOURCE_CLASSES:
            errors.append(f"alternative-map.csv:{row_num}: invalid source_class {source_class!r}")
        if source_date is None:
            errors.append(f"alternative-map.csv:{row_num}: invalid source_date")
        elif source_date > today:
            errors.append(f"alternative-map.csv:{row_num}: source_date is in the future")
        errors.extend(placeholder_errors(row.get("notes") or "", f"alternative-map.csv:{row_num}"))
    return errors


def validate_ledger(path: Path, channel_ids: set[str], strict: bool = True) -> tuple[list[str], list[dict[str, str]]]:
    rows, errors = headers_or_error(path, REQUIRED_LEDGER_HEADERS)
    if errors:
        return errors, []
    codes: set[str] = set()
    evidence_ids: set[str] = set()
    locators: list[str] = []
    independent_locators: list[str] = []
    today = date.today()
    for row_num, row in enumerate(rows, start=2):
        code = (row.get("market_claim_code") or "").strip()
        channel_id = (row.get("channel_id") or "").strip()
        side = (row.get("side") or "").strip()
        mode = (row.get("access_mode") or "").strip()
        source_class = (row.get("source_class") or "").strip()
        independence = (row.get("independence_level") or "").strip()
        source_date = parse_date(row.get("source_date") or "")
        locator = normalise_locator(row.get("source_url_or_locator") or "")
        for field in (
            "evidence_id", "channel_id", "side", "access_mode", "market_claim_code",
            "claim_supported", "observation_or_quote", "source_name",
            "source_url_or_locator", "source_date", "source_class", "independence_level",
            "alternative_explanation", "what_it_does_not_prove",
        ):
            if not (row.get(field) or "").strip():
                errors.append(f"external-evidence-ledger.csv:{row_num}: missing {field}")
        evidence_id = (row.get("evidence_id") or "").strip()
        if evidence_id in evidence_ids:
            errors.append(f"external-evidence-ledger.csv:{row_num}: duplicate evidence_id {evidence_id!r}")
        evidence_ids.add(evidence_id)
        if channel_id not in channel_ids:
            errors.append(f"external-evidence-ledger.csv:{row_num}: unknown channel_id {channel_id!r}")
        if side not in ALLOWED_SIDES:
            errors.append(f"external-evidence-ledger.csv:{row_num}: invalid side {side!r}")
        if mode not in ALLOWED_ACCESS_MODES:
            errors.append(f"external-evidence-ledger.csv:{row_num}: invalid access_mode {mode!r}")
        if code not in CLAIM_CODES:
            errors.append(f"external-evidence-ledger.csv:{row_num}: invalid market_claim_code {code!r}")
        else:
            codes.add(code)
        if source_class not in ALLOWED_SOURCE_CLASSES:
            errors.append(f"external-evidence-ledger.csv:{row_num}: invalid source_class {source_class!r}")
        if independence not in ALLOWED_INDEPENDENCE:
            errors.append(f"external-evidence-ledger.csv:{row_num}: invalid independence_level {independence!r}")
        if source_date is None:
            errors.append(f"external-evidence-ledger.csv:{row_num}: invalid source_date")
        elif source_date > today:
            errors.append(f"external-evidence-ledger.csv:{row_num}: source_date is in the future")
        elif strict and code in {"T", "O", "M", "C"} and (today - source_date).days > 365:
            errors.append(
                f"external-evidence-ledger.csv:{row_num}: transactional/object evidence is older than 365 days"
            )
        if locator:
            locators.append(locator)
            if is_positive_independent(row):
                independent_locators.append(locator)
        errors.extend(placeholder_errors(row.get("alternative_explanation") or "", f"external-evidence-ledger.csv:{row_num}"))
        errors.extend(placeholder_errors(row.get("what_it_does_not_prove") or "", f"external-evidence-ledger.csv:{row_num}"))
    if len(rows) < 3:
        errors.append("external-evidence-ledger.csv: requires at least 3 sourced observations")
    unique_locators = unique_nonempty(locators)
    unique_independent = unique_nonempty(independent_locators)
    if len(unique_locators) < 2:
        errors.append("external-evidence-ledger.csv: requires at least 2 distinct source locators")
    if len(unique_independent) < 1:
        errors.append("external-evidence-ledger.csv: requires at least 1 independent non-self-claim source")
    if strict:
        if len(unique_locators) < 3:
            errors.append("strict: requires at least 3 distinct source locators")
        if len(unique_independent) < 2:
            errors.append("strict: requires at least 2 distinct independent source locators")
    return errors, rows


def validate_map(
    path: Path,
    ledger_rows: list[dict[str, str]],
    strict: bool = True,
) -> tuple[list[str], list[dict[str, str]]]:
    rows, errors = headers_or_error(path, REQUIRED_MAP_HEADERS)
    if errors:
        return errors, []
    seen: set[str] = set()
    covered: set[str] = set()
    evidence_by_id = {row.get("evidence_id", "").strip(): row for row in ledger_rows}
    for row_num, row in enumerate(rows, start=2):
        identifier = (row.get("id") or "").strip()
        area = (row.get("area") or "").strip()
        status = (row.get("current_status") or "").strip()
        evidence_ids = {item.strip() for item in (row.get("external_evidence_id") or "").split(";") if item.strip()}
        for field in (
            "id", "area", "comparative_hypothesis", "current_status", "alternative_ids",
            "private_evidence_needed", "minimum_evidence_needed", "blocks_verdict",
            "external_evidence_summary", "contradiction_or_risk",
        ):
            if not (row.get(field) or "").strip():
                errors.append(f"business-model-hypothesis-map.csv:{row_num}: missing {field}")
        if identifier in seen:
            errors.append(f"business-model-hypothesis-map.csv:{row_num}: duplicate id {identifier!r}")
        seen.add(identifier)
        if area not in REQUIRED_AREAS:
            errors.append(f"business-model-hypothesis-map.csv:{row_num}: invalid area {area!r}")
        else:
            covered.add(area)
        if status not in ALLOWED_STATUSES:
            errors.append(f"business-model-hypothesis-map.csv:{row_num}: invalid current_status {status!r}")
        if (row.get("blocks_verdict") or "").strip() not in ALLOWED_VERDICTS:
            errors.append(f"business-model-hypothesis-map.csv:{row_num}: invalid blocks_verdict")
        missing_evidence = evidence_ids - set(evidence_by_id)
        if missing_evidence:
            errors.append(
                f"business-model-hypothesis-map.csv:{row_num}: unknown external_evidence_id(s): "
                f"{', '.join(sorted(missing_evidence))}"
            )
        referenced = [evidence_by_id[eid] for eid in evidence_ids if eid in evidence_by_id]
        independent_referenced = [item for item in referenced if is_positive_independent(item)]
        if status == "supported" and not referenced:
            errors.append(f"business-model-hypothesis-map.csv:{row_num}: supported claim has no evidence reference")
        if status == "supported" and strict and not independent_referenced:
            errors.append(f"business-model-hypothesis-map.csv:{row_num}: supported claim lacks independent evidence")
        if status == "weakly_supported" and not referenced:
            errors.append(f"business-model-hypothesis-map.csv:{row_num}: weakly_supported claim has no evidence reference")
        if status in {"contradictory", "disproven"} and strict and len(unique_nonempty([
            item.get("source_url_or_locator", "") for item in independent_referenced
        ])) < 2:
            errors.append(
                f"business-model-hypothesis-map.csv:{row_num}: {status} requires two independent observations"
            )
        errors.extend(placeholder_errors(row.get("contradiction_or_risk") or "", f"business-model-hypothesis-map.csv:{row_num}"))
        errors.extend(placeholder_errors(row.get("external_evidence_summary") or "", f"business-model-hypothesis-map.csv:{row_num}"))
    missing = REQUIRED_AREAS - covered
    if missing:
        errors.append(f"business-model-hypothesis-map.csv: missing required area(s): {', '.join(sorted(missing))}")
    return errors, rows


def extract_status(text: str, marker: str, allowed: set[str]) -> str:
    match = re.search(rf"{re.escape(marker)}\s*`([^`]+)`", text)
    return match.group(1).strip() if match else ""


def validate_diagnostic(
    path: Path,
    ledger_rows: list[dict[str, str]],
    map_rows: list[dict[str, str]],
    strict: bool = True,
) -> list[str]:
    text = path.read_text(encoding="utf-8")
    errors: list[str] = []
    sections = REQUIRED_SECTIONS if strict else REQUIRED_LEGACY_SECTIONS
    for section in sections:
        if section == "## 6. Сравнительная карта claims бизнес-модели":
            # v0.3 renamed the section title; accept both spellings.
            if "## 6. Сравнительная карта claims бизнес-модели" not in text and                "## 6. Сравнительная карта утверждений бизнес-модели" not in text:
                errors.append(f"business-model-diagnostic.md: missing section {section!r}")
        elif section not in text:
            errors.append(f"business-model-diagnostic.md: missing section {section!r}")
    market_reality = extract_status(text, "**Market reality:**", ALLOWED_MARKET_REALITY)
    object_proof = extract_status(text, "**Object proof:**", ALLOWED_OBJECT_PROOF)
    verdict = extract_status(text, "**Verdict готовности:**", ALLOWED_VERDICTS)
    confidence = extract_status(text, "**Уверенность вывода:**", ALLOWED_CONFIDENCE)
    if not market_reality:
        errors.append("business-model-diagnostic.md: missing or invalid Market reality status")
    if not object_proof:
        errors.append("business-model-diagnostic.md: missing or invalid Object proof status")
    if not verdict:
        errors.append("business-model-diagnostic.md: missing or invalid readiness verdict")
    if strict and not confidence:
        errors.append("business-model-diagnostic.md: missing or invalid confidence status")
    for marker in (
        "Рынок уже позволяет утверждать:", "Объект сам пока доказал:", "Нельзя пока утверждать:",
    ):
        if marker not in text:
            errors.append(f"business-model-diagnostic.md: missing evidence boundary {marker!r}")
    if strict:
        for marker in (
            "Самое сильное альтернативное объяснение:", "Что должно случиться, чтобы я изменил вывод:",
            "Не наблюдали / не доказано:",
        ):
            if marker not in text:
                errors.append(f"business-model-diagnostic.md: missing evidence boundary {marker!r}")
    errors.extend(placeholder_errors(text, "business-model-diagnostic.md"))

    if not strict or not (market_reality and object_proof and verdict and confidence and ledger_rows and map_rows):
        return errors

    locators = unique_nonempty([row.get("source_url_or_locator", "") for row in ledger_rows])
    independent = [row for row in ledger_rows if is_positive_independent(row)]
    independent_locators = unique_nonempty([row.get("source_url_or_locator", "") for row in independent])
    codes = {row.get("market_claim_code", "").strip() for row in ledger_rows}
    object_o_rows = [row for row in ledger_rows if row.get("market_claim_code", "").strip() == "O"]
    independent_object_rows = [row for row in object_o_rows if is_positive_independent(row)]

    required_confidence = "low"
    if len(locators) >= 3 and len(independent_locators) >= 2:
        required_confidence = "medium"
    if len(locators) >= 4 and len(independent_locators) >= 3:
        required_confidence = "high"
    if confidence == "high" and required_confidence != "high":
        errors.append("business-model-diagnostic.md: high confidence requires 4+ sources and 3+ independent sources")
    if confidence == "medium" and required_confidence == "high":
        errors.append("business-model-diagnostic.md: source base supports high confidence, but report declares medium")

    if object_proof == "independent_object_proof" and not independent_object_rows:
        errors.append("business-model-diagnostic.md: independent_object_proof requires independent O evidence")
    if object_proof == "self_claim_only" and independent_object_rows:
        errors.append("business-model-diagnostic.md: self_claim_only conflicts with independent O evidence")

    if market_reality == "external_demand_observed":
        buyer_transaction = [
            row for row in independent
            if row.get("side") == "buyer_side" and row.get("market_claim_code") in {"T", "J"}
        ]
        if len(unique_nonempty([row.get("source_url_or_locator", "") for row in buyer_transaction])) < 2:
            errors.append(
                "business-model-diagnostic.md: external_demand_observed requires 2+ independent buyer-side sources"
            )
    if market_reality == "switch_reason_plausible" and not ({"G", "F"} & codes):
        errors.append("business-model-diagnostic.md: switch_reason_plausible requires G or F evidence")
    if market_reality in {"job_observed", "alternatives_mapped", "switch_reason_plausible", "external_demand_observed"} and "J" not in codes:
        errors.append("business-model-diagnostic.md: market-reality status requires J evidence")
    if market_reality in {"alternatives_mapped", "switch_reason_plausible", "external_demand_observed"} and "A" not in codes:
        errors.append("business-model-diagnostic.md: market-reality status requires A evidence")

    if verdict == "limited_market_entry_supported":
        if market_reality != "external_demand_observed":
            errors.append("business-model-diagnostic.md: limited_market_entry_supported requires external_demand_observed")
        if object_proof not in {"early_object_signal", "independent_object_proof"}:
            errors.append("business-model-diagnostic.md: limited_market_entry_supported requires object-specific evidence")
        if not independent_object_rows:
            errors.append("business-model-diagnostic.md: limited_market_entry_supported requires independent object outcome evidence")
    if verdict == "switch_hypothesis_testable" and not {"J", "A", "G", "T"}.issubset(codes):
        errors.append("business-model-diagnostic.md: switch_hypothesis_testable requires J/A/G/T evidence")
    if verdict == "problem_and_alternatives_mapped" and not {"J", "A"}.issubset(codes):
        errors.append("business-model-diagnostic.md: problem_and_alternatives_mapped requires J/A evidence")
    if verdict == "market_research_required" and ({"J", "A"} & codes):
        errors.append("business-model-diagnostic.md: market_research_required conflicts with observed J/A evidence")
    if verdict == "scale_evidence_required" and not independent_object_rows:
        errors.append("business-model-diagnostic.md: scale_evidence_required requires independent object evidence")

    map_by_area = {row.get("area", "").strip(): row for row in map_rows}
    for area, needed_codes in AREA_CODES.items():
        row = map_by_area.get(area)
        if not row:
            continue
        status = row.get("current_status", "").strip()
        evidence_ids = {item.strip() for item in (row.get("external_evidence_id") or "").split(";") if item.strip()}
        referenced = [ledger_rows[[r.get("evidence_id") for r in ledger_rows].index(eid)] for eid in evidence_ids if eid in {r.get("evidence_id") for r in ledger_rows}]
        independent_refs = [item for item in referenced if is_positive_independent(item)]
        if status == "supported" and not independent_refs:
            errors.append(f"business-model-diagnostic.md: supported {area} lacks independent evidence")
        if status == "external_evidence_missing" and any(
            item.get("market_claim_code", "").strip() == "O" for item in independent_refs
        ):
            errors.append(f"business-model-diagnostic.md: external_evidence_missing {area} has independent object evidence")
    return errors


def validate_directory(path: Path, strict: bool = True) -> tuple[list[str], dict[str, object]]:
    errors: list[str] = []
    object_path = path / "object-card.md"
    channel_path = path / "channel-inventory.csv"
    alternative_path = path / "alternative-map.csv"
    ledger_path = path / "external-evidence-ledger.csv"
    map_path = path / "business-model-hypothesis-map.csv"
    report_path = path / "business-model-diagnostic.md"
    for required in (object_path, channel_path, alternative_path, ledger_path, map_path, report_path):
        if not required.is_file():
            errors.append(f"missing required file: {required.name}")

    channel_ids: set[str] = set()
    ledger_rows: list[dict[str, str]] = []
    map_rows: list[dict[str, str]] = []
    if object_path.is_file():
        errors.extend(validate_object_card(object_path))
    if channel_path.is_file():
        channel_errors, channel_ids, _ = validate_channels(channel_path)
        errors.extend(channel_errors)
    if alternative_path.is_file():
        errors.extend(validate_alternatives(alternative_path))
    if ledger_path.is_file():
        ledger_errors, ledger_rows = validate_ledger(ledger_path, channel_ids, strict=strict)
        errors.extend(ledger_errors)
    if map_path.is_file():
        map_errors, map_rows = validate_map(map_path, ledger_rows, strict=strict)
        errors.extend(map_errors)
    if report_path.is_file():
        errors.extend(validate_diagnostic(report_path, ledger_rows, map_rows, strict=strict))
    stats: dict[str, object] = {
        "ledger_rows": len(ledger_rows),
        "sources": len(unique_nonempty([row.get("source_url_or_locator", "") for row in ledger_rows])),
        "independent_sources": len(unique_nonempty([
            row.get("source_url_or_locator", "") for row in ledger_rows if is_positive_independent(row)
        ])),
    }
    return errors, stats


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("diagnostic_directory")
    parser.add_argument("--legacy", action="store_true", help="run the old structural gate only")
    args = parser.parse_args(argv)
    directory = Path(args.diagnostic_directory).expanduser().resolve()
    if not directory.is_dir():
        print(f"ERROR: not a directory: {directory}")
        return 2
    strict = not args.legacy
    errors, stats = validate_directory(directory, strict=strict)
    mode = "LEGACY STRUCTURAL" if not strict else "STRICT EVIDENCE"
    if errors:
        print(f"MULTICHANNEL EXTERNAL DIAGNOSTIC: {mode} FAIL")
        for error in errors:
            print(f"- {error}")
        return 1
    print(f"MULTICHANNEL EXTERNAL DIAGNOSTIC: {mode} PASS")
    print(
        "Evidence: "
        f"{stats['ledger_rows']} observations, {stats['sources']} sources, "
        f"{stats['independent_sources']} independent sources."
    )
    print("Reminder: validation checks reasoning discipline; it does not prove source truth, demand, PMF or success.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
