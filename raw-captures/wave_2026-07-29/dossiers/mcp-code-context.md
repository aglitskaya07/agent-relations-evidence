# UNIT: mcp-code-context | npm v3.9.1 (published 2026-07-17T21:48:39.927Z) | рамки: pulsemcp | captured 2026-07-29 (static, tarball)

## VERDICT: MCP-сервер (подтверждено)

`dist/src/index.js` — тонкий бутстрап stdio-сервера: `new Server({ name: "mcp-code-context", version: "3.9.1" }, { capabilities: { tools: {} } })` из `@modelcontextprotocol/sdk/server/index.js`, `StdioServerTransport`, `ListToolsRequestSchema`-хендлер отдаёт `TOOLS` из `tools/toolDefinitions.js`. Назначение: Tree-sitter (WASM) анализ кода — repo map, чтение/запись символов, AST-трансформации, Ruby/Rails-интеллект.

## CHANNEL: instructions, npm (static)
(не обнаружены статически)

Конструктор `Server` получает только `{ capabilities: { tools: {} } }` — опции `instructions` нет. Grep по всему `dist/**/*.js` на `instructions` — ноль совпадений в серверном коде. Файлы `INSTRUCTIONS.md` и `llms.txt` в пакете есть, но это документация для человека/индексации, в протокол MCP они не передаются.

## CHANNEL: tool descriptions, npm (static, coverage=full)

Всего 28 инструментов: 18 в `dist/src/tools/toolDefinitionsCore.js` (CORE_TOOLS) + 10 в `dist/src/tools/toolDefinitionsAdmin.js` (ADMIN_TOOLS). Описания дословно:

### CORE_TOOLS (18)

1. **get_semantic_repo_map** — "Generate a compressed architectural overview of an entire repository"
2. **read_file_surgical** — "Read a file or extract a specific named symbol"
3. **analyze_impact** — "Find all files that depend on a given file"
4. **read_file_lines** — "Read specific line ranges from a file"
5. **search_code_pattern** — "Search for code patterns across multiple files"
6. **parse_file** — "Parse a file using Tree-sitter and extract symbols"
7. **write_file_surgical** — "Replace a symbol with new code. Phase 1 (dry-run): returns diff + token. Phase 2: confirm with token to apply."
8. **insert_symbol** — "Insert code at a specific location. Phase 1: returns diff + token. Phase 2: confirm with token to apply."
9. **remove_symbol** — "Remove a symbol from file. Phase 1: returns diff + token. Phase 2: confirm with token to apply."
10. **rename_symbol** — "Rename a symbol across the entire repository. Phase 1: returns diff + token. Phase 2: confirm with token to apply."
11. **ast_transform** — "Apply a declarative AST transformation to a symbol. Supports: add_parameter, wrap_with_try_catch, add_decorator, change_return_type, extract_variable. Uses two-phase write (Phase 1: preview diff, Phase 2: confirm with token)."
12. **search_symbols** — "Search symbols by name across the repo using AST (not text search). Finds classes, functions, methods by approximate name."
13. **explain_symbol** — "Get signature, location, and callers of a symbol in one call. More efficient than read_file_surgical + analyze_impact separately."
14. **batch_read** — "Read multiple symbols from multiple files in one call. Reduces N round-trips to 1."
15. **get_rate_limit_status** — "Get current rate limiter token balance and operation costs. Use before expensive operations to check available budget."
16. **get_gemfile_context** — "Parse Gemfile and return known gem behaviors with implicit Rails conventions. Useful for understanding what capabilities are active in a Ruby project without running the app."
17. **find_metaprogramming** — "Scan Ruby files for dynamic method generation entry points (define_method, method_missing, class_eval, ActiveSupport::Concern, etc.). Surfaces WHERE to look for magic methods."
18. **get_rails_routes** — "Parse config/routes.rb and return a structured route map (method, path, controller, action). Supports resources, resource, explicit HTTP verbs, namespace/scope, and root."

### ADMIN_TOOLS (10)

19. **rollback_file** — "Revert a file to its backup state"
20. **clean_backups** — "Remove all backup files for a project"
21. **get_server_stats** — "Get server telemetry, audit statistics, and health metrics"
22. **get_cache_stats** — "Get cache statistics (entries, size, hit rate)"
23. **clear_cache** — "Clear all cached parse results for a project"
24. **configure_file_watcher** — "Start/stop file watcher for auto-cache invalidation"
25. **get_file_watcher_status** — "Get file watcher status for a project"
26. **get_session_stats** — "Get statistics for the current MCP client session"
27. **clear_session_cache** — "Clear cache for current session only"
28. **list_pending_operations** — "List pending operations for crash recovery"

### Стиринг-маркеры

Совпадений с регексами стиринг-маркеров (instead of built-in, most powerful, always default, takes precedence, LAST resort, MUST use и т.д.) — НЕТ. Единственный оттенок самопредпочтения — внутренний, между собственными инструментами: "More efficient than read_file_surgical + analyze_impact separately" (explain_symbol) и "Reduces N round-trips to 1" (batch_read). Претензий на приоритет над встроенными инструментами клиента в описаниях нет.

## NOTES

- Код НЕ минифицирован: скомпилированный TypeScript с сохранёнными именами, комментариями и sourcemaps (.js.map + .d.ts в пакете).
- Риск динамической сборки строк — низкий: TOOLS — статический массив литералов, конкатенация только `[...CORE_TOOLS, ...ADMIN_TOOLS]` в barrel-файле; ListTools отдаёт его напрямую.
- Просмотрено: полный листинг пакета (206 файлов), вычитаны целиком index.js, toolDefinitions.js, toolDefinitionsCore.js, toolDefinitionsAdmin.js; grep по всем .js в dist на `instructions` и на альтернативные конструкторы серверов (McpServer/FastMCP — отсутствуют).
- В пакете лежат маркетинговые файлы для человека (HIRE_ME.md, SPONSORS.md, llms.txt, INSTRUCTIONS.md) — в MCP-канал не попадают.
