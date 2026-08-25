# Матрица каналов для Business Model Evidence Diagnostic

## Правило чтения каналов

Канал — не источник «правды о компании». Он отвечает на один ограниченный вопрос: **какой claim можно проверить здесь и какую ложную интерпретацию нужно запретить.**

| Канал / место | Что можно наблюдать | Какие claims поддерживает | Что не доказывает | Режим доступа |
|---|---|---|---|---|
| Официальный сайт, pricing, docs | Offer, segmentation language, price unit, integration/delivery scope | Object claim; competitive positioning; commercial unit | Demand, usage, payment, retention, outcome | Public-web |
| Product Radar, Product Hunt, launch-posts | Launch timing, founder framing, early comments, search for partners/pilots | Early object signal; declared segment/route | PMF, revenue, real adoption | Public-web |
| App stores: RuStore, App Store, Google Play | Ratings, review text, install bands, update history, reply patterns | Consumer outcome/friction; weak usage/release signal | Retention, revenue, causal impact | Public-web |
| Reviews/comparison directories: G2, Capterra, Startpack, Trustpilot | User language, alternatives, complaints, switching reasons | Job reality; alternative friction; outcome claims | Representative market size, verified payment of every reviewer | Public-web |
| User communities: Habr, Reddit, Stack Overflow, forum, Telegram public channels | Workarounds, complaint language, migration stories, technical friction | Job reality; current alternatives; switching friction | Frequency, willingness-to-pay, average user profile | Public-web / public channel |
| GitHub, package registries, OSS docs | Releases, issues, stars/forks, installations if public, contributor activity | Developer adoption traces; technical friction; public roadmap | Commercial demand, revenue, enterprise retention | Public-web/API if public |
| Social/creator channels: LinkedIn, X, VC.ru, YouTube, podcasts, public Telegram | Messaging evolution, partner/client mentions, launches, public case claims | Communication hypotheses; public object/partner trace | Deal value, use/retention, representative demand | Public-web; read only |
| Partner/integration directories | Named integrations, certified agencies, marketplace listing, ecosystem placement | Route-to-market plausibility; partner claim | Active referral flow, deal volume, object outcome | Public-web |
| Job boards / freelance marketplaces / procurement | Service demand, skills sought, price bands, requested outcomes | Job reality; market transaction proxy; alternative cost/unit | Product-specific demand, close rate | Public-web |
| Media / customer case studies | Named deployment, context, claimed outcome | Independent object proof only when customer/third party is identifiable | Repeatability or economic viability | Public-web |
| Support/docs/status pages | Recurring failure modes, implementation burden, product change cadence | Delivery friction; resilience risk | User scale, satisfaction, revenue | Public-web or owner export |
| CRM / sales pipeline | Source, buyer role, objections, stage movement, lost reasons | Object demand, segment fit, channel conversion, price objections | Product outcome/retention after sale | Owner export / authorized connector |
| Product analytics | Activation, completed job, repeated use, cohort behavior | Useful outcome; retention; segment/context behavior | Willingness-to-pay, causality without design | Owner export / authorized connector |
| Billing / invoices / refunds | Payment, plan choice, revenue, refund timing | Value exchange; price acceptance; money | Product outcome; acquisition cost | Owner export / authorized connector |
| Support tickets / call transcripts | Failures, language of job, alternatives, pain after purchase | Job/reality; delivery friction; outcome failures | Market frequency without sampling | Owner export / authorized connector |
| Ad / search / attribution data | Query, source, landing response, cost, intent | Channel/access; competitor/search intent | Activated value, retention, unit economics alone | Owner export / authorized connector |

## Канал-claim coverage

| Claim | Приоритетные каналы | Нужна ли private data для сильного вывода |
|---|---|---|
| J — job reality | Reviews, communities, support, job boards, marketplaces | Нет для первичного signal; да для частоты/сегмента своего объекта. |
| A — alternatives | Search/category, pricing/docs, marketplaces, comparisons, user discussions | Нет для карты alternatives. |
| G — switching gap | Negative reviews, migration stories, community comparisons, support | Да, если нужно доказать, что именно объект закрыл gap. |
| T — transaction | Marketplace/price units, billing, CRM, procurement, paid pilots | Да для transaction объекта. |
| F — switching friction | Communities, docs, support, onboarding, migration guides | Нет для category friction; да для object funnel. |
| O — object proof | Third-party cases/reviews; analytics, invoices, support/retention | Почти всегда да для сильного object proof. |
| C — access | Search, partner directories, communities, CRM, attribution | Да для repeatable object channel. |
| M/R — economics/resilience | Public price/competitor delivery clues, but mainly billing, support, cohort/retention data | Да. External web alone is insufficient. |

## Мультиканальные правила

1. **Сначала ищи divergence:** если сайт обещает одно, а reviews/community/support говорят другое — фиксируй противоречие, не усредняй.
2. **Ищи buyer-side channel отдельно от object-side channel:** сайт компании показывает pitch; marketplace/reviews/community показывают job и alternatives.
3. **Не засчитывай активность как результат:** пост, launch, подписчики, stars, установку или partner badge нельзя автоматически переводить в payment, outcome или retention.
4. **Канал обязан иметь provenance:** URL/идентификатор, дату, mode доступа, source class, claim и caveat.
5. **Private adapter всегда optional:** отсутствие connector не блокирует public diagnosis; она лишь ограничивает object proof.
