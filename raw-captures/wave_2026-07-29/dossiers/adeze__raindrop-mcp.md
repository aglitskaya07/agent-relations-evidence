# UNIT: @adeze/raindrop-mcp | npm v2.4.5 (published 2026-03-11T06:15:52.834Z) | рамки: pulsemcp | captured 2026-07-29 (static, tarball)

## VERDICT: MCP-сервер

Полноценный MCP-сервер для Raindrop.io (закладки). Два entry point: `build/index.js` (stdio, bin `raindrop-mcp`) и `build/server.js` (HTTP/Express). Внутри — `new McpServer(...)` из `@modelcontextprotocol/sdk` (класс `RaindropMCPService`, src/services/raindropmcp.service.ts по сорсмапам), регистрация инструментов через `server.registerTool(...)` в цикле по декларативному массиву `toolConfigs`, плюс resources, prompts и experimental elicitation capability.

## CHANNEL: instructions, npm (static)
(не обнаружены статически)

Конструктор `McpServer` получает только `{ name: "raindrop-mcp", version, description: "MCP Server for Raindrop.io with advanced interactive capabilities" }` — поле `instructions` не передаётся ни в index.js (строка ~41156), ни в server.js (строка ~55910). Отдельного текста в initialize тоже нет.

## CHANNEL: tool descriptions, npm (static, coverage=full)

17 инструментов, все описания — статические строковые литералы, приведены дословно:

1. **diagnostics** — "Diagnostics resource and runtime metadata."
2. **collection_list** — "Lists all Raindrop.io collections as a flat list."
3. **get_collection_tree** — "Returns a hierarchical view of all collections with full breadcrumb paths."
4. **collection_manage** — "Creates, updates, or deletes a collection. Use the operation parameter to specify the action."
5. **bookmark_search** — "Searches bookmarks with advanced filters, tags, and full-text search."
6. **bookmark_manage** — "Creates, updates, or deletes bookmarks. Use the operation parameter to specify the action."
7. **get_raindrop** — "Fetch a single Raindrop.io bookmark by ID."
8. **list_raindrops** — "List Raindrop.io bookmarks for a collection with pagination."
9. **bulk_edit_raindrops** — "Bulk update, move, or remove bookmarks in a specific collection."
10. **tag_manage** — "Renames, merges, or deletes tags. Use the operation parameter to specify the action."
11. **highlight_manage** — "Creates, updates, or deletes highlights. Use the operation parameter to specify the action."
12. **library_audit** — "Scans the entire library for broken links and duplicate bookmarks."
13. **empty_trash** — "Permanently delete all bookmarks currently in the trash collection. Requires 'confirm: true' to execute."
14. **cleanup_collections** — "Remove all collections that do not contain any bookmarks. Requires 'confirm: true' to execute."
15. **remove_duplicates** — "Optimized duplicate deletion pattern. Scans all collections and removes duplicates in batches of 50 to minimize round-trips. Supports dry run to report counts without deleting."
16. **get_suggestions** — "Get AI-powered suggestions for tags and collections for a specific URL or existing bookmark."
17. **suggest_tags** — "Uses AI to suggest relevant tags based on bookmark metadata (title, URL, description)."

Маркер-паттерны стиринга (instead of built-in / prefer / primary / MUST use / takes precedence и т.п.) в описаниях НЕ встречаются. Тон нейтрально-функциональный; единственные императивы — защитные ("Requires 'confirm: true' to execute").

## Прочие каналы

- **Prompts (3):** organize_by_topic, find_duplicates, export_markdown — нейтральные системные промпты про организацию закладок, без стиринга в сторону сервера.
- **Sampling model hints** в suggestion-инструментах: `hints: [{ name: "claude-3-5-sonnet" }, { name: "gpt-4o" }]` — предпочтения модели для MCP sampling, не стиринг агента.
- **Resources:** mcp://user/profile, diagnostics://server — статические JSON-заглушки.

## NOTES

- Код НЕ минифицирован: bun-бандл ESM с сорсмапами, имена и структура читаемы; node_modules (SDK, axios, express, keyv, openai и пр.) вбандлены в те же файлы (~1.9 MB server.js, ~1.4 MB index.js).
- Риск динамической сборки строк описаний — низкий: все description — литералы в декларативных tool-конфигах; динамики только title (генерируется из name капитализацией).
- Просмотрено файлов: 3 содержательно (package.json, build/index.js, build/server.js); всего в тарболе 7 (плюс LICENSE, README.md, 2 сорсмапа).
