# Внешняя диагностика бизнес-модели — [объект]

**Дата:**
**Тип бизнеса:** B2B SaaS / сервис / consumer / marketplace / OSS / другое
**Риск, который хотят принять:** launch / сегмент / канал / pricing / масштабирование
**Внешние источники:** [число] источников; [число] независимых; [число] self-claims
**Граница диагностики:** Что недоступно извне и требует данных владельца.

## 1. Короткий вывод

**Market reality:** `market_unmapped` / `job_observed` / `alternatives_mapped` / `switch_reason_plausible` / `external_demand_observed`.
**Object proof:** `self_claim_only` / `early_object_signal` / `independent_object_proof` / `private_evidence_required`.
**Verdict готовности:** `market_research_required` / `problem_and_alternatives_mapped` / `switch_hypothesis_testable` / `limited_market_entry_supported` / `channel_or_economics_evidence_required` / `scale_evidence_required` / `insufficient_evidence`.

> **Рынок уже позволяет утверждать:** [что известно о job/alternatives/transaction].
> **Объект сам пока доказал:** [только то, что подтверждено отдельно].
> **Нельзя пока утверждать:** [какой рыночный или object claim и почему].

## 2. Объект исследования и текущая альтернатива

| Роль / buyer | Ситуация и job | Current alternative | Claim объекта | Unit of value |
|---|---|---|---|---|
|  |  |  |  |  |

Полный объект — `object-card.md`.

## 3. Проверенные коммуникационные каналы

| Канал | Сторона | Что наблюдалось | Какие claims поддерживает | Что не доказывает | Статус |
|---|---|---|---|---|---|
| Website/pricing/docs | Object-side |  | A / T / O | Demand / usage / payment | checked |
| Launch/social/community | Object-side |  | O / C | Payment / retention | checked / not available |
| Reviews/community/marketplace | Buyer-side |  | J / A / G / F | Frequency / WTP | checked / not available |
| Competitor pricing/docs | Alternative-side |  | A / T / F | Usage / PMF | checked |
| CRM/analytics/billing/support | Owner-private |  | O / U / V / C / M / R | Beyond supplied data | optional / not available |

Полный inventory — `channel-inventory.csv`.

## 4. Карта альтернатив и прямых конкурентов

| Альтернатива | Тип | Какую работу решает | Для кого | Цена / unit | Switching friction | Почему близка |
|---|---|---|---|---|---|---|
|  | DIY / doing nothing / incumbent / direct competitor / service alternative |  |  |  |  |  |
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |

Полная таблица — `alternative-map.csv`.

## 5. Внешние следы спроса и переключения

| Claim | Независимое наблюдение | Сила / класс источника | Что это не доказывает |
|---|---|---|---|
| J — job reality |  | high / medium / low |  |
| A — alternatives |  | high / medium / low |  |
| G — switch gap |  | high / medium / low |  |
| T — transaction |  | high / medium / low |  |
| F — friction |  | high / medium / low |  |
| O — object proof |  | high / medium / low |  |

Полный provenance ledger — `external-evidence-ledger.csv`.

## 6. Сравнительная карта claims бизнес-модели

| ID | Область | Что должно быть правдой относительно альтернатив | Статус | Внешнее доказательство | Что осталось private/unknown |
|---|---|---|---|---|---|
| P-01 | Проблема |  | untested / weakly_supported / supported / contradictory / disproven / unknown / external_evidence_missing |  |  |
| S-01 | Сегмент |  |  |  |  |
| V-01 | Обмен ценностью |  |  |  |  |
| U-01 | Полезный результат |  |  |  |  |
| C-01 | Доступ к покупателям |  |  |  |  |
| M-01 | Деньги и delivery |  |  |  |  |
| R-01 | Устойчивость |  |  |  |  |

Полная таблица — `business-model-hypothesis-map.csv`.

## 7. Блокирующие evidence gaps

| Приоритет | Claim, который нельзя говорить | Почему рынок/объект его ещё не поддерживают | Внешнее evidence, которое ещё можно собрать | Private data от владельца |
|---:|---|---|---|---|
| 1 |  |  |  |  |
| 2 |  |  |  |  |
| 3 |  |  |  |  |

## 8. Требования для смены verdict

| Gap | Какое наблюдение станет достаточным | У какого объекта его искать | Что не будет достаточным |
|---|---|---|---|
|  |  | Рынок / конкурент / владелец |  |

## 9. Ограничения вывода

- Цена конкурента доказывает наличие commercial offer, но не его usage или PMF.
- Лайки, launch-посты, ratings или installs без поведения не доказывают transaction/retention.
- Внешнее исследование не заменяет CRM, retention, invoices, unit economics и customer-side evidence владельца.
- Verdict не прогнозирует выручку или успех объекта; он ограничивает доказательные claims о рынке и готовности объекта.
