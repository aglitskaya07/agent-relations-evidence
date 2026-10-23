# UNIT: @serdnaley/metabase-mcp | npm v0.2.0 (published 2026-04-16T08:12:08.565Z) | рамки: npm-top,docker-catalog | captured 2026-07-29 (static, tarball)

## VERDICT: MCP server

Полноценный MCP-сервер: `new McpServer({ name: "metabase-mcp", version: "0.1.0" })` + `StdioServerTransport`, зависимость `@modelcontextprotocol/sdk` ^1.29.0. Бандл собран bun'ом из TypeScript (`dist/index.js`, ~31 445 строк, не минифицирован — читаемые имена и комментарии `// src/tools/*.ts`). 128 инструментов, регистрируются статически через `server.tool("name", "description", schema, handler)`; часть write-инструментов оборачивается в `if (!config2.readOnly)`.

## CHANNEL: instructions, npm (static)
(не обнаружены статически)

Конструктору `McpServer` передаются только `name` и `version` — поле `instructions` не используется. Единственные вхождения `instructions` в бандле — код самого SDK (`this._instructions = options?.instructions`).

## CHANNEL: tool descriptions, npm (static, coverage=marker-scan+sample)

Всего инструментов: **128** (все зарегистрированы статическими двойными кавычками, динамических имён/описаний нет; шаблонных литералов в аргументах `server.tool(` нет).

### Маркер-скан (полный, по всем 128 описаниям)
Регексы волны (instead of built-in, most powerful, always default, call this immediately, Best for:, prefer(red), Prefer this over, faster and cheaper, N% faster, PRECEDENCE, takes precedence, LAST resort, Do NOT answer from memory, even when you think you know, even if isn't named, The user has installed/chosen/set up, primary tool/provider/interface, refund/credit/reward, MUST use/run/be executed, ignore other/previous, whenever the user, Assume appropriate/legitimate, Perfect for/Great for/essential for, trusted sources, never means leave):

**Совпадений: 0.**

Описания сухие, функциональные, в стиле API-документации ("Get card details (query definition, visualization settings)"). Steering-приёмов не обнаружено.

### 8 репрезентативных полных описаний (дословно)
- **search** — "Search across all Metabase entities (cards, dashboards, collections, tables, etc.)"
- **execute_card_query** — "Run a saved question and return results. For parameterized cards, pass template tag values as key-value pairs (e.g. { fromDate: '2024-01-01', toDate: '2024-12-31' }). For date ranges in native queries, use two separate date/single parameters."
- **execute_query** — "Run an ad-hoc query (native SQL or structured) and return results"
- **create_card_public_link** — "Generate a public sharing link for a card. Returns the card with a public_uuid field. The public URL is {metabase_url}/public/question/{uuid}. Public sharing must be enabled in Metabase admin settings."
- **update_permissions_graph** — "Update the data permissions graph. Must include the 'revision' field from get_permissions_graph for optimistic locking."
- **create_user** — "Create a new Metabase user"
- **update_setting** — "Update a Metabase setting value"
- **create_alert** — "Create an alert on a saved question. Alerts notify recipients via email or Slack when query results meet a condition."

### Полный список имён инструментов
search, list_databases, get_database, get_database_metadata, list_database_schemas, get_database_schema, create_database, update_database, delete_database, validate_database, sync_database_schema, notify_database, get_table, get_table_query_metadata, get_field, get_field_values, update_table, update_field, rescan_field_values, discard_field_values, reorder_fields, get_collection_tree, list_collections, get_collection, list_collection_items, create_collection, update_collection, list_cards, get_card, execute_card_query, create_card, update_card, delete_card, copy_card, create_card_public_link, delete_card_public_link, list_dashboards, get_dashboard, create_dashboard, update_dashboard, delete_dashboard, copy_dashboard, update_dashboard_cards, create_dashboard_public_link, delete_dashboard_public_link, list_actions, get_action, create_action, update_action, delete_action, execute_action, create_action_public_link, delete_action_public_link, execute_query, list_users, get_user, get_current_user, list_groups, create_user, update_user, deactivate_user, reactivate_user, create_group, update_group, delete_group, add_group_member, remove_group_member, get_permissions_graph, get_collection_permissions, update_permissions_graph, update_collection_permissions, list_segments, get_segment, create_segment, update_segment, delete_segment, list_revisions, revert_revision, list_settings, get_setting, update_setting, list_alerts, get_alert, list_dashboard_subscriptions, create_alert, update_alert, delete_alert, create_dashboard_subscription, update_dashboard_subscription, delete_dashboard_subscription, generate_xray, invalidate_cache, update_cache_config, persist_model, unpersist_model, refresh_persisted_model, upload_csv, get_activity, list_tasks, get_task, list_snippets, get_snippet, create_snippet, update_snippet, delete_snippet, list_glossary_terms, get_glossary_term, create_glossary_term, update_glossary_term, delete_glossary_term, list_documents, get_document, create_document, update_document, delete_document, list_timelines, get_timeline, create_timeline, update_timeline, delete_timeline, create_timeline_event, update_timeline_event, delete_timeline_event, list_bookmarks, create_bookmark, delete_bookmark, create_moderation_review, translate_entity_ids

## NOTES
- Файлы в пакете: 3 (README.md, package.json, dist/index.js). Просмотрены все.
- Код НЕ минифицирован (bun build без minify, читаемые имена, сохранены комментарии путей исходников).
- Риск динамической сборки строк: низкий — все 128 вызовов `server.tool(` имеют литеральные имя и описание; instructions в конструктор не передаются нигде.
- package.json description сам по себе рекламно-нейтральный: "MCP server for Metabase — 128 tools for full API coverage…" — заявленное число совпадает с фактическим (128).
