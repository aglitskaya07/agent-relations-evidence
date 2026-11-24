# UNIT: clickhouse | ClickHouse | github ClickHouse/mcp-clickhouse | author type: official | captured 2026-07-29 (static source)

## SERVER CONFIRMED
Python repository, MCP server on FastMCP. Constructor: `mcp_clickhouse/mcp_server.py:132` — `mcp = FastMCP(name=MCP_SERVER_NAME, instructions=CLICKHOUSE_SERVER_INSTRUCTIONS, **_resolve_auth(get_mcp_config()))`. Tool registration via `mcp.add_tool(Tool.from_function(...))` at the end of the same file (lines 938–955).

## CHANNEL: instructions (278 chars)

Source: `mcp_clickhouse/skills_advisor.py:3` — constant `CLICKHOUSE_SERVER_INSTRUCTIONS`, passed to `FastMCP(instructions=...)`.

Literally:

```
When working on ClickHouse-related coding, schema design, SQL/query optimization,
data migrations, or troubleshooting, consider using the official ClickHouse Agent
Skills: https://github.com/ClickHouse/agent-skills

Install with:
npx -y skills add clickhouse/agent-skills --all
```

## CHANNEL: tool descriptions (coverage=full)

There are 4 tool definitions in total (3 are registered when `CLICKHOUSE_ENABLED=true`, 1 — when chDB is enabled).

### 1. `list_databases`
Registration: `mcp.add_tool(Tool.from_function(list_databases))` (mcp_server.py:939). The description is taken from the function docstring (`mcp_server.py:196`):

```
List available ClickHouse databases
```

### 2. `list_tables`
Registration: `mcp.add_tool(Tool.from_function(list_tables))` (mcp_server.py:940). Description = function docstring (`mcp_server.py:345–363`), verbatim:

```
List available ClickHouse tables in a database, including schema, comment,
row count, and column count.

Args:
    database: The database to list tables from
    like: Optional LIKE pattern to filter table names
    not_like: Optional NOT LIKE pattern to exclude table names
    page_token: Token for pagination, obtained from a previous call
    page_size: Number of tables to return per page (default: 50)
    include_detailed_columns: Whether to include detailed column metadata (default: True).
        When False, the columns array will be empty but create_table_query still contains
        all column information. This reduces payload size for large schemas.

Returns:
    A JSON-encoded string of an object containing:
    - tables: List of table information (as dictionaries)
    - next_page_token: Token for the next page, or None if no more pages
    - total_tables: Total number of tables matching the filters
```

### 3. `run_query`
Registration: `mcp_server.py:941–951`, explicit `description` parameter:

```
Execute SQL queries in ClickHouse. Queries run in read-only mode by default. Set CLICKHOUSE_ALLOW_WRITE_ACCESS=true to allow DDL and DML operations. Set CLICKHOUSE_ALLOW_DROP=true to additionally allow destructive operations (DROP, TRUNCATE).
```

(in code, the string is assembled from three concatenated literals in parentheses)

### 4. `run_chdb_select_query` (conditional registration, only when `CHDB_ENABLED`)
Registration: `mcp_server.py:922–928`, explicit `description` parameter:

```
Run SQL in chDB, an in-process ClickHouse engine
```

## PROMPTS (for context, not tool description)
`chdb_initial_prompt` (`mcp_server.py:929–934`), description: `This prompt helps users understand how to interact and perform common operations in chDB`
