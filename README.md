# Market Evidence Diagnostic

> **Open-source skill для проверки claims бизнес-модели через рынок, альтернативы и доказательства из разных каналов.**

**Автор и maintainer:** [Виктор Зайцев](https://vospri9tielandingpage.vercel.app/) — продуктовый стратег и консультант, Санкт-Петербург.
**Статус:** `v0.3.0-rc1` — рабочий research skill, который проходит структурную проверку; не готовый «автономный market-research agent».

## Зачем это нужно

Компания легко может принять за доказательство рынка собственный сайт, красивый launch-пост, прайс, подписчиков или несколько разговоров. Это не доказывает, что люди регулярно сталкиваются с проблемой, платят за её решение или будут менять текущий способ работы.

`Market Evidence Diagnostic` собирает **research pack**, который отделяет:

| Что нужно проверить | Что skill ищет |
|---|---|
| Реальна ли работа/потеря | Следы того, как люди жалуются, ищут, обходят проблему или платят за workaround. |
| Чем её решают сейчас | DIY, incumbent, service alternative, direct competitor и status quo. |
| Почему кто-то переключится | Наблюдаемую разницу в цене, времени, риске, coverage или delivery. |
| Что доказал именно объект | Независимый review/case/usage signal или разрешённые owner data. |
| Чего ещё не хватает | Чёткий evidence gap: внешний источник или минимальные данные от владельца. |

Результат — **не совет “что делать дальше” и не прогноз выручки**. Это ограниченный verdict: что рынок уже позволяет утверждать, что объект доказал сам и какие claims пока преждевременны.

## Что внутри

```text
skill/                          # Устанавливаемый skill для AI-агента
├── SKILL.md                    # Workflow
├── templates/                  # Object card, channel inventory, ledger, verdict
├── references/                 # Источники, каналы и adapter contract
├── scripts/validate_diagnostic.py
└── fixtures/                   # Валидный и невалидный research pack
examples/fictional-static-export/ # Полностью вымышленный, безопасный пример
```

## Быстрый старт

1. Скопируйте `examples/fictional-static-export/` в новую рабочую папку.
2. Заполните `object-card.md`: **одна роль, одна ситуация, одна работа и текущая альтернатива**.
3. Заполните `channel-inventory.csv`. Нужен минимум один проверенный канал каждой стороны: object-side, buyer-side и alternative-side.
4. Найдите минимум три реальных alternatives и внесите их в `alternative-map.csv`.
5. В `external-evidence-ledger.csv` записывайте только наблюдения с источником, датой, классом, альтернативным объяснением и колонкой `what_it_does_not_prove`.
6. Заполните `business-model-hypothesis-map.csv` и `business-model-diagnostic.md`.
7. Запустите проверку:

```bash
python skill/scripts/validate_diagnostic.py path/to/your-pack
```

Если проверка не проходит, **не выдавайте market-readiness verdict**. Сначала закройте structural gap или явно зафиксируйте, что источник недоступен.

## Какие каналы учитываются

Skill не ограничивается сайтом компании. Он отдельно смотрит:

| Сторона | Примеры каналов | Что они могут показать |
|---|---|---|
| Object-side | Сайт, pricing, docs, GitHub, app store, Product Radar/Product Hunt, public social, партнёрские страницы | Offer, product scope, declared segment, release/partner signal. Обычно это self-claim. |
| Buyer-side | Reviews, communities, forums, public Telegram, marketplaces, job boards, procurement | Job language, alternatives, workarounds, switching friction и transaction proxies. |
| Alternative-side | Pricing/docs конкурентов, service marketplaces, category pages, integration directories | Current alternatives, commercial units, onboarding и switching constraints. |
| Owner-private | CRM, analytics, billing, support, attribution export | Payment, completed job, retention, channel conversion, delivery/economics — только с разрешением владельца. |

Подробнее: [guide по каналам](docs/evidence-and-channel-guide.md) и [adapter contract](docs/adapter-contract.md).

## Что этот проект **не** делает

- Не доказывает PMF, готовность к рынку, выручку или успех компании.
- Не превращает лайки, installs, stars, waitlist или pricing page в доказательство спроса.
- Не обходит login/paywall, не собирает личные контакты и не отправляет outreach.
- Не включает и не создаёт CRM/analytics/social connectors сам. Private adapters — только read-only и только по явному разрешению.
- Не является юридической, инвестиционной или финансовой консультацией.

## Для кого

Первый целевой пользователь — независимый product-консультант или малая продуктовая студия, которым нужно превращать клиентский brief в воспроизводимый research pack, не продавая «стратегию» на доверии.

Вторичные пользователи: B2B SaaS/AI founders после MVP, venture studios, акселераторы и product/innovation leads. Проект пока не доказал product-market fit в этих сегментах — именно для этого он ищет design partners.

## Текущий статус и участие

`v0.3.0-rc1` включает workflow, templates и validator. До `v1.0.0` нужны 3–5 независимых design-partner runs, review failure modes и проверка, что новый пользователь проходит Quickstart без сопровождения. Смотрите [ROADMAP.md](ROADMAP.md) и [guide для design partners](docs/design-partner-guide.md).

Вопросы, баги и улучшения — через [Issues](../../issues). Пожалуйста, сначала прочитайте [CONTRIBUTING.md](CONTRIBUTING.md), [SECURITY.md](SECURITY.md) и [Code of Conduct](CODE_OF_CONDUCT.md).

## Авторство и лицензия

Copyright 2026 Viktor Zaitsev. Проект распространяется по [Apache License 2.0](LICENSE). Она разрешает коммерческое переиспользование при сохранении условий лицензии и NOTICE; она **не** даёт право создавать впечатление, что Виктор Зайцев одобряет fork, сервис или производный продукт.

Этот проект разработан независимо. Он не связан, не одобрен и не основан на текстах, branding или proprietary структурах сторонних методологий. Подробности — в [методологических границах](docs/methodology-boundaries.md).
