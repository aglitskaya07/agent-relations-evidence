# UNIT: agentation-mcp | npm v1.2.0 (published 2026-02-15T20:37:04.456Z) | рамки: npm-top | captured 2026-07-29 (static, tarball)

Верифицированный MCP-сервер: stdio-сервер (`new Server({name: "agentation", version: "0.0.1"}, {capabilities: {tools: {}}})` + `StdioServerTransport`, dist/index.mjs:1434-1458) и дополнительный Streamable HTTP-вариант (`createMcpSession`, dist/index.mjs:1704-1723). Зависимость `@modelcontextprotocol/sdk`. Назначение: визуальный фидбек (аннотации в браузере) для AI coding agents; SQLite/in-memory store, webhooks.

## CHANNEL: instructions, npm (static)
(не обнаружены статически)

Оба конструктора Server получают только `{name, version}` и `{capabilities: {tools: {}}}` — поле `instructions` нигде не передаётся; grep по слову `instructions` во всех трёх бандлах (cli.js, index.js, index.mjs) даёт 0 совпадений.

## CHANNEL: tool descriptions, npm (static, coverage=full)

Статический массив `TOOLS` (dist/index.mjs:982-1119), отдаётся как есть в ListTools обоими транспортами. 9 инструментов, все дословно:

1. **agentation_list_sessions** — "List all active annotation sessions"
2. **agentation_get_session** — "Get a session with all its annotations"
3. **agentation_get_pending** — "Get all pending (unacknowledged) annotations for a session. Use this to see what feedback the human has given that needs attention."
4. **agentation_get_all_pending** — "Get all pending annotations across ALL sessions. Use this to see all unaddressed feedback from the human across all pages they've visited."
5. **agentation_acknowledge** — "Mark an annotation as acknowledged. Use this to let the human know you've seen their feedback and will address it."
6. **agentation_resolve** — "Mark an annotation as resolved. Use this after you've addressed the feedback. Optionally include a summary of what you did."
7. **agentation_dismiss** — "Dismiss an annotation. Use this when you've decided not to address the feedback, with a reason why."
8. **agentation_reply** — "Add a reply to an annotation's thread. Use this to ask clarifying questions or provide updates to the human."
9. **agentation_watch_annotations** — "Block until new annotations appear, then collect a batch and return them. Triggers automatically when annotations are created — the user just annotates in the browser and the agent picks them up. After detecting the first new annotation, waits for a batch window to collect more before returning. Use in a loop for hands-free processing. After addressing each annotation, call agentation_resolve with the annotation ID and a summary of what you did. Only resolve annotations the user accepted — if the user rejects your change, leave the annotation open."

Стиринг-маркеры: мягкие поведенческие директивы в №9 ("Use in a loop for hands-free processing", "After addressing each annotation, call agentation_resolve…", "Only resolve annotations the user accepted") и шаблон "Use this to/when/after" в №3-8 — рабочий workflow-гайд, не кросс-инструментное вытеснение конкурентов; маркеров типа "instead of built-in / takes precedence / MUST use" нет.

## NOTES
- Код — бандл tsup, читаемый (не минифицирован); sourcemaps приложены.
- TOOLS — статический литерал; сборки динамических строк описаний нет, риск динамики низкий. Описания в cli.js и index.mjs побайтно совпадают (diff по извлечённым description — идентичны).
- Просмотрено: package.json, README.md (заголовочно), dist/cli.js, dist/index.js, dist/index.mjs (~256 KB текста; .d.ts и .map — по касательной).
- Расхождение версий: package.json v1.2.0, но в конструкторе Server захардкожено version "0.0.1".
