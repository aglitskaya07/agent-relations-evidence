# UNIT: metabase | Metabase | github easecloudio/mcp-metabase-server | тип автора: комьюнити | captured 2026-07-29 (static source)

## SERVER CONFIRMED

TypeScript-сервер на `@modelcontextprotocol/sdk`. `src/server.ts` — класс `MetabaseServer`, инстанцирует `new Server({ name: "metabase-server", version: "0.1.0" }, { capabilities: { resources: {}, tools: {} } })`, регистрирует обработчики `tools/list`, `tools/call`, `resources/list`, `resources/read`, транспорт `StdioServerTransport`. Не SDK, не прокси, не только-документация.

## CHANNEL: instructions
(не обнаружены статически)

Второй аргумент конструктора `new Server(...)` содержит только `capabilities`; поля `instructions` нет. Grep по `instructions` в `src/`, `package.json`, `smithery.yaml` — ноль совпадений. Отдельного обработчика `initialize` с кастомным ответом в коде нет (используется дефолтный из SDK).

## CHANNEL: tool descriptions (coverage=marker-scan+sample)

Всего инструментов, найденных статически: **95** (суммарный объём всех описаний — 5305 символов, т.е. в среднем ~56 символов на инструмент).

Регистрация — не через `registerTool`/`server.tool()`, а через массивы литералов `TaggedTool[]`, возвращаемые методами `getToolSchemas()` пяти классов-хендлеров плюс приватным `getAdditionalToolSchemas()` реестра. `ToolRegistry.getAllToolSchemas()` конкатенирует их и отдаёт в ответ `tools/list`.

Распределение по файлам (все в `src/handlers/`):
- `card-tools.ts` — 21
- `dashboard-tools.ts` — 27
- `database-tools.ts` — 16
- `table-tools.ts` — 17
- `tool-registry.ts` (`getAdditionalToolSchemas`: collections / users / permissions / search) — 12
- `schema-cache-tools.ts` — 2

Список всех 95 имён: list_cards, get_card, create_card, update_card, delete_card, execute_card, create_card_public_link, delete_card_public_link, list_public_cards, list_embeddable_cards, export_card_result, copy_card, get_card_query_metadata, get_card_dashboards, move_cards, move_cards_to_collection, execute_pivot_card_query, get_card_param_values, search_card_param_values, get_card_param_remapping, get_card_series, list_dashboards, create_dashboard, update_dashboard, delete_dashboard, get_dashboard_cards, add_card_to_dashboard, remove_card_from_dashboard, update_dashboard_card, create_dashboard_public_link, delete_dashboard_public_link, list_public_dashboards, list_embeddable_dashboards, copy_dashboard, get_dashboard_revisions, revert_dashboard, get_dashboard_related, get_dashboard, search_dashboards, execute_dashboard_card, favorite_dashboard, unfavorite_dashboard, add_text_block, update_dashcard, update_dashboard_cards, save_dashboard, save_dashboard_to_collection, get_dashboard_queries, list_databases, execute_query, get_database_schema, get_database_tables, create_database_connection, test_database_connection, sync_database_schema, get_database_sync_status, check_database_health, validate_database, list_database_schemas, get_database_metadata, get_database, update_database, delete_database, add_sample_database, get_schema_cache, refresh_schema_cache, list_tables, get_table, get_table_metadata, get_table_fks, get_field_id, update_table, sync_table_schema, rescan_table_field_values, discard_table_field_values, update_tables, get_table_related, get_card_table_fks, get_card_table_query_metadata, get_table_data, append_csv_to_table, replace_table_csv, reorder_table_fields, list_collections, create_collection, get_collection, update_collection, delete_collection, get_collection_items, list_users, create_user, list_permission_groups, create_permission_group, move_to_collection, search_content.

### Полный маркер-скан (по всем 95 описаниям)

Совпадений: **1**.

1. `get_field_id` (`src/handlers/table-tools.ts`) — дословная цитата совпадения с контекстом:
   > "Look up the Metabase field ID for a column by table ID and column name. Essential for building MBQL queries."

Все остальные 94 описания совпадений не дали.

### 10 репрезентативных полных описаний (дословно)

1. `get_schema_cache` — "Get cached database schema (tables + field IDs) for a Metabase database. Auto-fetches from Metabase if cache is missing or older than 24h. Use this BEFORE translating SQL to MBQL — field IDs in the response are required for MBQL field references like [\"field\", 42, null]."
2. `get_database_metadata` — "Get full metadata for a database including all tables and fields with their IDs. This is the authoritative source for field IDs needed in MBQL queries."
3. `get_table_metadata` — "Get full query metadata for a table including all fields with their IDs, types, and semantic types. Use this to get field IDs needed for MBQL queries."
4. `get_card` — "Get a single Metabase question/card by ID with full details including the SQL query (dataset_query). Returns MBQL 5 by default."
5. `execute_query` — "Execute a SQL query against a Metabase database"
6. `update_dashboard_cards` — "Bulk-replace all cards on a dashboard. WARNING: replaces the entire card layout."
7. `get_dashboard_queries` — "Extract all card queries from a dashboard with their resolved database IDs and SQL. Useful for auditing what data a dashboard queries."
8. `create_dashboard_public_link` — "Create a public sharing link for a dashboard. Returns the UUID for the public URL."
9. `delete_database` — "Permanently remove a database connection from Metabase"
10. `search_content` — "Search across all Metabase content"

### Дополнительно: скрытый канал управления составом инструментов

`ToolRegistry` читает `process.env.TOOL_MODE` (`essential` | `read` | `write` | `all`, дефолт `all`) и фильтрует выдачу `tools/list` по полю `metadata.mode` каждого инструмента; при непустом фильтре вызов невидимого инструмента отвергается с `MethodNotFound`. Это влияет на то, сколько из 95 описаний реально попадает в контекст модели, но текст описаний не меняет.
