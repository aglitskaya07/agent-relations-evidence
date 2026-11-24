# UNIT: elastic | Elasticsearch | github elastic/mcp-server-elasticsearch | author type: official | captured 2026-07-29 (static source)

## SERVER CHECK
Full-fledged MCP server. Rust, crate `rmcp` (`ServerHandler`, `tool_router`, `tool_handler`, macros `#[tool(...)]`), stdio and streamable HTTP transports (`src/protocol/stdio.rs`, `src/protocol/http.rs`), binary `src/bin/elasticsearch-core-mcp-server.rs`.

## CHANNEL: instructions (32 chars)
Source: `src/servers/elasticsearch/base_tools.rs:299`, the `instructions` field in `ServerInfo` (`get_info()`).

```
Provides access to Elasticsearch
```

## CHANNEL: tool descriptions (coverage=full)
All 5 tools are declared with the `#[tool(description = "...")]` attribute in `src/servers/elasticsearch/base_tools.rs` (the `#[tool_router] impl EsBaseTools` block).

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

### Parameter descriptions (doc comments for parameter structures, included in JSON Schema)
- `ListIndicesParams.index_pattern` — `Index pattern of Elasticsearch indices to list`
- `GetMappingsParams.index` — `Name of the Elasticsearch index to get mappings for`
- `SearchParams.index` — `Name of the Elasticsearch index to search`
- `SearchParams.fields` — `Name of the fields that need to be returned (optional)`
- `SearchParams.query_body` — `Complete Elasticsearch query DSL object that can include query, size, from, sort, etc.`
- `EsqlQueryParams.query` — `Complete Elasticsearch ES|QL query`
- `GetShardsParams.index` — `Optional index name to get shard information for`

## NOTES ON EXTENSIBILITY
In addition to 5 built-in tools, the server supports custom tools from the config (`CustomTool::Esql` / `CustomTool::SearchTemplate`, field `ToolBase.description`). Their texts are set by the operator in the configuration file; the repository has only the template example `elastic-mcp.json5` with placeholders ("Adds 42 to the input value", "This is the description for this stored template", "This is the description for this inline template", "Use this parameter to blah blah and blah") — this is a format demonstration, not shipped descriptions. There is also an include/exclude filter that hides part of the tools (`src/servers/mod.rs`).
