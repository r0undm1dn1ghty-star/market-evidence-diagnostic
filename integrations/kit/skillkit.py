#!/usr/bin/env python3
"""skillkit — лёгкий HTTP-мост для интеграции скилла в ЛЮБЫЕ агентные системы и чат-боты.

Зачем: у каждого агента/бота свой стек. Вместо «ставь наш SDK» этот файл поднимает
локальный HTTP-сервис на чистой стандартной библиотеке Python 3.8+ — и всё, что умеет
делать HTTP-запрос (Telegram-бот, n8n, Make, Zapier, Bitrix24, любой LangChain/LlamaIndex
агент, GPT Actions, MCP-клиент), может пользоваться скиллом без единой зависимости.

Возможности
-----------
1. HTTP API:      POST /run  {"input": "...", ...}   -> результат скилла
                  GET  /openapi.json                 -> OpenAPI 3.1 (GPT Actions / Swagger)
                  GET  /health                       -> статус
2. CLI-режим:     python skillkit.py --input "..."     (pipe-friendly)
3. Адаптеры:      prompt() -> системный промпт для LLM, openapi() -> схема для GPT Actions
4. Ноль зависимостей: только stdlib. Не требует сети для собственной работы.

Подключение к скиллу: реализация в inject-файле `skill_impl.py` рядом (функция run(input, **kw)).
"""
from __future__ import annotations

import argparse
import json
import os
import sys
import threading
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)

VERSION = "1.0.0"


def _impl():
    """Загружает реализацию скилла (skill_impl.run)."""
    import importlib
    mod = importlib.import_module("skill_impl")
    importlib.reload(mod)
    return mod


def run(input_value=None, **kw):
    """Единая точка входа: вход (текст/dict) -> структурированный результат."""
    return _impl().run(input_value, **kw)


def prompt() -> str:
    """Системный промпт для LLM-агентов без доступа к файлам репозитория."""
    return _impl().SYSTEM_PROMPT


def openapi() -> dict:
    """OpenAPI 3.1 описание — для GPT Actions, Swagger UI, генерации клиентов."""
    m = _impl()
    return {
        "openapi": "3.1.0",
        "info": {"title": m.SKILL_NAME, "version": m.SKILL_VERSION,
                 "description": m.SKILL_DESCRIPTION},
        "servers": [{"url": "http://localhost:8765"}],
        "paths": {
            "/run": {
                "post": {
                    "operationId": "run_skill",
                    "summary": m.SKILL_DESCRIPTION,
                    "requestBody": {"required": True, "content": {"application/json": {
                        "schema": m.INPUT_SCHEMA}}},
                    "responses": {"200": {"description": "Результат", "content": {
                        "application/json": {"schema": m.OUTPUT_SCHEMA}}}},
                }
            },
            "/health": {"get": {"operationId": "health", "summary": "Статус сервиса",
                                "responses": {"200": {"description": "ok"}}}},
        },
    }


class _Handler(BaseHTTPRequestHandler):
    server_version = "skillkit/" + VERSION

    def _send(self, code, payload, ctype="application/json"):
        body = payload if isinstance(payload, bytes) else json.dumps(
            payload, ensure_ascii=False).encode("utf-8")
        self.send_response(code)
        self.send_header("Content-Type", ctype + "; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.end_headers()
        self.wfile.write(body)

    def do_OPTIONS(self):
        self._send(204, b"", "text/plain")

    def do_GET(self):
        path = self.path.split("?")[0].rstrip("/") or "/"
        if path == "/health":
            m = _impl()
            self._send(200, {"status": "ok", "skill": m.SKILL_NAME,
                             "version": m.SKILL_VERSION, "kit": VERSION})
        elif path == "/openapi.json":
            self._send(200, openapi())
        elif path in ("/", "/prompt"):
            m = _impl()
            self._send(200, {"skill": m.SKILL_NAME, "version": m.SKILL_VERSION,
                             "prompt": prompt(), "endpoints": ["POST /run", "GET /openapi.json",
                                                               "GET /health", "GET /prompt"]})
        else:
            self._send(404, {"error": "not found", "hint": "POST /run | GET /openapi.json"})

    def do_POST(self):
        if self.path.split("?")[0].rstrip("/") != "/run":
            self._send(404, {"error": "not found"})
            return
        try:
            n = int(self.headers.get("Content-Length") or 0)
            raw = self.rfile.read(n).decode("utf-8") if n else "{}"
            payload = json.loads(raw) if raw.strip() else {}
        except Exception as e:
            self._send(400, {"error": f"bad json: {e}"})
            return
        try:
            value = payload.pop("input", payload.pop("text", payload)) if isinstance(payload, dict) else payload
            self._send(200, {"ok": True, "result": run(value, **payload) if isinstance(payload, dict) else run(value)})
        except Exception as e:
            self._send(200, {"ok": False, "error": str(e)})

    def log_message(self, *a):
        if os.environ.get("SKILLKIT_VERBOSE"):
            sys.stderr.write(" ".join(str(x) for x in a) + "\n")


def serve(host="127.0.0.1", port=8765):
    ThreadingHTTPServer((host, port), _Handler).serve_forever()


def main(argv=None):
    ap = argparse.ArgumentParser(description="skillkit — HTTP/CLI мост для агентов и чат-ботов")
    ap.add_argument("--input", "-i", default=None, help="вход (строка или JSON)")
    ap.add_argument("--json", action="store_true", help="вывод JSON")
    ap.add_argument("--serve", action="store_true", help="поднять HTTP-сервис")
    ap.add_argument("--port", type=int, default=8765)
    ap.add_argument("--host", default="127.0.0.1")
    ap.add_argument("--prompt", action="store_true", help="напечатать системный промпт")
    ap.add_argument("--openapi", action="store_true", help="напечатать OpenAPI 3.1")
    a = ap.parse_args(argv)
    if a.prompt:
        print(prompt()); return 0
    if a.openapi:
        print(json.dumps(openapi(), ensure_ascii=False, indent=2)); return 0
    if a.serve:
        m = _impl()
        print(f"{m.SKILL_NAME} v{m.SKILL_VERSION} (skillkit {VERSION})")
        print(f"  POST http://{a.host}:{a.port}/run")
        print(f"  GET  http://{a.host}:{a.port}/openapi.json")
        serve(a.host, a.port); return 0
    raw = a.input if a.input is not None else sys.stdin.read()
    inp = raw
    if a.input is not None:
        try:
            inp = json.loads(raw)
        except Exception:
            inp = raw
    out = run(inp)
    print(json.dumps(out, ensure_ascii=False, indent=2) if a.json else json.dumps(out, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
