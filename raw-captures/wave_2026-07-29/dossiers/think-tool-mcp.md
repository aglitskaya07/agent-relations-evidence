# UNIT: think-tool-mcp | npm v1.0.2 (published 2025-08-12T08:13:38.861Z) | рамки: pulsemcp | captured 2026-07-29 (static, tarball)

## VERDICT: MCP-сервер

Да, это MCP-сервер: `src/server.ts` / `dist/server.js` создают `McpServer` из `@modelcontextprotocol/sdk/server/mcp.js`, регистрируют один инструмент через `this.mcp.tool(...)` и подключают `StdioServerTransport`. Точка входа `dist/index.js` (bin) запускает `ThinkToolServer().run()`.

## CHANNEL: instructions, npm (static)
(не обнаружены статически)

Конструктору `McpServer` передаются только `{ name: serverName, version: "0.1.0" }` — поля `instructions` нет нигде в пакете (grep по всем .ts/.js/.json — ноль совпадений вне source maps).

## CHANNEL: tool descriptions, npm (static, coverage=full)

Всего инструментов: 1.

### 1. `think`
```
Use this tool to think about something. It will not obtain new information or change anything. Use it when complex reasoning is needed.

      Args:
      thought: A thought to think about. This can be structured reasoning, step-by-step analysis, policy verification, or any other mental process that helps with problem-solving.
```
Параметры: `{ thought: z.string() }`. Обработчик возвращает эхо мысли, усечённое до 50 символов.

Маркеры стеринга: совпадений по маркер-регексам нет. Описание нейтральное, без давления на приоритет над другими инструментами.

## NOTES
- Код не минифицирован: dist — обычный tsc-выхлоп с комментариями и source maps, 1:1 с src.
- Риск динамической сборки строк: нулевой — все строки (имя, описание) — статические литералы; `serverName` параметризуем, но дефолт "think-tool" и bin его не переопределяет.
- Просмотрено файлов: src/server.ts, src/index.ts, dist/server.js, dist/index.js (через листинг), package.json/README косвенно через grep; всего в пакете 20 файлов.
