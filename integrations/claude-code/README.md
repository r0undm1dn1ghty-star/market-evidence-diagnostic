# Интеграция с Claude Code

## Установка

1. Скопируйте папку `skill/` в проект:
   ```bash
   cp -r skill/ ваш_проект/skills/market-evidence/
   ```
2. Добавьте в `CLAUDE.md` проекта:
   ```markdown
   ## Market Evidence Diagnostic
   При запросах о проверке рынка/бизнес-модели используй скилл из `skills/market-evidence/SKILL.md`.
   Не выдавай market-readiness verdict, пока валидатор не пройден.
   ```
3. Запустите Claude Code в папке проекта.

## Использование

```bash
# Запустить диагностику
claude "Запусти Market Evidence Diagnostic. Объект — наша новая B2B-услуга, бриф в brief.md"
```

## Что делает агент

1. Читает `skill/SKILL.md` — процедуру сбора research pack.
2. Заполняет шаблоны: object card, channel inventory, alternative map, evidence ledger.
3. Запускает проверку: `python skill/scripts/validate_diagnostic.py <pack>`
4. Если проверка не прошла — фиксирует пробелы, а не выдаёт вердикт.

## Стоп-правила

- Лайки, installs, stars, waitlist и pricing page — НЕ доказательство спроса.
- Не обходи login/paywall, не собирай личные контакты.
- Private-данные — только read-only и с разрешения владельца.
- Полный список — в `skill/SKILL.md` и `docs/methodology-boundaries.md`.
