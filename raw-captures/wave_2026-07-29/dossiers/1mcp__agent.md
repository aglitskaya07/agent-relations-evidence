# UNIT: @1mcp/agent | npm v0.34.4 (published 2026-07-21T16:16:20.606Z) | рамки: pulsemcp,smithery-top20 | captured 2026-07-29 (static, tarball)

## ТИП: MCP-агрегатор/прокси, НО с собственным серверным кодом MCP

Это 1MCP — unified proxy, который сам поднимает `new Server(...)` из `@modelcontextprotocol/sdk` на каждую входящую сессию (`build/core/server/connectionManager.js:180`), агрегирует downstream-серверы и добавляет собственные внутренние инструменты (mcp_install, mcp_search, tool_invoke и т.д.). Квалифицирован как сервер, не как NOT-A-SERVER.

## CHANNEL: instructions, npm (static, ~3900 chars template)

Строка `instructions` собирается ДИНАМИЧЕСКИ на каждую сессию: `InstructionAggregator.getFilteredInstructions()` рендерит Handlebars-шаблон и результат передаётся в конструктор `new Server(this.serverConfig, { ...capabilities, instructions: filteredInstructions })` (`connectionManager.js:175-180`). Инструкции downstream-серверов оборачиваются в XML-теги `<server-name>...</server-name>` и вставляются внутрь. Пользователь может задать customTemplate; при его падении в LLM уходит notice:

> `⚠️ IMPORTANT: The user's custom instruction template failed to render due to an error: "<msg>". Please inform the user that their custom template configuration has an issue and the default template is being used instead. They should check their template syntax.`

Статический скелет — DEFAULT_INSTRUCTION_TEMPLATE (`build/core/instructions/templateTypes.js:31-168`), дословно (Handlebars):

```
# {{title}}

{{#if hasServers}}
You are interacting with 1MCP, a proxy server that aggregates capabilities from multiple MCP (Model Context Protocol) servers. 1MCP acts as a unified gateway, allowing you to access tools and resources from various specialized MCP servers through a single connection.

{{#if lazyLoading.enabled}}
## Tool Access: Meta-Tool Discovery Mode

1MCP is running in {{lazyLoading.mode}} mode for optimized token usage. Tools are loaded on-demand using meta-tools for discovery.

### Meta-Tool Workflow

When you need to use a tool, follow this three-step discovery process:

1. **List Available Tools**: Call `tool_list` to see all available tools
   - Returns tool names, source servers, and descriptions
   - Use optional filters: `server`, `pattern`, `tag`, `limit`, `cursor`

2. **Describe Tool**: Call `tool_schema` with `server` and `toolName` to get the full input schema
   - Returns complete tool definition including required parameters
   - Load schema only when you need to use the tool

3. **Call Tool**: Invoke `tool_invoke` with `server`, `toolName`, and `args`
   - Executes the tool on the upstream server
   - Returns the result with structured responses

### Error Handling

Meta-tools use structured error responses with `_errorType` field:

- **validation_error**: Missing or invalid parameters
  - Fix: Provide all required parameters with correct types

- **not_found_error**: Tool or server not found
  - Fix: Call `tool_list` to verify tool exists

- **upstream_error**: Server-side error or connection issue
  - Fix: This is an upstream server issue - may need to retry or report

### Tool Categories

Tools are organized by server for easier discovery:
{{#each servers}}
- **{{name}}**: {{#if hasInstructions}}{{description}}{{else}}Various tools from {{name}}{{/if}}
{{/each}}

{{#if lazyLoading.catalog}}
### Tool Catalog ({{lazyLoading.availableToolsCount}} tools)

{{#each lazyLoading.catalog}}
- `{{server}}:{{name}}` - {{description}}
{{/each}}

{{#if (gt lazyLoading.availableToolsCount 100)}}
### Pagination for Large Tool Sets

When working with many tools, use pagination:
- Start with `tool_list` with `limit` parameter
- Use returned `cursor` for next page
- Continue until `hasMore` is false
{{/if}}
{{/if}}

{{else}}
## How 1MCP Works

- **Unified Access**: Connect to multiple MCP servers through one proxy
- **Tool Aggregation**: All tools are available with the naming pattern `{{toolPattern}}`
- **Resource Sharing**: Access files, data, and capabilities across different servers
- **Intelligent Routing**: Your requests are automatically routed to the appropriate servers
{{/if}}

## Currently Connected Servers

{{connectedServerCount}} MCP {{connectedPluralServers}} {{connectedIsAre}} currently available{{filterContext}}:

{{#each servers}}
{{name}}
{{/each}}

{{#if hasInstructionalServers}}
{{#unless lazyLoading.enabled}}
## Available Capabilities

All tools from connected servers are accessible using the format: `{{toolPattern}}`

Examples:
{{#each examples}}
- `{{name}}` - {{description}}
{{/each}}
{{/unless}}

## Server-Specific Instructions

The following sections contain instructions from each connected MCP server. Each server's instructions are wrapped in XML-like tags (e.g., `<server-name>instructions</server-name>`) to clearly identify their source and scope.

{{#each servers}}
{{#if hasInstructions}}
<{{name}}>
{{instructions}}
</{{name}}>

{{/if}}
{{/each}}

## Tips for Using 1MCP

{{#if lazyLoading.enabled}}
- Use meta-tools for efficient tool discovery and on-demand loading
- Tools are organized by server name to avoid naming conflicts
- Cache statistics: {{lazyLoading.cachedToolsCount}}/{{lazyLoading.availableToolsCount}} tools loaded
- Call `tool_list` first to discover available tools
{{else}}
- Tools are namespaced by server to avoid conflicts
{{/if}}

{{else}}
## Status

Connected servers are available but have not provided instructions yet. Tools and capabilities will become available once servers provide their instructions.
{{/if}}

{{else}}
You are interacting with 1MCP, a proxy server that aggregates capabilities from multiple MCP (Model Context Protocol) servers.

## Current Status

No MCP servers are currently connected. 1MCP is ready to connect to servers and provide unified access to their capabilities once they become available.

## What 1MCP Provides

- **Unified Access**: Connect to multiple MCP servers through one proxy
- **Tool Aggregation**: Access tools using the pattern `{{toolPattern}}`
- **Resource Sharing**: Share files, data, and capabilities across servers
- **Intelligent Routing**: Automatic request routing to appropriate servers

1MCP will automatically detect and connect to available MCP servers. Once connected, their tools and capabilities will become available through the unified interface.
{{/if}}
```

Default title: `1MCP - Model Context Protocol Proxy`; default toolPattern: `{server}_1mcp_{tool}`; default examples: `filesystem_1mcp_read_file` — "Read files through filesystem server", `web_1mcp_search` — "Search the web through web server", `database_1mcp_query` — "Query databases through database server".

## CHANNEL: tool descriptions, npm (static, coverage=full)

Собственные (внутренние) инструменты — 17 шт. Проксируемые инструменты downstream-серверов — динамические, их описания пробрасываются от upstream и в пакете отсутствуют.

### Discovery (build/core/capabilities/internal/discoveryTools.js)
1. **mcp_search** — `Search for MCP servers in the registry`
2. **mcp_registry_status** — `Check registry availability and performance`
3. **mcp_registry_info** — `Get detailed registry information`
4. **mcp_registry_list** — `List available registries`
5. **mcp_info** — `Get detailed information about a specific MCP server`

### Installation (installationTools.js)
6. **mcp_install** — `Install a new MCP server. Use package+command+args for direct package installation (e.g., npm packages), or just name for registry-based installation`
7. **mcp_uninstall** — `Remove an MCP server`
8. **mcp_update** — `Update an MCP server`

### Management (managementTools.js)
9. **mcp_enable** — `Enable an MCP server`
10. **mcp_disable** — `Disable an MCP server`
11. **mcp_list** — `List MCP servers`
12. **mcp_status** — `Get MCP server status`
13. **mcp_edit** — `Edit MCP server configuration`
14. **mcp_reload** — `Reload MCP server or configuration`

### Lazy-loading meta-tools (lazyTools.js)
15. **tool_list** — `List all available MCP tools with names and descriptions. Use for tool discovery.`
16. **tool_schema** — `Get the full schema for a specific tool including input validation rules`
17. **tool_invoke** — `Execute any tool on any MCP server with proper argument validation`

Маркер-скан по регексам steering-паттернов: в описаниях внутренних инструментов совпадений НЕТ (нейтральные). Единственные steering-подобные элементы — в instructions-канале: (а) императив «Please inform the user…» при падении custom template; (б) сама архитектура: инструкции чужих серверов транслируются клиенту дословно внутри `<server-name>`-тегов, т.е. 1MCP — усилитель steering-контента upstream-серверов.

## NOTES
- Код не минифицирован: обычный tsc-вывод с .d.ts и sourcemaps, читается свободно. 340 JS-файлов в build/; детально просмотрено ~10 ключевых (server.js, connectionManager.js, instructionAggregator.js, templateTypes.js, 4 файла internal-tools, toolSchemas.js, discovery.js schemas).
- Риск динамической сборки строк: ВЫСОКИЙ по дизайну — итоговые instructions рендерятся Handlebars-шаблоном в рантайме и включают произвольные instructions downstream-серверов и пользовательский customTemplate (до 1MB). Статически зафиксирован только скелет.
- Описания собственных инструментов — статические литералы, динамики нет. Проксируемые инструменты переименовываются по паттерну `{server}_1mcp_{tool}`, описания upstream не модифицируются (по просмотренному коду).
