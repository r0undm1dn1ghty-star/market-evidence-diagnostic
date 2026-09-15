#!/usr/bin/env python3
"""Validate a multichannel external business-model evidence diagnostic.

Usage:
    python validate_diagnostic.py <diagnostic_directory>

The check verifies research artifacts and provenance fields. It cannot verify
source truth, market demand, causal impact, or business success.
"""
from __future__ import annotations

import csv
import sys
from pathlib import Path

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
ALLOWED_ALTERNATIVE_TYPES = {
    "DIY", "doing_nothing", "incumbent", "direct_competitor", "service_alternative",
}
ALLOWED_SOURCE_CLASSES = {
    "independent_behavior", "independent_account", "competitor_docs",
    "object_self_claim", "owner_operational_data",
}
ALLOWED_SIDES = {"object_side", "buyer_side", "alternative_side", "owner_private"}
ALLOWED_ACCESS_MODES = {"public_web", "user_file_export", "authorized_connector"}
ALLOWED_CHANNEL_STATUS = {"checked", "not_available", "optional"}
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
REQUIRED_SECTIONS = (
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


def headers_or_error(path: Path, expected: set[str]) -> tuple[list[dict[str, str]], list[str]]:
    with path.open(encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        missing = expected - set(reader.fieldnames or [])
        if missing:
            return [], [f"{path.name}: missing header(s): {', '.join(sorted(missing))}"]
        return list(reader), []


def validate_object_card(path: Path) -> list[str]:
    text = path.read_text(encoding="utf-8")
    required = ("## Исследовательская единица", "| Объект |", "| Роль / buyer |", "| Ситуация |", "| Current alternative |", "| Claim объекта |")
    return [f"object-card.md: missing required field/section {item!r}" for item in required if item not in text]


def validate_channels(path: Path) -> tuple[list[str], set[str]]:
    rows, errors = headers_or_error(path, REQUIRED_CHANNEL_HEADERS)
    if errors:
        return errors, set()
    ids: set[str] = set()
    checked_sides: set[str] = set()
    for row_num, row in enumerate(rows, start=2):
        identifier = (row.get("channel_id") or "").strip()
        side = (row.get("side") or "").strip()
        mode = (row.get("access_mode") or "").strip()
        status = (row.get("status") or "").strip()
        for field in ("channel_id", "side", "channel_type", "access_mode", "locator_or_query", "purpose", "does_not_prove", "status"):
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
        if status == "checked":
            checked_sides.add(side)
    for required_side in ("object_side", "buyer_side", "alternative_side"):
        if required_side not in checked_sides:
            errors.append(f"channel-inventory.csv: requires one checked {required_side} channel")
    return errors, ids


def validate_alternatives(path: Path) -> list[str]:
    rows, errors = headers_or_error(path, REQUIRED_ALTERNATIVE_HEADERS)
    if errors:
        return errors
    if len(rows) < 3:
        errors.append("alternative-map.csv: requires at least 3 current alternatives/direct competitors")
    seen: set[str] = set()
    for row_num, row in enumerate(rows, start=2):
        identifier = (row.get("alternative_id") or "").strip()
        kind = (row.get("alternative_type") or "").strip()
        source_class = (row.get("source_class") or "").strip()
        for field in ("alternative_id", "alternative_name", "role_or_buyer", "situation_or_job", "why_relevant", "source_url", "source_class"):
            if not (row.get(field) or "").strip():
                errors.append(f"alternative-map.csv:{row_num}: missing {field}")
        if identifier in seen:
            errors.append(f"alternative-map.csv:{row_num}: duplicate alternative_id {identifier!r}")
        seen.add(identifier)
        if kind not in ALLOWED_ALTERNATIVE_TYPES:
            errors.append(f"alternative-map.csv:{row_num}: invalid alternative_type {kind!r}")
        if source_class not in ALLOWED_SOURCE_CLASSES:
            errors.append(f"alternative-map.csv:{row_num}: invalid source_class {source_class!r}")
    return errors


def validate_ledger(path: Path, channel_ids: set[str]) -> list[str]:
    rows, errors = headers_or_error(path, REQUIRED_LEDGER_HEADERS)
    if errors:
        return errors
    codes: set[str] = set()
    non_self_claim = 0
    for row_num, row in enumerate(rows, start=2):
        code = (row.get("market_claim_code") or "").strip()
        channel_id = (row.get("channel_id") or "").strip()
        side = (row.get("side") or "").strip()
        mode = (row.get("access_mode") or "").strip()
        source_class = (row.get("source_class") or "").strip()
        for field in ("evidence_id", "channel_id", "side", "access_mode", "market_claim_code", "claim_supported", "observation_or_quote", "source_name", "source_url_or_locator", "source_class", "what_it_does_not_prove"):
            if not (row.get(field) or "").strip():
                errors.append(f"external-evidence-ledger.csv:{row_num}: missing {field}")
        if channel_id not in channel_ids:
            errors.append(f"external-evidence-ledger.csv:{row_num}: unknown channel_id {channel_id!r}")
        if side not in ALLOWED_SIDES:
            errors.append(f"external-evidence-ledger.csv:{row_num}: invalid side {side!r}")
        if mode not in ALLOWED_ACCESS_MODES:
            errors.append(f"external-evidence-ledger.csv:{row_num}: invalid access_mode {mode!r}")
        if code not in {"J", "A", "G", "T", "F", "O", "C", "M", "R"}:
            errors.append(f"external-evidence-ledger.csv:{row_num}: invalid market_claim_code {code!r}")
        else:
            codes.add(code)
        if source_class not in ALLOWED_SOURCE_CLASSES:
            errors.append(f"external-evidence-ledger.csv:{row_num}: invalid source_class {source_class!r}")
        if source_class != "object_self_claim":
            non_self_claim += 1
    if len(rows) < 3:
        errors.append("external-evidence-ledger.csv: requires at least 3 sourced observations")
    if non_self_claim < 2:
        errors.append("external-evidence-ledger.csv: requires at least 2 non-self-claim sources")
    missing_core = {"J", "A", "G", "T", "F"} - codes
    if missing_core:
        errors.append(f"external-evidence-ledger.csv: missing core market claim code(s): {', '.join(sorted(missing_core))}")
    return errors


def validate_map(path: Path) -> list[str]:
    rows, errors = headers_or_error(path, REQUIRED_MAP_HEADERS)
    if errors:
        return errors
    seen: set[str] = set()
    covered: set[str] = set()
    for row_num, row in enumerate(rows, start=2):
        identifier = (row.get("id") or "").strip()
        area = (row.get("area") or "").strip()
        status = (row.get("current_status") or "").strip()
        for field in ("id", "area", "comparative_hypothesis", "current_status", "alternative_ids", "private_evidence_needed", "minimum_evidence_needed", "blocks_verdict"):
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
        if status == "supported" and not (row.get("external_evidence_summary") or "").strip():
            errors.append(f"business-model-hypothesis-map.csv:{row_num}: supported claim requires external_evidence_summary")
    missing = REQUIRED_AREAS - covered
    if missing:
        errors.append(f"business-model-hypothesis-map.csv: missing required area(s): {', '.join(sorted(missing))}")
    return errors


def validate_diagnostic(path: Path) -> list[str]:
    text = path.read_text(encoding="utf-8")
    errors = []
    for section in REQUIRED_SECTIONS:
        if section not in text:
            errors.append(f"business-model-diagnostic.md: missing section {section!r}")
    if "**Market reality:**" not in text or not any(f"`{item}`" in text for item in ALLOWED_MARKET_REALITY):
        errors.append("business-model-diagnostic.md: missing allowed market-reality status")
    if "**Object proof:**" not in text or not any(f"`{item}`" in text for item in ALLOWED_OBJECT_PROOF):
        errors.append("business-model-diagnostic.md: missing allowed object-proof status")
    if "**Verdict готовности:**" not in text or not any(f"`{item}`" in text for item in ALLOWED_VERDICTS):
        errors.append("business-model-diagnostic.md: missing allowed readiness verdict")
    for marker in ("Рынок уже позволяет утверждать:", "Объект сам пока доказал:", "Нельзя пока утверждать:"):
        if marker not in text:
            errors.append(f"business-model-diagnostic.md: missing evidence boundary {marker!r}")
    return errors


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: validate_diagnostic.py <diagnostic_directory>")
        return 2
    directory = Path(sys.argv[1]).expanduser().resolve()
    if not directory.is_dir():
        print(f"ERROR: not a directory: {directory}")
        return 2
    errors: list[str] = []
    object_path = directory / "object-card.md"
    channel_path = directory / "channel-inventory.csv"
    alternative_path = directory / "alternative-map.csv"
    ledger_path = directory / "external-evidence-ledger.csv"
    map_path = directory / "business-model-hypothesis-map.csv"
    report_path = directory / "business-model-diagnostic.md"
    if not object_path.is_file():
        errors.append("missing required file: object-card.md")
    else:
        errors.extend(validate_object_card(object_path))
    channel_ids: set[str] = set()
    if not channel_path.is_file():
        errors.append("missing required file: channel-inventory.csv")
    else:
        channel_errors, channel_ids = validate_channels(channel_path)
        errors.extend(channel_errors)
    if not alternative_path.is_file():
        errors.append("missing required file: alternative-map.csv")
    else:
        errors.extend(validate_alternatives(alternative_path))
    if not ledger_path.is_file():
        errors.append("missing required file: external-evidence-ledger.csv")
    else:
        errors.extend(validate_ledger(ledger_path, channel_ids))
    if not map_path.is_file():
        errors.append("missing required file: business-model-hypothesis-map.csv")
    else:
        errors.extend(validate_map(map_path))
    if not report_path.is_file():
        errors.append("missing required file: business-model-diagnostic.md")
    else:
        errors.extend(validate_diagnostic(report_path))
    if errors:
        print("MULTICHANNEL EXTERNAL DIAGNOSTIC: FAIL")
        for error in errors:
            print(f"- {error}")
        return 1
    print("MULTICHANNEL EXTERNAL DIAGNOSTIC: PASS")
    print("Object, channels, alternatives, sourced evidence and comparative model coverage are present.")
    print("Reminder: this check does not prove source truth, demand, PMF or commercial success.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
