# Интеграция с Hermes Agent (и другими агентными CLI)

## Установка

1. Скопируйте папку `skill/` в свою библиотеку скиллов:
   ```bash
   cp -r skill/ ~/skills/market-evidence/
   ```
2. Hermes (и большинство агентных рантаймов) читает `SKILL.md` как инструкцию. Если рантайм использует YAML-frontmatter — он уже есть в `skill/SKILL.md`.

## Использование

```bash
hermes -z "Запусти Market Evidence Diagnostic. Объект — наш сервис, бриф в brief.md. Собери research pack и прогони валидатор."
```

## Что делает агент

1. Читает `skill/SKILL.md` — 7-шаговую процедуру.
2. Заполняет шаблоны из `skill/templates/`: object card, channel inventory, alternative map, evidence ledger, hypothesis map.
3. Прогоняет `python skill/scripts/validate_diagnostic.py <pack>`.
4. Вердикт выдаёт только после прохождения проверки; иначе — список пробелов.

## Стоп-правила

- Не выдаёт утверждения за доказательства: внешний источник + дата обязательны.
- Не обходит paywall/login, не собирает контакты.
- Не даёт инвестиционных/финансовых рекомендаций.
- Полный список — в `skill/SKILL.md`.

## Примечание

Любой агентный рантайм, умеющий читать Markdown-инструкции (Claude Code, OpenCode, Cursor, etc.), подключается тем же способом: скопировать `skill/` и сослаться на `SKILL.md`.
