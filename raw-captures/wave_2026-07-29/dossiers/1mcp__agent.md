# UNIT: @1mcp/agent | npm v0.34.4 (published 2026-07-21T16:16:20.606Z) | frames: pulsemcp,smithery-top20 | captured 2026-07-29 (static, tarball)

## TYPE: MCP aggregator/proxy, BUT with its own MCP server code

This is 1MCP — unified proxy, which itself spins up `new Server(...)` from `@modelcontextprotocol/sdk` for each incoming session (`build/core/server/connectionManager.js:180`), aggregates downstream servers, and adds its own internal tools (mcp_install, mcp_search, tool_invoke, etc.). Qualified as a server, not as NOT-A-SERVER.

## CHANNEL: instructions, npm (static, ~3900 chars template)

The `instructions` string is assembled DYNAMICALLY for each session: `InstructionAggregator.getFilteredInstructions()` renders a Handlebars template and the result is passed to the constructor `new Server(this.serverConfig, { ...capabilities, instructions: filteredInstructions })` (`connectionManager.js:175-180`). Instructions from downstream servers are wrapped in XML tags `<server-name>...</server-name>` and inserted inside. The user can set customTemplate; if it fails, the LLM receives notice:

> `⚠️ IMPORTANT: The user's custom instruction template failed to render due to an error: "<msg>". Please inform the user that their custom template configuration has an issue and the default template is being used instead. They should check their template syntax.`

Static skeleton — DEFAULT_INSTRUCTION_TEMPLATE (`build/core/instructions/templateTypes.js:31-168`), verbatim (Handlebars):

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

Own (internal) tools — 17 items. Proxied downstream-server tools — dynamic, their descriptions are passed through from upstream and are absent in the package.

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

Marker scan for steering regexes: no matches in the descriptions of internal tools (neutral). The only steering-like elements are in the instructions channel: (a) the imperative "Please inform the user…" when the custom template fails; (b) the architecture itself: instructions from other servers are passed through to the client verbatim inside `<server-name>` tags, i.e. 1MCP is an amplifier of upstream servers' steering content.

## NOTES
- The code is not minified: ordinary tsc output with .d.ts and sourcemaps, readable without issue. 340 JS files in build/; about 10 key ones were reviewed in detail (server.js, connectionManager.js, instructionAggregator.js, templateTypes.js, 4 internal-tools files, toolSchemas.js, discovery.js schemas).
- Risk of dynamic construction of strings: HIGH by design — the final instructions are rendered by a Handlebars template at runtime and include arbitrary instructions from downstream servers and the user's customTemplate (up to 1MB). Only the skeleton is statically fixed.
- Descriptions of own tools are static literals; there is no dynamic behavior. Proxied tools are renamed by the pattern `{server}_1mcp_{tool}`, and upstream descriptions are not modified (based on the code reviewed).
