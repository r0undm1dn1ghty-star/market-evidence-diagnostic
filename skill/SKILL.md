---
name: business-model-evidence-diagnostic
description: "Проводит мультиканальную внешнюю диагностику жизнеспособности бизнес-модели. Используй, когда нужно исследовать продукт через его сайт, публичные коммуникации, площадки покупателей, текущие альтернативы, прямых конкурентов, reviews/community/marketplace signals и — только с разрешением — CRM, аналитику, биллинг или support exports; затем определить, какие claims подтверждены рынком, а каких доказательств не хватает."
license: Apache-2.0
metadata:
  release: 0.3.0-rc1
  product: Business Model Evidence Diagnostic
---

# Мультиканальная внешняя диагностика бизнес-модели

> **Не оценивай сайт. Исследуй, как конкретная работа решается на рынке, что компания говорит в разных каналах, где покупатели уже действуют и чем объект выигрывает или проигрывает альтернативам.**

Используй skill для SaaS, сервисов, consumer-приложений, marketplace и open-source-продуктов перед запуском, новым сегментом, каналом, pricing change или ростом.

Не используй его как генератор общей стратегии, прогноз выручки, замену customer research или основание для скрытого сбора контактов/рассылки.

## Что выдаёт skill

1. **Object card:** роль, ситуация, работа, бизнес-модель и claim объекта.
2. **Channel inventory:** какие object-side и buyer-side каналы проверены, что каждый может подтвердить и где видны противоречия.
3. **Alternative map:** current workaround, doing nothing и 3–7 ближайших прямых конкурентов.
4. **External evidence ledger:** наблюдения с provenance, каналом, URL/датой, class источника и границей вывода.
5. **Comparative hypothesis map:** какие claims объекта подтверждены относительно альтернатив.
6. **Market-readiness verdict:** что можно утверждать о рынке/объекте и какие внешние или private evidence gaps остаются.

## Режимы доступа

| Режим | Когда использовать | Граница |
|---|---|---|
| `public_web` | Открытые сайты, app stores, reviews, communities, public social, docs, GitHub, marketplaces, partner directories. | Не обходи login/paywall; не делай profile enrichment; не пиши людям. |
| `user_file_export` | Владелец дал CSV/таблицу/анонимизированные transcripts. | Запроси минимально нужный файл; не собирай PII без необходимости. |
| `authorized_connector` | Пользователь явно подключил read-only источник и это нужно для конкретного gap. | Не включай/создавай connector сам, не используй write/action scopes. |

Подробные таблицы каналов — `references/channel-matrix.md`. Contract adapters — `references/adapter-contract.md`.

## Непреложный порядок работы

### 1. Зафиксируй объект исследования

Скопируй `templates/object-card.md`.

Определи одну исследовательскую единицу:

> **[Роль] в [ситуации] пытается [выполнить работу / избежать потери] и сейчас использует [альтернативу]. Объект предлагает [изменение результата, стоимости, риска или усилия].**

Если нельзя назвать role + situation + job, верни `market_research_required`. Не исследуй «компанию вообще».

### 2. Инвентаризируй каналы до выводов

Скопируй `templates/channel-inventory.csv`. Проверь минимум:

- **object-side:** website/pricing/docs и один доступный публичный communication channel — launch platform, app store, GitHub, social/community, partner directory, media or public case;
- **buyer-side:** хотя бы один канал, где люди обсуждают job/альтернативы или покупают их — reviews, forum, community, marketplace, job board, category directory;
- **alternative-side:** official pricing/docs и один independent/buyer-side signal, если доступен.

Каждый канал должен содержать: purpose, observed signal, supported claims, `does_not_prove`, access mode и provenance. Если канал недоступен, зафиксируй `not_available`; не подменяй его догадкой.

### 3. Построй карту alternatives и direct competitors

Скопируй `templates/alternative-map.csv`. Найди минимум:

- один current workaround / DIY / ручной сервис;
- один incumbent или существующий продукт;
- один ближайший direct competitor;
- при наличии — doing nothing / status quo.

Конкурент релевантен, только если совпадают минимум два признака: job/context, buyer role, тип обмена ценностью. Не называй «конкурентов нет», пока не исследованы categories, marketplaces, app stores, reviews и service alternatives.

### 4. Собери доказательства по распределённым каналам

Скопируй `templates/external-evidence-ledger.csv`. Для каждой записи укажи `channel`, URL/locator, дату, source class, claim, альтернативное объяснение и границу вывода.

Ищи не «упоминания бренда», а наблюдения по claims:

| Claim | Вопрос | Приоритетные каналы |
|---|---|---|
| J | Реальна ли работа/потеря? | Reviews, communities, support export, marketplaces, job boards. |
| A | Чем решают её сейчас? | Competitor docs/pricing, comparisons, marketplaces, communities. |
| G | Почему могут переключиться? | Negative reviews, migration stories, comparisons, support. |
| T | За что рынок отдаёт деньги/время? | Marketplace/procurement, pricing + reviews, billing/CRM export. |
| F | Что мешает switch? | Docs, discussions, migration guides, support, onboarding. |
| O | Что объект доказал именно относительно альтернатив? | Third-party case/review, app/GitHub trace, analytics/billing/support export. |

Self-claim объекта допускается только как `object_self_claim`. Он не может в одиночку создать `supported` claim.

### 5. Подключай private evidence только по конкретному gap

Сначала сформулируй, какого факта не хватает. Затем выбери минимальный adapter:

| Gap | Минимальный adapter | Что не выводить без него |
|---|---|---|
| Payment/price acceptance | Billing/CRM export | Willingness to pay объекта. |
| Completed job/repeat use | Analytics export + support sample | Object outcome/retention. |
| Buyer role/objections | CRM export or anonymized sales calls | Segment fit/price objection. |
| Repeatable channel | Attribution/CRM export | Channel fit/CAC. |
| Money/delivery/resilience | Billing + support + cohort/operations export | Unit economics/scale claim. |

File export предпочтительнее нового connector. Для реального connector сначала inspect availability; включение/создание требует отдельного явного согласия пользователя и read-only scope.

### 6. Построй сравнительную карту claims

Скопируй `templates/business-model-hypothesis-map.csv`. P/S/V/U/C/M/R — выход мультиканального сравнения, а не самооценка:

| Область | Проверяй через |
|---|---|
| P / S | Job и роль в buyer-side channels + alternatives. |
| V | Market transaction signal + object billing/CRM where authorized. |
| U | Gap against alternatives + third-party/analytics/support object evidence. |
| C | Где role уже ищет/покупает alternatives + object attribution. |
| M / R | External price/delivery clues + owner billing/support/cohorts. |

Статусы: `untested`, `weakly_supported`, `supported`, `contradictory`, `disproven`, `unknown`, `external_evidence_missing`.

### 7. Сформируй двухконтурный verdict

Скопируй `templates/business-model-diagnostic.md`.

| Контур | Допустимые статусы |
|---|---|
| Market reality | `market_unmapped`, `job_observed`, `alternatives_mapped`, `switch_reason_plausible`, `external_demand_observed` |
| Object proof | `self_claim_only`, `early_object_signal`, `independent_object_proof`, `private_evidence_required` |

| Verdict | Когда допустим |
|---|---|
| `market_research_required` | Job/current alternatives/buyer-side channel не определены. |
| `problem_and_alternatives_mapped` | Job и alternatives имеют external signals; object proof слаб. |
| `switch_hypothesis_testable` | Есть plausible gap/transaction structure; нужен object outcome/payment. |
| `limited_market_entry_supported` | Есть external demand, known alternatives и ограниченный object outcome. |
| `channel_or_economics_evidence_required` | Object value observed, но C/M ещё не доказаны. |
| `scale_evidence_required` | Market and object proof есть, но нет repeated/volume evidence. |
| `insufficient_evidence` | Нет object definition и минимального channel/research pack. |

Всегда разделяй **external evidence still collectable** и **private evidence required from owner**.

## Quality gate

Перед выдачей результата запусти:

```bash
python scripts/validate_diagnostic.py <папка_диагностики>
```

Проверка требует object card, channel inventory, минимум три alternatives, внешний ledger и comparative sections. Она не проверяет правдивость ссылок, спрос, PMF или успех бизнеса.

## Правила безопасности и независимости

- Не используй private data без разрешения, не обходи login/paywall и не делай скрытый contact enrichment.
- Не отправляй сообщения, не меняй CRM, не включай connector и не создавай API/MCP без явного согласия пользователя.
- Не превращай активность в результат: launch, likes, followers, stars, installs или partner badge не равны payment/outcome/retention.
- Не превращай price page конкурента в доказательство его usage или PMF.
- Не копируй язык, структуру, scoring или proprietary элементы внешних методологий.
