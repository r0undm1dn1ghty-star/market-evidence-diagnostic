#!/usr/bin/env python3
"""Adversarial regression tests for validate_diagnostic.py.

Each scenario mutates a copy of the valid fixture into an overreach case and
asserts that the strict validator rejects it. Run:

    python skill/scripts/test_adversarial.py
"""
from __future__ import annotations

import csv
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
VALID = ROOT / "skill" / "fixtures" / "valid-diagnostic"
VALIDATOR = ROOT / "skill" / "scripts" / "validate_diagnostic.py"


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def write_csv(path: Path, rows: list[dict[str, str]]) -> None:
    if not rows:
        return
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def run_validator(directory: Path) -> tuple[int, str]:
    proc = subprocess.run(
        [sys.executable, str(VALIDATOR), str(directory)],
        capture_output=True,
        text=True,
        timeout=120,
    )
    return proc.returncode, proc.stdout + proc.stderr


def scenario_single_source(base: Path, tmp: Path) -> str:
    """All evidence rows point at one URL -> strict must reject (<2 independent locators)."""
    work = tmp / "single_source"
    shutil.copytree(base, work)
    ledger = read_csv(work / "external-evidence-ledger.csv")
    for row in ledger:
        if row["source_class"] != "object_self_claim":
            row["source_url_or_locator"] = "https://example.com/one-source"
    write_csv(work / "external-evidence-ledger.csv", ledger)
    return "external-evidence-ledger.csv"


def scenario_selfbacked_supported(base: Path, tmp: Path) -> str:
    """A map row claims supported but references only the self-claim evidence."""
    work = tmp / "selfbacked_supported"
    shutil.copytree(base, work)
    rows = read_csv(work / "business-model-hypothesis-map.csv")
    for row in rows:
        if row["id"] == "S-01":
            row["external_evidence_id"] = "E-06"  # object_self_claim
            row["current_status"] = "supported"
    write_csv(work / "business-model-hypothesis-map.csv", rows)
    return "business-model-hypothesis-map.csv"


def scenario_inflated_verdict(base: Path, tmp: Path) -> str:
    """limited_market_entry_supported while object proof is self_claim_only."""
    work = tmp / "inflated_verdict"
    shutil.copytree(base, work)
    report = (work / "business-model-diagnostic.md").read_text(encoding="utf-8")
    report = report.replace("**Object proof:** `self_claim_only`.", "**Object proof:** `self_claim_only`.")
    report = report.replace(
        "**Verdict готовности:** `switch_hypothesis_testable`.",
        "**Verdict готовности:** `limited_market_entry_supported`.",
    )
    (work / "business-model-diagnostic.md").write_text(report, encoding="utf-8")
    return "business-model-diagnostic.md"


def scenario_future_date(base: Path, tmp: Path) -> str:
    """A ledger row dated in the future must be rejected."""
    work = tmp / "future_date"
    shutil.copytree(base, work)
    ledger = read_csv(work / "external-evidence-ledger.csv")
    ledger[0]["source_date"] = "2099-01-01"
    write_csv(work / "external-evidence-ledger.csv", ledger)
    return "external-evidence-ledger.csv"


def scenario_overclaimed_confidence(base: Path, tmp: Path) -> str:
    """high confidence with a small source base must be rejected."""
    work = tmp / "overclaimed_confidence"
    shutil.copytree(base, work)
    report = (work / "business-model-diagnostic.md").read_text(encoding="utf-8")
    report = report.replace("**Уверенность вывода:** `medium`.", "**Уверенность вывода:** `high`.")
    (work / "business-model-diagnostic.md").write_text(report, encoding="utf-8")
    return "business-model-diagnostic.md"


def scenario_missing_adversarial(base: Path, tmp: Path) -> str:
    """Strict requires the adversarial self-check section."""
    work = tmp / "missing_adversarial"
    shutil.copytree(base, work)
    report = (work / "business-model-diagnostic.md").read_text(encoding="utf-8")
    start = report.index("## 10. Adversarial self-check")
    end = report.index("\n## ", start + 5) if "\n## " in report[start + 5:] else len(report)
    report = report[:start] + report[end:]
    (work / "business-model-diagnostic.md").write_text(report, encoding="utf-8")
    return "business-model-diagnostic.md"


SCENARIOS = [
    ("single_source", scenario_single_source, "independent source"),
    ("selfbacked_supported", scenario_selfbacked_supported, "supported claim"),
    ("inflated_verdict", scenario_inflated_verdict, "limited_market_entry"),
    ("future_date", scenario_future_date, "future"),
    ("overclaimed_confidence", scenario_overclaimed_confidence, "high confidence"),
    ("missing_adversarial", scenario_missing_adversarial, "Adversarial self-check"),
]


def main() -> int:
    failures: list[str] = []
    with tempfile.TemporaryDirectory() as tmp_name:
        tmp = Path(tmp_name)
        for name, mutate, expected_fragment in SCENARIOS:
            work = tmp / name
            scenario_file = mutate(VALID, tmp)
            code, output = run_validator(work)
            ok = code == 1 and expected_fragment.lower() in output.lower()
            status = "PASS" if ok else "FAIL"
            print(f"[{status}] {name}: expected rejection mentioning {expected_fragment!r}")
            if not ok:
                failures.append(name)
                print(f"  exit={code}\n  output:\n{output}")
    if failures:
        print(f"ADVERSARIAL SUITE: FAIL ({len(failures)} of {len(SCENARIOS)} scenarios did not reject)")
        return 1
    print(f"ADVERSARIAL SUITE: PASS ({len(SCENARIOS)}/{len(SCENARIOS)} overreach scenarios rejected)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
