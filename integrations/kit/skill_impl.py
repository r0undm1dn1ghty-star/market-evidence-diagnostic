# -*- coding: utf-8 -*-
"""Реализация Market Evidence Diagnostic (strict) для skillkit.
Вход: {"claims": {...}, "evidence": [{source_class, date, sum}], "observed": n}."""
SKILL_NAME = "market-evidence-diagnostic"
SKILL_VERSION = "0.5.0"
SKILL_DESCRIPTION = ("Evidence-диагностика бизнес-модели: проверка заявлений против независимых "
                     "наблюдений. Вердикт + уверенность + adversarial self-check.")
INPUT_SCHEMA = {"type": "object", "properties": {
    "input": {"type": "object", "properties": {
        "claims": {"type": "object"}, "evidence": {"type": "array"}}}}, "required": ["input"]}
OUTPUT_SCHEMA = {"type": "object", "properties": {
    "verdict": {"type": "string"}, "confidence": {"type": "string"},
    "independent_locators": {"type": "integer"}, "adversarial": {"type": "array"}}}
SYSTEM_PROMPT = """Ты — диагност бизнес-моделей по строгому evidence-протоколу.
ПРАВИЛА: (1) «supported» требует независимого наблюдения, а не заявления компании;
(2) вердикт выше switch_hypothesis_testable невозможен при одном независимом locator;
(3) high confidence требует 4+ источников, из них 3+ независимых;
(4) обязателен adversarial self-check: какой вывод ты бы сделал без сверки и чем он грозил.
Не выдумывай источники. Если данных мало — пиши «не наблюдаю» и понижай уверенность."""

LOCATOR_CLASSES = {"independent_behavior", "independent_third_party", "external_measurement", "regulatory"}
VERDICTS = ["not_testable", "switch_hypothesis_testable", "switch_supported", "switch_contradicted"]


def run(input_value=None, **kw):
    d = input_value if isinstance(input_value, dict) else {"text": str(input_value or "")}
    evidence = d.get("evidence") or []
    claims = d.get("claims") or {}
    locators = [e for e in evidence if e.get("source_class") in LOCATOR_CLASSES]
    indep = len({(e.get("source") or e.get("url") or str(i)) for i, e in enumerate(locators)})
    contradictions = [e for e in evidence if e.get("contradicts")]
    if d.get("observed") == 0 or not evidence:
        verdict, conf = "not_testable", "low"
    elif contradictions:
        verdict, conf = "switch_contradicted", "medium"
    elif indep >= 2 and any(e.get("supports") for e in evidence):
        verdict, conf = "switch_supported", "high" if len(evidence) >= 4 and indep >= 3 else "medium"
    else:
        verdict = "switch_hypothesis_testable"
        conf = "medium" if indep == 1 else "low"
    adversarial = [
        f"Какой вывод был бы сделан без независимой сверки: {claims.get('headline', '«заявление верно»')}",
        "Какая метрика может быть не тем, чем кажется (GMV vs выручка, DAU vs регистрации, заявка vs оплата)",
        "Где single-source: если независимый locator всего один — вердикт не выше гипотезы",
    ]
    return {"verdict": verdict, "confidence": conf, "independent_locators": indep,
            "evidence_count": len(evidence), "contradictions": len(contradictions),
            "adversarial": adversarial,
            "rule": "1 независимый locator -> вердикт не выше switch_hypothesis_testable (SKILL.md)."}
