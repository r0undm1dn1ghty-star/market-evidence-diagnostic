# Examples / Баттлтесты

Реальные прогоны скилла на обезличенных данных. Каждый — с входом, ходом, результатом, бенчмарком.

## Баттлтест 2026-09-16 — реальные бизнес-модели

Главный отчёт: [`diagnostic-battle-2026-09-16.md`](diagnostic-battle-2026-09-16.md) — Yandex AI Studio, Kwork, Avito: что рынок позволяет утверждать, а что преждевременно.

Структурированные pack'и (все прошли `python skill/scripts/validate_diagnostic.py`):

| Объект | Market reality | Object proof | Verdict |
|---|---|---|---|
| [yandex-ai-studio/](diagnostic-battle-2026-09-16/yandex-ai-studio) | `alternatives_mapped` | `self_claim_only` | `switch_hypothesis_testable` |
| [kwork/](diagnostic-battle-2026-09-16/kwork) | `external_demand_observed` | `independent_object_proof` | `limited_market_entry_supported` |
| [avito/](diagnostic-battle-2026-09-16/avito) | `external_demand_observed` | `independent_object_proof` | `channel_or_economics_evidence_required` |

Главный результат баттлтеста: протокол различает модели по доказательной силе их claims — «30 000+ агентов» и CPL-кейсы не превращаются в proof of demand, а рыночная оценка «21,4 млрд ₽» не воспроизводится в независимых источниках.

## Fictional demo

[`fictional-static-export/`](fictional-static-export/) — полностью вымышленный pack для демонстрации структуры протокола.
