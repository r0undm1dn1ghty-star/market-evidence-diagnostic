# Market Evidence Model v2

## Главная смена логики

**v1:** объект → его заявление → P/S/V/U/C/M/R → verdict.
**v2:** объект + job + current alternatives + direct competitors + external demand traces → сравнительные утверждения → P/S/V/U/C/M/R → verdict.

P/S/V/U/C/M/R остаются полезными, но не являются списком факторов, которые «управляют моделью». Это семь мест, в которых нужно проверить **право объекта на существование рядом с уже доступными способами решения работы**.

## Внешние утверждения, которые нужно проверить до P/S/V/U/C/M/R

| Код | Сравнительное утверждение | Вопрос к рынку | Сильное внешнее доказательство | Недостаточное доказательство |
|---|---|---|---|---|
| J | Job reality | Люди в определённой ситуации уже пытаются выполнить эту работу/избежать потери? | Complaint + costly workaround, repeated comparison/search, migration, paid service request. | Лендинг объекта говорит, что проблема есть. |
| A | Alternative landscape | Чем они решают работу сейчас, включая nothing/DIY? | 3+ observable alternatives with actual use/review/price/documentation. | Список «конкурентов» без близости к job. |
| G | Gap / switch reason | Почему объект может быть выбран вместо текущей альтернативы? | External pain in incumbent or observable difference in price/time/risk/coverage. | «Наш UX лучше» или feature list. |
| T | Transaction signal | За что рынок уже отдаёт деньги/время/доступ? | Public pricing + reviews/cases/marketplace transactions/hiring/commitments. | Price page объекта. |
| F | Friction | Что мешает переключению или внедрению? | Migration/lock-in, switching discussion, compliance, workflow coupling, cost/time observed externally. | «Пользователи консервативны». |
| O | Object proof | Что объект уже доказал именно против альтернатив? | Third-party review/case, product metric with provenance, named partner/implementation. | Founder post or website case without verification. |

## Как внешняя модель превращается в карту бизнес-модели

| Область модели | Проверяется через внешний контур | Вопрос про объект |
|---|---|---|
| P — проблема | J: job reality | Решает ли объект наблюдаемую потерю, а не сформулированную боль? |
| S — сегмент | J + A | Есть ли конкретная роль/ситуация, где alternatives повторяются? |
| V — обмен ценностью | T + F | Есть ли ресурсный выбор/цена и достаточно ли gap, чтобы переключиться? |
| U — полезный результат | G + O | Даёт ли объект результат, который альтернативы не дают или дают хуже? |
| C — доступ к покупателям | A + T | Где эта роль уже ищет/покупает альтернативы и может ли объект туда попасть? |
| M — деньги/delivery | T + F + O | Вписывается ли offer в observed market unit/economics и выдерживает ли delivery? |
| R — устойчивость | O + repeated T | Есть ли повторяемость выбора/результата, а не один launch signal? |

## Двухконтурный verdict

Окончательный verdict содержит два независимых слоя.

| Слой | Возможные статусы | Что означает |
|---|---|---|
| **Market reality** | `market_unmapped`, `job_observed`, `alternatives_mapped`, `switch_reason_plausible`, `external_demand_observed` | Насколько внешний рынок и возможности переключения исследованы. |
| **Object proof** | `self_claim_only`, `early_object_signal`, `independent_object_proof`, `private_evidence_required` | Насколько именно объект доказал своё право на утверждение. |

Нельзя заменять один слой другим. Сильный рынок не доказывает объект. Наличие working object не доказывает рынок.

## Правила verdict готовности

| Verdict | Требования к внешнему контуру | Требования к объекту |
|---|---|---|
| `market_research_required` | Нет J/A или current alternatives не определены. | Любые утверждения об объекте преждевременны. |
| `problem_and_alternatives_mapped` | J и A имеют независимые следы; F понятен. | Object proof может быть ещё слабым. |
| `switch_hypothesis_testable` | G и T сформулированы через сравнение с альтернативами. | Нужно получить pilot/usage/transaction объекта. |
| `limited_market_entry_supported` | External demand and alternatives are known; route/facility plausible. | Есть observed/purchased object outcome у ограниченной группы. |
| `channel_or_economics_evidence_required` | Market/object value observed. | Нет repeatable C/M evidence. |
| `scale_evidence_required` | Market and object proof exist. | Нет repeated object outcome/economics at volume. |

## Необходимый честный вывод

Если внешние источники нашли только конкурентные price pages и category noise, output не должен говорить «рынок подтверждён». Он должен сказать:

> **Есть коммерческая категория и набор альтернатив. Не найдено независимых следов того, что указанная роль регулярно выбирает объект/альтернативы именно в заявленном контексте. Нужны customer-side evidence или private owner data.**
