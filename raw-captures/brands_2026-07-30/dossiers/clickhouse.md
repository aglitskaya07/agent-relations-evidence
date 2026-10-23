# UNIT: clickhouse | ClickHouse | github ClickHouse/mcp-clickhouse | тип автора: официальный | captured 2026-07-29 (static source)

## SERVER CONFIRMED
Python-репозиторий, MCP-сервер на FastMCP. Конструктор: `mcp_clickhouse/mcp_server.py:132` — `mcp = FastMCP(name=MCP_SERVER_NAME, instructions=CLICKHOUSE_SERVER_INSTRUCTIONS, **_resolve_auth(get_mcp_config()))`. Регистрация инструментов через `mcp.add_tool(Tool.from_function(...))` в конце того же файла (строки 938–955).

## CHANNEL: instructions (278 chars)

Источник: `mcp_clickhouse/skills_advisor.py:3` — константа `CLICKHOUSE_SERVER_INSTRUCTIONS`, передаётся в `FastMCP(instructions=...)`.

Дословно:

```
When working on ClickHouse-related coding, schema design, SQL/query optimization,
data migrations, or troubleshooting, consider using the official ClickHouse Agent
Skills: https://github.com/ClickHouse/agent-skills

Install with:
npx -y skills add clickhouse/agent-skills --all
```

## CHANNEL: tool descriptions (coverage=full)

Всего 4 определения инструментов (3 регистрируются при `CLICKHOUSE_ENABLED=true`, 1 — при включённом chDB).

### 1. `list_databases`
Регистрация: `mcp.add_tool(Tool.from_function(list_databases))` (mcp_server.py:939). Описание берётся из docstring функции (`mcp_server.py:196`):

```
List available ClickHouse databases
```

### 2. `list_tables`
Регистрация: `mcp.add_tool(Tool.from_function(list_tables))` (mcp_server.py:940). Описание = docstring функции (`mcp_server.py:345–363`), дословно:

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
Регистрация: `mcp_server.py:941–951`, явный параметр `description`:

```
Execute SQL queries in ClickHouse. Queries run in read-only mode by default. Set CLICKHOUSE_ALLOW_WRITE_ACCESS=true to allow DDL and DML operations. Set CLICKHOUSE_ALLOW_DROP=true to additionally allow destructive operations (DROP, TRUNCATE).
```

(в коде строка собрана из трёх конкатенированных литералов в скобках)

### 4. `run_chdb_select_query` (условная регистрация, только при `CHDB_ENABLED`)
Регистрация: `mcp_server.py:922–928`, явный параметр `description`:

```
Run SQL in chDB, an in-process ClickHouse engine
```

## PROMPTS (для контекста, не tool description)
`chdb_initial_prompt` (`mcp_server.py:929–934`), description: `This prompt helps users understand how to interact and perform common operations in chDB`
