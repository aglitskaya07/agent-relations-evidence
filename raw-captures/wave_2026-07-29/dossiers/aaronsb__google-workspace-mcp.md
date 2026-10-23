# UNIT: @aaronsb/google-workspace-mcp | npm v4.0.1 (published 2026-07-12T21:51:22.133Z) | рамки: pulsemcp | captured 2026-07-29 (static, tarball)

## VERDICT: MCP-сервер

Да, это MCP-сервер. `build/server/server.js` создаёт `new Server({name: '@aaronsb/google-workspace-mcp', version: VERSION}, {capabilities: {tools: {}, resources: {}}})` из `@modelcontextprotocol/sdk/server/index.js`, подключает `StdioServerTransport`, регистрирует хендлеры ListTools/CallTool/ListResources/ReadResource. Точка входа — `bin: google-workspace-mcp -> ./build/index.js`.

## CHANNEL: instructions, npm (static)
(не обнаружены статически)

Конструктору `Server` передаются только `name`/`version` и capabilities — поля `instructions` нет нигде в `build/` (grep по "instructions" дал только несвязанные упоминания). Канал server-instructions не используется.

## CHANNEL: tool descriptions, npm (static, coverage=full)

Всего инструментов: 11 (4 hand-coded в `build/server/tools.js` + 7 factory-generated из YAML-манифестов `build/factory/manifest/*.yaml`; top-level `description` каждого YAML становится description инструмента без модификаций — проверено по `generateSchema` в `build/factory/generator.js`).

1. **manage_accounts** — "Manage Google Workspace account lifecycle: list, authenticate, check status, refresh credentials, update scopes, or remove accounts."
2. **manage_workspace** — "Manage files and directories in the workspace sandbox. Supports nested paths (e.g. \"reports/q1/summary.csv\"). The workspace is the exchange point for file operations (attachments, downloads, exports)."
3. **manage_scratchpad** — "Compose, edit, and deliver text content. Use for any multi-line content: emails, documents, descriptions. Compose in the scratchpad, edit by line or JSON path, attach files, then send to any target. For short one-liners, use the service tool directly instead."
4. **queue_operations** — "Execute multiple operations in sequence. Operations run in order with result references ($0.field) to chain outputs. Use for multi-step workflows."
5. **manage_calendar** — "List events, view agenda, check availability, or manage calendar events." (9 операций)
6. **manage_docs** — "Read, write, insert, and find-replace text in Google Docs documents." (5 операций)
7. **manage_drive** — "Search, upload, download, share, comment on, or manage files in Google Drive." (17 операций)
8. **manage_email** — "Search, read, send, forward, or manage emails in a Google Workspace account. Supports Gmail search syntax." (15 операций)
9. **manage_meet** — "Browse past Google Meet conferences, participants, transcripts, recordings, and AI-generated smart notes. Requires Workspace Business Standard+ for transcripts/recordings." (11 операций)
10. **manage_sheets** — "Read, write, and manage Google Sheets spreadsheets." (13 операций)
11. **manage_tasks** — "Manage task lists and tasks in Google Tasks." (10 операций)

Маркер-скан steering-регексов по манифестам и tools.js: 0 совпадений. Описания сугубо функциональные, без само-продвижения, приоритетных директив или попыток вытеснить встроенные инструменты. Единственное мягкое steering — в manage_scratchpad ("Use for any multi-line content… For short one-liners, use the service tool directly instead") — внутренняя маршрутизация между собственными инструментами сервера, не против чужих.

Дополнительно: сервер публикует 4 MCP-ресурса (gws://safety/policies, gws://config/services, gws://config/workspace, gws://config/version) — метаданные, без инструкционного текста для модели.

## NOTES

- Код не минифицирован: чистый tsc-вывод с комментариями и sourcemaps, читается напрямую.
- Риск динамической сборки строк: низкий. Описания инструментов — статические строки в tools.js либо top-level `description` из YAML; единственная конкатенация — description enum-параметра `operation` собирается из per-operation descriptions манифеста ("op: desc | op: desc"), детерминированно из статических YAML, без env/сетевых источников.
- Просмотрено ~12 файлов: package.json, build/server/{server,tools}.js, build/factory/{registry,generator,patches}.js, 7 YAML-манифестов; плюс grep по всему build/ (72 JS-файла) на instructions/registerTool/steering-маркеры.
