# Custom GPT для Market Evidence Diagnostic

## Настройка

1. Откройте ChatGPT → Explore GPTs → Create.
2. Вставьте системный промпт из `prompts/core_strategist.md`.
3. Загрузите файлы: `skill/templates/` (все 6 шаблонов).
4. Сохраните и протестируйте.

## Системный промпт (кратко)

> Ты — Market Evidence Diagnostic. Проверяешь утверждения бизнес-модели через рынок, альтернативы и доказательства из каналов. Следуй процедуре: object card → channel inventory → alternative map → evidence ledger → hypothesis map → diagnostic. Не выдавай market-readiness verdict, пока структура не полная. Каждый вывод — источник + дата.

## Ограничения

- Custom GPT не заменяет инвестиционную/финансовую консультацию.
- Не передавайте конфиденциальные данные в облако без необходимости.
- Для чувствительных данных используйте локальный MCP-сервер.
