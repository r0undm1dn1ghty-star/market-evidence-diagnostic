#!/usr/bin/env python3
"""MCP-сервер Market Evidence Diagnostic — локальная проверка research pack.

Чистый Python (stdlib), JSON-RPC 2.0 по stdio (протокол Model Context Protocol).
Запуск: python mcp_server.py   (подключение через MCP-клиент, см. README.md)

Инструменты:
  validate_pack  — прогон структурного валидатора по папке research pack
  list_templates — список шаблонов, которые нужно заполнить
"""
import json
import os
import subprocess
import sys

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
VALIDATOR = os.path.join(REPO_ROOT, "skill", "scripts", "validate_diagnostic.py")
TEMPLATES_DIR = os.path.join(REPO_ROOT, "skill", "templates")

TEMPLATES = [
    "object-card.md",
    "channel-inventory.csv",
    "alternative-map.csv",
    "external-evidence-ledger.csv",
    "business-model-hypothesis-map.csv",
    "business-model-diagnostic.md",
]


def validate_pack(pack_path: str) -> dict:
    """Прогоняет валидатор по папке research pack."""
    if not os.path.isdir(pack_path):
        return {"ok": False, "error": f"Папка не найдена: {pack_path}"}
    if not os.path.exists(VALIDATOR):
        return {"ok": False, "error": f"Валидатор не найден: {VALIDATOR}"}
    try:
        proc = subprocess.run(
            [sys.executable, VALIDATOR, pack_path],
            capture_output=True, text=True, timeout=60,
        )
        return {
            "ok": proc.returncode == 0,
            "exit_code": proc.returncode,
            "output": proc.stdout.strip() + proc.stderr.strip(),
        }
    except subprocess.TimeoutExpired:
        return {"ok": False, "error": "Валидатор не завершился за 60 секунд"}
    except Exception as exc:
        return {"ok": False, "error": str(exc)}


def list_templates() -> dict:
    """Список шаблонов для заполнения."""
    present = [t for t in TEMPLATES if os.path.exists(os.path.join(TEMPLATES_DIR, t))]
    return {"templates": present, "count": len(present), "templates_dir": TEMPLATES_DIR}


TOOLS = [
    {
        "name": "validate_pack",
        "description": "Прогоняет структурный валидатор по папке research pack. Вердикт только после PASS.",
        "inputSchema": {
            "type": "object",
            "properties": {"pack_path": {"type": "string", "description": "Абсолютный путь к папке research pack"}},
            "required": ["pack_path"],
        },
    },
    {
        "name": "list_templates",
        "description": "Список шаблонов, которые нужно заполнить для research pack.",
        "inputSchema": {"type": "object", "properties": {}},
    },
]


def _read_request() -> dict | None:
    line = sys.stdin.readline()
    if not line:
        return None
    try:
        return json.loads(line)
    except json.JSONDecodeError:
        return None


def _respond(req: dict, result: dict | None = None, error: dict | None = None) -> None:
    resp = {"jsonrpc": "2.0", "id": req.get("id")}
    if error is not None:
        resp["error"] = error
    else:
        resp["result"] = result
    sys.stdout.write(json.dumps(resp, ensure_ascii=False) + "\n")
    sys.stdout.flush()


def main() -> None:
    while True:
        req = _read_request()
        if req is None:
            break
        method = req.get("method", "")

        if method == "initialize":
            _respond(req, {
                "protocolVersion": "2024-11-05",
                "capabilities": {"tools": {}},
                "serverInfo": {"name": "market-evidence-diagnostic", "version": "0.3.0-rc1"},
            })
        elif method == "tools/list":
            _respond(req, {"tools": TOOLS})
        elif method == "tools/call":
            name = req.get("params", {}).get("name", "")
            args = req.get("params", {}).get("arguments", {})
            try:
                if name == "validate_pack":
                    result = validate_pack(args.get("pack_path", ""))
                elif name == "list_templates":
                    result = list_templates()
                else:
                    _respond(req, error={"code": -32601, "message": f"Неизвестный инструмент: {name}"})
                    continue
                _respond(req, {"content": [{"type": "text", "text": json.dumps(result, ensure_ascii=False, indent=2)}]})
            except Exception as exc:
                _respond(req, error={"code": -32603, "message": str(exc)})
        elif method == "ping":
            _respond(req, {})
        else:
            _respond(req, error={"code": -32601, "message": f"Метод не поддерживается: {method}"})


if __name__ == "__main__":
    main()
