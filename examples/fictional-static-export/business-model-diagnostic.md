# Внешняя диагностика бизнес-модели — ExportKit (fictional example)

> **Полностью synthetic demonstration. Все названия, URLs, источники и observations в этом pack вымышлены и существуют только для показа формата.**

**Дата:** 2026-08-17
**Тип бизнеса:** Вымышленный B2B SaaS / service
**Риск, который хотят принять:** Ограниченный выход к независимым веб-разработчикам
**Внешние источники:** 6 synthetic источников; 5 modelled non-self-claim; 1 modelled self-claim
**Граница диагностики:** Нет реальных invoices, completion events, support cost или attribution.

## 1. Короткий вывод

**Market reality:** `alternatives_mapped`.
**Object proof:** `self_claim_only`.
**Verdict готовности:** `switch_hypothesis_testable`.

> **Рынок уже позволяет утверждать:** только то, что transfer job может иметь DIY, incumbent и service alternatives с наблюдаемыми synthetic price/scope signals.
> **Объект сам пока доказал:** лишь наличие synthetic owner offer; outcome, payment и repeatability не подтверждены.
> **Нельзя пока утверждать:** что реальные покупатели готовы платить вымышленному ExportKit или что он лучше alternatives.

## 2. Объект исследования и текущая альтернатива

| Роль / buyer | Ситуация и job | Current alternative | Claim объекта | Unit of value |
|---|---|---|---|---|
| Независимый веб-разработчик | Передать небольшой клиентский сайт без ежемесячной builder subscription | Manual rebuild, builder subscription, migration service | Быстрый статический перенос с меньшим риском | Разовый перенос сайта |

Полный объект находится в `object-card.md`.

## 3. Проверенные коммуникационные каналы

| Канал | Сторона | Что наблюдалось | Claims | Что не доказывает | Статус |
|---|---|---|---|---|---|
| Owner demo/pricing | Object-side | Synthetic offer и price page | A / T / O | Demand / outcome | checked |
| Practitioner discussion | Buyer-side | Synthetic manual workaround | J / G / F | Frequency / WTP | checked |
| Builder/service docs | Alternative-side | Synthetic units и scope alternatives | A / T / F | Usage / PMF | checked |
| Analytics export | Owner-private | Data не supplied | U / R | Private performance claims | optional |

Полный inventory находится в `channel-inventory.csv`.

## 4. Карта альтернатив и прямых конкурентов

| Альтернатива | Тип | Какую работу решает | Для кого | Цена / unit | Switching friction | Почему близка |
|---|---|---|---|---|---|---|
| Manual HTML rebuild | DIY | Передать сайт на свой hosting | Веб-разработчик | Время разработчика | Time/quality risk | Тот же job без продукта |
| Builder subscription | Incumbent | Держать сайт работающим | Веб-разработчик/клиент | Monthly subscription | Live dependencies | Status quo |
| Migration agency | Service alternative | Перенести сайт | Веб-разработчик | Fixed project price | Handoff/scheduling | Тот же output как услуга |

Полная таблица находится в `alternative-map.csv`.

## 5. Внешние следы спроса и переключения

| Claim | Модель наблюдения | Сила / класс источника | Что это не доказывает |
|---|---|---|---|
| J — job reality | Synthetic practitioner описывает manual rebuild | medium / independent account | Частоту job |
| A — alternatives | Synthetic builder и migration service публикуют offer | medium / competitor docs | Usage/PMF alternatives |
| G — switch gap | Manual rebuild имеет time/quality burden | medium / independent account | Object outcome |
| T — transaction | Service alternative публикует project price | medium / competitor docs | Object willingness to pay |
| F — friction | Builder имеет live dependencies | medium / competitor docs | Object conversion |
| O — object proof | Есть только owner demo | low / object self-claim | Independent object proof |

Полный provenance ledger находится в `external-evidence-ledger.csv`.

## 6. Сравнительная карта claims бизнес-модели

| ID | Область | Что должно быть правдой относительно alternatives | Статус | Внешнее evidence | Что осталось private/unknown |
|---|---|---|---|---|---|
| P-01 | Проблема | Есть migration job и workaround | weakly_supported | E-01 | Частота/сила job |
| S-01 | Сегмент | Есть повторяемая роль/context | weakly_supported | E-02 | Buyer cohort |
| V-01 | Обмен ценностью | Есть unit оплаты за alternative | weakly_supported | E-04 | Object payment |
| U-01 | Полезный результат | Object лучше manual/service alternative | external_evidence_missing | E-03 | Completed outcome |
| C-01 | Доступ к покупателям | Role discoverable in category | weakly_supported | E-02 | Object attribution |
| M-01 | Деньги и delivery | Market unit может покрыть object cost | external_evidence_missing | E-04 | Object unit economics |
| R-01 | Устойчивость | Differentiated outcome повторяется | unknown | E-06 | Repeat cohorts |

Полная карта находится в `business-model-hypothesis-map.csv`.

## 7. Блокирующие evidence gaps

| Приоритет | Claim, который нельзя говорить | Почему он не поддержан | Внешнее evidence, которое ещё можно собрать | Минимальные private data |
|---:|---|---|---|---|
| 1 | Object reliably better | Нет verified object outcome | Real public reviews/cases с проверяемой provenance | Completed transfers без PII |
| 2 | Buyers will pay object | Есть только alternative price | Реальные service comparisons и buyer-side evidence | Invoices/pilots со scope |
| 3 | Model can scale | Нет repeated object evidence | Реальные category patterns | Cohorts и support-cost bands |

## 8. Требования для смены verdict

| Gap | Достаточное наблюдение | У какого объекта искать | Что не будет достаточным |
|---|---|---|---|
| Object outcome | Completed transfer сравнён с current alternative | Владелец/пользователь объекта | Demo screen |
| Paid exchange | Invoice или pilot с stated scope | Владелец | Competitor price page |
| Repeat access | Source-to-qualified activation across cycles | Владелец | Один launch post |

## 9. Ограничения вывода

Цена alternative доказывает только наличие commercial offer, а не его usage, margin или PMF. Лайки, launch posts, ratings или installs без поведенческого следа не доказывают transaction/retention. Внешнее исследование не заменяет CRM, retention, invoices, unit economics и customer-side evidence владельца. Verdict не прогнозирует выручку или успех объекта; он лишь ограничивает claims, которые можно обоснованно делать о рынке и готовности объекта.
