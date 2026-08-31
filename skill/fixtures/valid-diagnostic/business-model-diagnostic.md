# Внешняя диагностика бизнес-модели — ExportKit

**Дата:** 2026-08-17
**Тип бизнеса:** B2B SaaS / сервис
**Риск, который хотят принять:** Ограниченный выход к веб-разработчикам
**Внешние источники:** 6 источников; 5 не-self-claim; 1 self-claim
**Граница диагностики:** Нет private invoices, completion events, support cost и attribution.

## 1. Короткий вывод

**Market reality:** `alternatives_mapped`.
**Object proof:** `self_claim_only`.
**Verdict готовности:** `switch_hypothesis_testable`.

> **Рынок уже позволяет утверждать:** задача передачи/миграции небольших сайтов имеет DIY, incumbent и service alternatives с observable price/frequency signals.
> **Объект сам пока доказал:** только наличие demo и заявленного offer.
> **Нельзя пока утверждать:** что ExportKit даёт более надёжный outcome или что покупатели готовы платить именно ему.

## 2. Объект исследования и текущая альтернатива

| Роль / buyer | Ситуация и job | Current alternative | Claim объекта | Unit of value |
|---|---|---|---|---|
| Независимый веб-разработчик | Передать небольшой клиентский сайт без ежемесячной подписки | Ручная пересборка, builder subscription, migration service | Быстрый статический перенос с меньшим риском | Разовый перенос |

Полный объект — `object-card.md`.

## 3. Проверенные коммуникационные каналы

| Канал | Сторона | Что наблюдалось | Какие утверждения поддерживает | Что не доказывает | Статус |
|---|---|---|---|---|---|
| Owner demo/pricing | Object-side | Offer and price | A / T / O | Demand / outcome | checked |
| Practitioner discussion | Buyer-side | Manual workaround | J / G / F | Frequency / WTP | checked |
| Builder/service docs | Alternative-side | Alternative units and scope | A / T / F | Usage / PMF | checked |
| Analytics export | Owner-private | No data supplied | U / R | Any private performance claim | optional |

Полный inventory — `channel-inventory.csv`.

## 4. Карта альтернатив и прямых конкурентов

| Альтернатива | Тип | Какую работу решает | Для кого | Цена / unit | Switching friction | Почему близка |
|---|---|---|---|---|---|---|
| Manual HTML rebuild | DIY | Передать сайт на свой hosting | Веб-разработчик | Время разработчика | Time/quality risk | Тот же job без продукта |
| Builder subscription | Incumbent | Держать сайт работающим | Веб-разработчик/клиент | Monthly subscription | Live dependencies | Status quo |
| Migration agency | Service alternative | Перенести сайт | Веб-разработчик | Fixed project price | Handoff/scheduling | Тот же output как услуга |

Полная таблица — `alternative-map.csv`.

## 5. Внешние следы спроса и переключения

| Claim | Независимое наблюдение | Сила / класс источника | Что это не доказывает |
|---|---|---|---|
| J — job reality | Practitioner describes manual rebuild to remove subscription | medium / independent account | Частоту job |
| A — alternatives | Builder and migration service publish their offers | medium / competitor docs | Usage/PMF alternatives |
| G — switch gap | Manual rebuild has observable time/quality burden | medium / independent account | Object outcome |
| T — transaction | Migration service has project price | medium / competitor docs | Object willingness to pay |
| F — friction | Builder has live dependencies | medium / competitor docs | Object conversion |
| O — object proof | Only owner demo is available | low / object self claim | Independent object proof |

Полный provenance ledger — `external-evidence-ledger.csv`.

## 6. Сравнительная карта утверждений бизнес-модели

| ID | Область | Что должно быть правдой относительно альтернатив | Статус | Внешнее доказательство | Что осталось private/unknown |
|---|---|---|---|---|---|
| P-01 | Проблема | Есть migration job и workaround | weakly_supported | E-01 | Частота/сила job |
| S-01 | Сегмент | Есть повторяемая роль/context | weakly_supported | E-02 | Buyer cohort |
| V-01 | Обмен ценностью | Есть unit оплаты за альтернативу | weakly_supported | E-04 | Object payment |
| U-01 | Полезный результат | Object лучше manual/service alternative | external_evidence_missing | E-03 | Completed outcome |
| C-01 | Доступ к покупателям | Role discoverable in alternative category | weakly_supported | E-02 | Object attribution |
| M-01 | Деньги и delivery | Market unit can cover object cost | external_evidence_missing | E-04 | Object unit economics |
| R-01 | Устойчивость | Differentiated outcome repeats | unknown | E-06 | Repeat cohorts |

Полная таблица — `business-model-hypothesis-map.csv`.

## 7. Блокирующие evidence gaps

| Приоритет | Claim, который нельзя говорить | Почему рынок/объект его ещё не поддерживают | Внешнее evidence, которое ещё можно собрать | Private data от владельца |
|---:|---|---|---|---|
| 1 | Object is reliably better | No independent outcome | Reviews/cases | Completed transfers |
| 2 | Buyers will pay object | Only competitor price exists | Service comparison/reviews | Invoices/pilots |
| 3 | Model can scale | No repeat object evidence | Category patterns | Cohorts/support cost |

## 8. Требования для смены verdict

| Gap | Какое наблюдение станет достаточным | У какого объекта его искать | Что не будет достаточным |
|---|---|---|---|
| Object outcome | Completed transfer compared with current alternative | Владелец | Demo screen |
| Paid exchange | Invoice/pilot with stated scope | Владелец | Competitor price page |
| Repeat access | Source to qualified activation across cycles | Владелец | One launch post |

## 9. Ограничения вывода

- Цена конкурента доказывает наличие commercial offer, но не его usage или PMF.
- Лайки, launch-посты, ratings или installs без поведения не доказывают transaction/retention.
- Внешнее исследование не заменяет CRM, retention, invoices, unit economics и customer-side evidence владельца.
- Verdict не прогнозирует выручку или успех объекта; он ограничивает доказательные утверждения о рынке и готовности объекта.
