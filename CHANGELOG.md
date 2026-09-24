# Changelog

Все заметные изменения документируются здесь.

## [0.5.0] — 2026-09-20 (cycle 4: services/edtech/ai-platforms)

### Added

- Третий конкурентный рыночный прогон: `examples/competition-services-2026-09-20/` — Profi.ru (услуги-маркетплейс, живые отзывы 19.09.2026), Skyeng (EdTech, outcome-claim без методики), Just AI (ИИ-платформа, рейтинги Markswebb 2023) + сводный отчёт.
- **Правило единственного независимого источника** в SKILL.md: 1 независимый locator → вердикт ≤ `switch_hypothesis_testable`, уверенность ограничена явно.
- Все 3 pack'а содержат секцию 10 (adversarial self-check) и поле «Уверенность вывода».

### Found (failure mode)

- Strict-валидатор отклонил все 3 новых pack'а по правилу «2+ независимых locator'а» — из открытого curl-доступа за один прогон доступен 1 независимый источник на объект. Зафиксировано как граница метода, не как дефект pack'ов.

## [0.4.0] — 2026-09-19 (adversarial cycle)

### Added

- **Strict evidence validator** (default mode): проверяет не только структуру, но и силу вывода — supported-claims требуют независимого evidence (medium/high), contradictory/disproven требуют 2 независимых наблюдения, future-dated источники отклоняются, transactional/object evidence старше 365 дней отклоняется, high confidence требует 4+ источников и 3+ независимых.
- **Adversarial self-check** (секция 10 отчёта, обязательна в strict): самое сильное альтернативное объяснение, что изменило бы вывод, что не наблюдали/не доказано.
- **Уверенность вывода** (low/medium/high) — вычисляется validator'ом из базы источников; high при малой базе отклоняется.
- `skill/scripts/test_adversarial.py` — 6 red-team сценариев: single_source, selfbacked_supported, inflated_verdict, future_date, overclaimed_confidence, missing_adversarial. Все 6 ловятся strict-режимом.
- `--legacy` режим для старых pack'ов (архивные examples проходят без adversarial-секций).

### Fixed

- validate_map возвращал только ошибки, из-за чего кросс-проверка вердикта/уверенности не выполнялась — исправлено.
- Owner operational data больше не считается независимым источником (только independent_behavior/independent_account с medium/high).
- Placeholder-детектор: незаполненные шаблонные поля в отчётах отклоняются.

### Verification

- `test_adversarial.py`: PASS 6/6.
- Legacy fixture + 8 реальных pack'ов: PASS.
- Strict fixture: PASS.

## [0.3.2] — 2026-09-18

### Added

- Второй цикл рыночного прогона: `examples/competition-freelance-2026-09-17/` — конкурентная evidence-диагностика 5 фриланс-бирж одного сегмента (Kwork, FL.ru, Weblancer, Kadrof, poisk-pro.ru) + сводный отчёт `examples/competition-freelance-2026-09-17.md` со сравнительной таблицей и ранжированием «кто выживет».
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
