# MCP-интеграция Market Evidence Diagnostic

> Локальный MCP-сервер для проверки research pack. Чистый Python (stdlib), работает без облака и без зависимостей.

## Установка

```bash
# Зависимостей нет — только Python 3.9+
python mcp_server.py
```

## Инструменты

| Инструмент | Описание |
|---|---|
| `validate_pack` | Прогоняет структурный валидатор по папке research pack. Вердикт только после PASS |
| `list_templates` | Список шаблонов, которые нужно заполнить |

## Конфигурация (Claude Desktop / Claude Code / любой MCP-клиент)

Добавьте в MCP-конфиг:

```json
{
  "mcpServers": {
    "market-evidence": {
      "command": "python",
      "args": ["путь/до/integrations/mcp/mcp_server.py"]
    }
  }
}
```

## Проверка вручную (без MCP-клиента)

```bash
echo '{"jsonrpc":"2.0","id":1,"method":"initialize","params":{}}' | python mcp_server.py
```

## Стоп-правила

Сервер проверяет структуру, но **не** доказывает спрос, PMF или коммерческий успех. Лайки, installs, stars и waitlist — не доказательство. Полный набор — в `skill/SKILL.md`.
