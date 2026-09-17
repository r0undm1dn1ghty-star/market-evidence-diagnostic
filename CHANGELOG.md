# Changelog

Все заметные изменения документируются здесь.

## [0.3.2] — 2026-09-18

### Added

- Второй цикл баттлтеста: `examples/competition-freelance-2026-09-17/` — конкурентная evidence-диагностика 5 фриланс-бирж одного сегмента (Kwork, FL.ru, Weblancer, Kadrof, poisk-pro.ru) + сводный отчёт `examples/competition-freelance-2026-09-17.md` со сравнительной таблицей и ранжированием «кто выживет».
- Все 5 pack'ов проходят `validate_diagnostic.py` (PASS × 5).

### Fixed

- Валидатор во втором цикле отклонял pack'и без кода F (friction) в `external-evidence-ledger.csv` — зафиксировано, что код F обязателен в каждом ledger (ошибка первого цикла, где F отсутствовал в части pack'ов).

## [0.3.0-rc1] — 2026-08-17

Первый публичный release candidate самостоятельного GitHub-проекта.

### Added

- Мультиканальный workflow: object-side, buyer-side, alternative-side и optional owner-private data.
- `channel-inventory.csv` и обязательная связь evidence с каналом, режимом доступа и стороной рынка.
- Alternative map с минимум тремя ближайшими способами решения работы.
- External evidence ledger с provenance, source class, alternative explanation и `what_it_does_not_prove`.
- Comparative hypothesis map по проблеме, сегменту, value exchange, outcome, customer access, money/delivery и resilience.
- Два verdict-контура: `market reality` и `object proof`.
- Structural validator и valid/invalid fixtures.
- Public documentation, privacy/security boundaries, contribution rules и Apache-2.0 licensing.

### Not included

- Hosted service, API, OAuth, CRM/analytics/billing/social integrations, scheduled sync или connector setup.
- Automatic outreach, lead generation, contact enrichment, PMF/revenue guarantee or autonomous market-research claims.
- Real-company research packs or private owner data.

### Upgrade criteria for 1.0.0

- 3–5 reviewed design-partner runs.
- At least two documented failure modes leading to template/validator improvements.
- External user completes Quickstart without maintainer assistance.
- Reconfirmed public claims, license/NOTICE and security/privacy policy.
