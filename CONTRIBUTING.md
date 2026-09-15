# Contributing to Market Evidence Diagnostic

Спасибо за вклад. Цель проекта — сделать research packs более честными и воспроизводимыми, а не увеличить количество уверенных, но неподтверждённых выводов.

## Что можно предложить

Подходящие contributions включают новые templates, validator checks, de-identified fictional examples, public-source adapters, documentation improvements и bug reports.

Перед pull request откройте issue, если меняете workflow, claim taxonomy, verdict rules или public positioning.

## Обязательные правила

| Правило | Требование |
|---|---|
| Source provenance | Укажите URL/locator, date, source class, alternative explanation и `does_not_prove`. |
| Claims | Не переводите self-claim, price page, follower count, launch, star, install или waitlist в proof of demand/outcome. Не выдавайте утверждения за доказательства. |
| Real companies | Не добавляйте research pack третьей компании без её явного разрешения или без полной деперсонализации/fictionalisation. |
| Personal data | Не добавляйте контакты, emails, CRM records, transcripts, screenshots с PII, credentials, tokens или cookie/session data. |
| License hygiene | Вносите только собственный код/текст либо материал, который разрешён для Apache-2.0 redistribution с сохранением notices. |
| Integrations | Не добавляйте write actions; каждый provider adapter должен быть read-only, минимальным и документировать scope. |
| Tests | Изменение templates или validator должно обновлять fixture и проходить `python skill/scripts/validate_diagnostic.py skill/fixtures/valid-diagnostic`. |

## Pull request checklist

- [ ] Я написал, какое evidence gap решает изменение.
- [ ] Я обновил template/reference/fixture там, где это необходимо.
- [ ] Я не добавил private data, контакты, credentials или непроверенные рыночные утверждения.
- [ ] Я проверил license/source attribution для внесённых материалов.
- [ ] Я запустил quality gate и приложил результат в PR description.
- [ ] Я согласен, что contribution лицензируется под Apache-2.0.

## Чего проект не примет

Не будут приняты: lead lists, outreach automation, scraping behind login/paywall, скрытый profile enrichment, утверждения о PMF/гарантии выручки, вложенные proprietary frameworks, а также PR с real customer data без документированного разрешения.
