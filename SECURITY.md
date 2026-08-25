# Security and privacy

## Supported scope

`Market Evidence Diagnostic` is a documentation/template/validator project. It does not run a hosted service, store credentials or ship provider integrations in `v0.3.0-rc1`.

## Reporting a vulnerability

Не публикуйте security issue, leaked token, private export или personal data в public GitHub issue. Вместо этого напишите maintainer’у через [сайт «восприятие»](https://vospri9tielandingpage.vercel.app/) с темой `Market Evidence Diagnostic security` и минимальным описанием проблемы.

Пожалуйста, включите affected file/version, безопасный reproduction path и возможный impact. Не прикладывайте настоящие credentials, customer records, sessions/cookies или данные третьих лиц.

## Data handling rules

| Категория | Правило |
|---|---|
| Public-web sources | Сохраняйте URL, дату, source class и минимальную цитату; соблюдайте ограничения доступа площадки. |
| Private exports | Принимайте только с разрешения владельца и только минимальный набор полей для одного evidence gap. |
| PII | Не нужен по умолчанию. Redact before use; не публикуйте в repo, issue, fixture, example или PR. |
| Credentials | Никогда не сохраняйте в repository, output, screenshots или templates. |
| Connectors | Только explicit user-authorized, read-only, minimal scope; no send/create/update/delete actions. |
| Real-company packs | Не публикуйте без явного письменного разрешения владельца и проверки third-party data. |

## Research safety

The validator checks artifact structure only. It cannot validate a source, its permission status, causal claim, commercial result or legal basis of data processing. Maintainers and contributors must preserve provenance and state `what_it_does_not_prove` for every observation.
