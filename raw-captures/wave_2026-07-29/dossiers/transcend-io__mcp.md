# UNIT: @transcend-io/mcp | npm v0.6.11 (published 2026-07-22T19:12:03.008Z) | рамки: npm-top,smithery-top20 | captured 2026-07-29 (static, tarball)

## VERDICT: MCP-сервер (umbrella-агрегатор)

Да, это MCP-сервер: `dist/cli.mjs` создаёт `ToolRegistry`, вызывает `buildMcpServer({name: "transcend-mcp", version, instructions, tools})` из `@transcend-io/mcp-server-base` и подключает `StdioServerTransport` (или HTTP-режим через `runMcpHttp`). Однако тарбол — тонкая обёртка: сами инструменты (описания, схемы, хендлеры) импортируются из 9 внешних пакетов-зависимостей (`@transcend-io/mcp-server-{admin,assessment,base,consent,discovery,docs,dsr,inventory,preferences,workflows}`), которых в тарболе НЕТ (нет node_modules, нет бандла их кода).

## CHANNEL: instructions, npm (static, 322 chars)

Найдены в `dist/cli.mjs` (константа `UMBRELLA_DOCS_SERVER_INSTRUCTIONS`, передаётся в `buildMcpServer` как `instructions`), дословно:

> For how-to, product concepts, setup guides, or "what is X" questions about Transcend (e.g. airgap, consent, DSR): (1) call docs_list with a keyword, (2) call docs_fetch on the best matching URL, (3) answer from that content. API tools return data from the signed-in organization; they do not replace product documentation.

Комментарий: мягкий steering — предписывает трёхшаговый workflow (docs_list → docs_fetch → answer from that content) для вопросов о продукте; без «primary/precedence/last resort»-риторики.

## CHANNEL: tool descriptions, npm (static, coverage=none)

(не извлекаемы статически из этого тарбола)

- README заявляет: «access to all 73 Transcend tools at once».
- Регистрация: `dist/oauth-scopes-uzulgUw_.mjs` → `ToolRegistry.registerAllTools()` вызывает `getDocsTools`, `getDSRTools`, `getConsentTools`, `getPreferenceTools`, `getInventoryTools`, `getDiscoveryTools`, `getAssessmentTools`, `getWorkflowTools`, `getAdminTools` — все из внешних npm-пакетов.
- Ни одной строки description инструмента в тарболе нет (проверены dist/*.mjs, *.map, *.d.mts, README). Известные из кода/README имена: `docs_list`, `docs_fetch` (упомянуты в instructions).
- Для полного покрытия описаний нужны тарболы 9 доменных пакетов @transcend-io/mcp-server-* (версии 0.3.4–0.7.0 зафиксированы точно в package.json).

## NOTES

- Код НЕ минифицирован (tsdown-бандл с сохранёнными именами и комментариями, source maps приложены).
- Риск динамической сборки строк: низкий в самом тарболе; instructions — статический литерал. Реальный контент описаний инструментов — вне тарбола (supply-chain перенос поверхности в зависимости).
- Просмотрено файлов: 7 (package.json, README.md, dist/cli.mjs, dist/index.mjs, dist/oauth-scopes-uzulgUw_.mjs, dist/*.d.mts, *.map по grep).
- Аутентификация: OAuth (UMBRELLA_OAUTH_SCOPES — merge scope'ов 8 доменов) либо TRANSCEND_API_KEY; deep links в ответах инструментов на app.transcend.io.
