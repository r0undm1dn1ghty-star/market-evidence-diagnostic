# Каналы и доказательства

Начинайте не со списка ссылок, а с вопроса: **какой claim нужно проверить и где покупатель уже оставляет наблюдаемый след?**

## Минимальный внешний контур

| Сторона | Обязательно проверить | Почему |
|---|---|---|
| Object-side | Сайт/pricing/docs и ещё один публичный канал компании | Сайт показывает offer; второй канал помогает увидеть release, ecosystem, product trace или смену messaging. |
| Buyer-side | Reviews, community, marketplace, job board или публичное обсуждение | Здесь видны actual job language, workaround, friction и alternatives. |
| Alternative-side | Документацию/price ближайшего alternative и независимый buyer-side signal | Иначе comparison останется feature list двух лендингов. |

Если одного из каналов нет, запишите `not_available`. Это не ошибка. Ошибка — заполнить пробел уверенностью.

## Как выбирать канал

| Нужно понять | Начните с | Усильте, если требуется | Не принимайте за доказательство |
|---|---|---|---|
| Реальна ли работа | Reviews, forums, public communities, marketplaces | Anonymized support/interview export | Object landing page |
| Чем решают сейчас | Competitor docs/pricing, category pages, marketplace services | Public comparisons/migration stories | Список известных брендов |
| Почему могут switch | Negative reviews, migration guides, community workaround | Lost-deal/support evidence | Feature matrix |
| Есть ли transaction | Marketplace unit, procurement, pricing + reviews | Billing/CRM paid pilot export | Price page или waitlist |
| Работает ли объект | Third-party case, public review, app/GitHub signal | Analytics + support + billing export | Demo/video/screenshot |
| Можно ли повторять channel | Public search/partner/community route | CRM attribution and conversion export | Один launch post |
| Сходятся ли delivery и деньги | External implementation clues | Billing, support, cohort and operations export | Market-size slide |

## Как читать sources

Каждое наблюдение в ledger обязано иметь URL/locator, дату, source class, альтернативное объяснение и `what_it_does_not_prove`.

| Source class | Что он может дать | Чего он не доказывает сам |
|---|---|---|
| `independent_behavior` | Public action: review, migration, marketplace category, hiring, usage trace | Мотивацию, repeatability, causal effect. |
| `independent_account` | Customer/practitioner story or community discussion | Representative frequency or payment. |
| `competitor_docs` | Offer, price, scope, onboarding and contract structure | Adoption, quality, revenue, PMF. |
| `object_self_claim` | What the object says it does | Market demand, outcome or transaction. |
| `owner_operational_data` | Payment, outcome, retention, channel performance of the object | Market structure outside supplied sample. |

## Важный принцип: divergence важнее усреднения

Если сайт обещает «no-code migration in minutes», app-store reviews говорят «forms stop working», а marketplace services продают manual SEO migration, это не три усредняемых сигнала. Это три части модели: offer, buyer friction и service alternative. Зафиксируйте противоречие как evidence gap объекта.

## Private data: минимальный запрос

Не просите доступ к «всему CRM». Сначала запишите claim, который нельзя проверить снаружи. Затем попросите минимальный export:

| Claim | Минимальные поля |
|---|---|
| Paid value | Date, segment, amount/plan, paid/refunded — без contact PII. |
| Completed job | Cohort/segment, completed action, repeat event, period. |
| Channel fit | Source, role/segment, stage, outcome, period. |
| Delivery economics | Job type, delivery time, support category, direct cost band. |

Пожалуйста, не публикуйте private exports, customer messages, full records, credentials or browser sessions в GitHub Issues, examples или pull requests.
