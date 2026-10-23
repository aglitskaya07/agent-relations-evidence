# UNIT: @n8n/mcp-apps | npm v0.9.0 (published 2026-07-21T07:29:18.713Z) | рамки: npm-top | captured 2026-07-29 (static, tarball)

## NOT-A-SERVER

Пакет — вспомогательная библиотека («UI resources and server helpers for n8n»), а не самостоятельный MCP-сервер:

- Нигде в `dist/` нет конструирования сервера: grep по `new Server|new McpServer|createServer|instructions` — ноль совпадений. `@modelcontextprotocol/sdk` — только peerDependency.
- Экспорт `@n8n/mcp-apps/server` (`dist/server/index.js`) отдаёт хелперы, которые вызываются кодом `packages/cli` основного n8n поверх УЖЕ созданного сервера:
  - `registerMcpAppTool(server, name, config, handler)` — тонкая обёртка над `server.registerTool`, единственная логика — нормализация `_meta` (синхронизация `ui.resourceUri` и легаси-ключа `'ui/resourceUri'`). Ни имени инструмента, ни description она не задаёт — всё приходит извне.
  - `registerWorkflowPreviewApp(server, options)` — регистрирует ОДИН MCP-ресурс (не инструмент): `ui://workflow-preview/workflow-preview.html`, mime `text/html;profile=mcp-app`, description дословно: `'Workflow preview shown after creating a workflow from code'`. Отдаёт заранее собранный inline-HTML (Vue-приложение MCP Apps / ext-apps) с инъекцией telemetry-конфига (RudderStack CDN origin).
- README подтверждает: это UI-часть (MCP Apps по расширению `@modelcontextprotocol/ext-apps`) для рендера превью воркфлоу после инструмента `create_workflow_from_code`, живущего в основном n8n.

## CHANNEL: instructions, npm (static)
(не обнаружены статически — пакет не конструирует сервер, строки instructions нет нигде в dist)

## CHANNEL: tool descriptions, npm (static, coverage=none)
Инструментов пакет не определяет (0). Единственный текст, попадающий в MCP-поверхность, — description ресурса:

- resource `workflow-preview` (`ui://workflow-preview/workflow-preview.html`): "Workflow preview shown after creating a workflow from code"

Маркер-скан steering-регексов по всему dist — совпадений нет.

## NOTES
- Код не минифицирован (tsc-выхлоп с sourcemaps), читается полностью; исключение — `dist/apps/workflow-preview.html` (inline-собранный Vite/Vue бандл, минифицирован, но это UI-артефакт, а не серверные строки).
- Риск динамической сборки строк: низкий. Единственная динамика — `injectTelemetryConfig` вставляет `<script>window.<GLOBAL>=<json></script>` в HTML ресурса; описания/инструкции не собираются конкатенацией.
- Просмотрено: все 12 JS/JSON/MD файлов серверной части (package.json, README, dist/server/*.js, dist/apps-manifest.js, dist/telemetry-contract.js) + grep по всем ~30 файлам пакета.
