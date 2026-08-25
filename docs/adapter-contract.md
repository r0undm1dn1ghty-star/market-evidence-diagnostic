# Adapter contract

Adapters превращают разрешённый источник в запись evidence ledger. Они **не** принимают бизнес-решение, не должны менять внешние системы и не являются готовыми integrations в `v0.3.0-rc1`.

## Режимы доступа

| Режим | Что можно использовать | Ограничение |
|---|---|---|
| `public_web` | Открытые сайты, docs, reviews, public communities, public social, app stores, marketplaces, public GitHub | Не обходить login/paywall, не делать private profile enrichment, не отправлять сообщения. |
| `user_file_export` | CSV/таблица/анонимизированный transcript, который предоставил владелец | Запрашивать минимальный dataset под один evidence gap. |
| `authorized_connector` | Read-only provider connection, явно выбранная и подтверждённая владельцем | Не включать и не создавать автоматически; no write/action scope. |

## Унифицированная запись adapter output

Каждое наблюдение должно содержать:

```text
adapter_id
access_mode
channel
observed_at
source_locator
subject
observation
claim_codes
source_class
privacy_class
alternative_explanation
does_not_prove
```

Ни ключей, ни токенов, ни полного PII в этой записи быть не должно.

## Поддерживаемые типы входов

| Adapter family | Вход | Что может поддержать |
|---|---|---|
| Public web / reviews / community / marketplace | URL или public query | Job, alternatives, switching friction, category transaction proxies. |
| App store | Public app URL/ID | Review language, public release trace, visible install/rating signal. |
| GitHub / OSS | Public repository/package URL | Issues, release cadence, public ecosystem trace. |
| CRM export | Authorized file/connector | Buyer role, source, stage, objections, lost reasons. |
| Analytics export | Authorized file/connector | Activation, completed job, repeat use, cohorts. |
| Billing export | Authorized file/connector | Payment, plan, refund, renewal. |
| Support export | Authorized file/connector | Failure, job language, alternative, delivery friction. |
| Attribution export | Authorized file/connector | Source-to-conversation/activation/cost evidence. |

## Что реализовано сейчас

`v0.3.0-rc1` описывает schema и безопасный workflow. Он **не содержит** OAuth, API clients, provider-specific connectors, secret storage, scheduled sync или write actions. Начинайте с public-web research или file export. Нужна интеграция — сначала откройте issue с provider, read-only use case, exact evidence gap и минимальным scope.
