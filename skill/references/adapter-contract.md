# Adapter contract для мультиканальной диагностики

## Цель

Adapter не принимает решение за диагностический skill. Он переводит разрешённый источник в **нормализованные наблюдения** с provenance, чтобы skill мог связать их с J/A/G/T/F/O и P/S/V/U/C/M/R.

## Общий выход адаптера

Каждый adapter должен вернуть записи в следующей форме:

| Поле | Значение |
|---|---|
| `adapter_id` | Идентификатор типа источника, например `public_app_store`, `crm_export`, `analytics_export`. |
| `access_mode` | `public_web`, `user_file_export`, `authorized_connector`. |
| `channel` | App store, community, CRM, analytics, billing, support, social, partner directory и т.д. |
| `observed_at` | Дата/период наблюдения. |
| `source_locator` | URL, file hash/name+sheet, query/report ID; без секретов. |
| `subject` | Object, alternative или segment/community. |
| `observation` | Факт или короткая цитата без интерпретации. |
| `claim_codes` | Один или несколько: J/A/G/T/F/O/C/M/R. |
| `source_class` | `independent_behavior`, `independent_account`, `competitor_docs`, `object_self_claim`, `owner_operational_data`. |
| `privacy_class` | `public`, `owner_authorized_aggregate`, `owner_authorized_sensitive`. |
| `alternative_explanation` | Почему факт может означать не то, что кажется. |
| `does_not_prove` | Запрещённый вывод. |

## Adapter families

| Adapter | Вход | Что выдаёт | Claims | Минимальный безопасный scope |
|---|---|---|---|---|
| `public_web_scan` | Object/competitor URLs and public queries | Docs, pricing, marketplace/review/community observations | J/A/G/T/F/O | Публичные страницы, без обхода login/paywall. |
| `app_store_scan` | App IDs/URLs | Rating/review text, version history, install bands where public | J/U/F/O | Публичная карточка; рейтинг отдельно от behaviour. |
| `public_community_scan` | Public forum/subreddit/Habr/X/Telegram channel URLs/queries | Complaints, workarounds, comparisons, public asks | J/A/G/F | Только публичные посты; не profile enrichment, не DM. |
| `github_oss_scan` | Public repo/package URL | Issues, release cadence, contributors, integrations, public adoption signals | A/F/O/R | GitHub API/public repo; stars not treated as transaction. |
| `review_directory_scan` | Product/category URLs | User language, alternative mentions, outcome/failure stories | J/A/G/U/F/O | Public reviews; mark review-site incentives and sampling limits. |
| `marketplace_scan` | Service/job/category URL | Price unit, provider count, visible reviews, request language | J/A/T/F | Public category data; not closed deal volume. |
| `crm_export` | User-provided CSV or explicit read-only connector | Role, source, stage, objection, lost reason, timestamps | S/V/C/T | Aggregated/de-identified fields by default; no contact enrichment. |
| `analytics_export` | User-provided CSV or explicit read-only connector | Activation, completed job, repeat use, cohorts, events | U/R/S/C | Aggregated event/cohort data; no raw PII. |
| `billing_export` | User-provided CSV or explicit read-only connector | Payment, plan, refund, renewal, payment date | V/M/R | Aggregated invoices/transactions; no full payment details. |
| `support_export` | User-provided anonymized tickets/transcripts | Failure, language of job, alternatives, outcome issue | J/U/F/R | Redact PII; sample/aggregate when possible. |
| `attribution_export` | User-provided CSV or explicit read-only connector | Channel → visit/conversation/activation/cost | C/M/S | Aggregate by source/segment/period. |

## Connector policy

1. **Public adapters first.** A missing connector cannot stop basic market mapping.
2. **Private adapters are opt-in.** Request the smallest data export that answers one defined evidence gap; file upload is preferred before persistent connector setup.
3. **Connector setup is separate from diagnosis.** Inspect availability first; enable/create only after the user explicitly chooses provider and confirms read-only need.
4. **No action permissions.** CRM/social/support adapters are read-only: no send, update, create, delete, assign, follow or export contacts beyond the minimum scope.
5. **No secret in skill artifacts.** Store only provider name, adapter status and non-sensitive report ID; never put keys/tokens in output.

## Adapter selection logic

| Evidence gap | First adapter | If insufficient | Do not infer from |
|---|---|---|---|
| Is the job real? | Public communities/reviews/marketplace | Anonymized support/interview export | Object landing page |
| Who is the segment? | Alternatives/reviews/community language | CRM + analytics segment export | Follower demographic |
| Why switch / what friction? | Negative reviews, migration docs, comparisons | Support tickets and lost-deal reasons | Feature comparison only |
| Will they pay? | Marketplace/competitor price unit | Billing + CRM paid pilot records | Price page, signup, waitlist |
| Does object work? | Third-party case/review | Analytics completed job + support + user evidence | Demo, screenshots, internal QA alone |
| Can channel repeat? | Public discovery routes/partners | CRM attribution export | One launch post/referral |
| Is model economical/resilient? | External price/implementation clues | Billing, support, attribution, cohorts | Public website or market size |

## Current implementation boundary

The skill describes these adapters and accepts their files/outputs. It does **not** call third-party APIs autonomously, enable connectors by itself, or store credentials. Any real provider integration must be implemented and activated separately with user confirmation.
