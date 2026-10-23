# UNIT: elastic | Elasticsearch | github elastic/mcp-server-elasticsearch | тип автора: официальный | captured 2026-07-29 (static source)

## SERVER CHECK
Полноценный MCP-сервер. Rust, crate `rmcp` (`ServerHandler`, `tool_router`, `tool_handler`, макросы `#[tool(...)]`), транспорты stdio и streamable HTTP (`src/protocol/stdio.rs`, `src/protocol/http.rs`), бинарь `src/bin/elasticsearch-core-mcp-server.rs`.

## CHANNEL: instructions (32 chars)
Источник: `src/servers/elasticsearch/base_tools.rs:299`, поле `instructions` в `ServerInfo` (`get_info()`).

```
Provides access to Elasticsearch
```

## CHANNEL: tool descriptions (coverage=full)
Все 5 инструментов объявлены атрибутом `#[tool(description = "...")]` в `src/servers/elasticsearch/base_tools.rs` (блок `#[tool_router] impl EsBaseTools`).

1. **list_indices** — `List all available Elasticsearch indices`
   (annotations: title = "List ES indices", read_only_hint = true)

2. **get_mappings** — `Get field mappings for a specific Elasticsearch index`
   (annotations: title = "Get ES index mappings", read_only_hint = true)

3. **search** — `Perform an Elasticsearch search with the provided query DSL.`
   (annotations: title = "Elasticsearch search DSL query", read_only_hint = true)

4. **esql** — `Perform an Elasticsearch ES|QL query.`
   (annotations: title = "Elasticsearch ES|QL query", read_only_hint = true)

5. **get_shards** — `Get shard information for all or specific indices.`
   (annotations: title = "Get ES shard information", read_only_hint = true)

### Описания параметров (doc-комментарии структур параметров, попадают в JSON Schema)
- `ListIndicesParams.index_pattern` — `Index pattern of Elasticsearch indices to list`
- `GetMappingsParams.index` — `Name of the Elasticsearch index to get mappings for`
- `SearchParams.index` — `Name of the Elasticsearch index to search`
- `SearchParams.fields` — `Name of the fields that need to be returned (optional)`
- `SearchParams.query_body` — `Complete Elasticsearch query DSL object that can include query, size, from, sort, etc.`
- `EsqlQueryParams.query` — `Complete Elasticsearch ES|QL query`
- `GetShardsParams.index` — `Optional index name to get shard information for`

## NOTES ON EXTENSIBILITY
Помимо 5 встроенных инструментов сервер поддерживает пользовательские инструменты из конфига (`CustomTool::Esql` / `CustomTool::SearchTemplate`, поле `ToolBase.description`). Их тексты задаёт оператор в файле конфигурации; в репозитории есть только шаблонный пример `elastic-mcp.json5` с плейсхолдерами («Adds 42 to the input value», «This is the description for this stored template», «This is the description for this inline template», «Use this parameter to blah blah and blah») — это демонстрация формата, а не поставляемые описания. Есть также фильтр include/exclude, скрывающий часть инструментов (`src/servers/mod.rs`).
