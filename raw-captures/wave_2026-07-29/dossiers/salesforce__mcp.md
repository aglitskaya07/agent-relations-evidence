# UNIT: @salesforce/mcp | npm v0.30.15 (published 2026-07-09T14:42:18.783Z) | scopes: npm-top,smithery-top20 | captured 2026-07-29 (static, tarball)

## VERDICT: MCP server (wrapper/host)

A real stdio MCP server (oclif command `lib/index.js` → `SfMcpServer extends McpServer` from `@modelcontextprotocol/sdk` → `StdioServerTransport`). However, the tarball itself is a **host shell**: almost all working Salesforce tools live in external provider packages (`@salesforce/mcp-provider-dx-core`, `-code-analyzer`, `-lwc-experts`, `-aura-experts`, `-mobile-web`, `-devops`, `-scale-products`, `-metadata-enrichment` — registry in `lib/registry.js`), which are NOT included in the tarball (bundleDependencies: none, node_modules absent). Statically, the package defines only 2 "dynamic" core tools: `list_tools` and `enable_tools`.

## CHANNEL: instructions, npm (static)
(not found statically)

The constructor in `lib/index.js:151` passes only `{ name: 'sf-mcp-server', version, capabilities: { resources: {}, tools: {} } }` + telemetry option. There is no `instructions` and no custom initialize text in any file of the package (grep for `instructions` in JS — 0 matches).

## CHANNEL: tool descriptions, npm (static, coverage=full — for tools present in the tarball; 2 items)

### 1. list_tools (`lib/tools/list_tools.js`)
title: "List all individual tools"

description (verbatim):
```
List all available tools this Salesforce MCP server can offer, providing the enabled status and description of each.

AGENT INSTRUCTIONS:
DO NOT USE THIS TOOL if you already know what tool you need - try to call the tool directly first.
ONLY use this tool if:
1. You tried to call a tool and got an error that it doesn't exist or isn't enabled
2. You genuinely don't know what tools are available for a specific task
3. You need to discover new tools for an unfamiliar use case

If you find one or more tools you want to enable, call enable_tools with all the tool names.
Once you have enabled a tool, you MUST invoke the tool to accomplish the user's original request - DO NOT USE A DIFFERENT TOOL OR THE COMMAND LINE.
Once a tool has been enabled, you do not need to call list_tools again - instead, invoke the desired tool directly.
```

### 2. enable_tools (`lib/tools/enable_tools.js`)
title: "Enable Salesforce MCP tools"

description (verbatim):
```
Enable one or more of the tools the Salesforce MCP server provides.

AGENT INSTRUCTIONS:
Use list_tools first to learn what tools are available for enabling.
Once you have enabled the tool, you MUST invoke that tool to accomplish the user's original request - DO NOT USE A DIFFERENT TOOL OR THE COMMAND LINE.
```

### Marker scan (across all lib/ + bin/)
Matches on steering regexes:
- `enable_tools`: «you MUST invoke that tool to accomplish the user's original request - DO NOT USE A DIFFERENT TOOL OR THE COMMAND LINE.»
- `list_tools`: «you MUST invoke the tool to accomplish the user's original request - DO NOT USE A DIFFERENT TOOL OR THE COMMAND LINE.»

The steering character: a mildly aggressive locking-in of the agent inside the server ecosystem — after enable, the agent is forbidden in all caps to use another tool or CLI. A classic lock-in pattern "MUST invoke / DO NOT USE A DIFFERENT TOOL", but without anti-memory ("don't answer from memory"), without slander of built-in tools, and without precedence claims.

## NOTES
- Code is NOT minified: plain tsc output with sourceMappingURL, comments and JSDoc preserved. 16 JS files reviewed (lib/*.js, lib/tools/*.js, lib/utils/*.js, bin/*.js), ~1451 lines + package.json, README.md.
- There is no dynamic construction of description strings: descriptions of the two local tools are static template literals. But the main body of tool descriptions (dx-core: query_org, deploy_metadata, etc.; code-analyzer; lwc/aura experts; devops...) is pulled at runtime from 8 external npm packages `@salesforce/mcp-provider-*` — for full wave coverage, these packages must be analyzed as separate units.
- `registerTool` in `SfMcpServer` wraps all tools with telemetry (@salesforce/telemetry, PDP events) and a rate limiter; descriptions are not modified at registration (`lib/utils/tools.js` only reads `toolInfo.tool.description`).
- `--dynamic-tools` mode: only list_tools/enable_tools are registered, the rest are enabled by the agent on the fly through enable_tools + sendToolListChanged — the very mechanism of progressive tool disclosure.
