# UNIT: touchdesigner-mcp-server | npm v1.5.0 (published 2026-07-11T03:22:00.223Z) | scope: pulsemcp | captured 2026-07-29 (static, tarball)

## VERDICT: MCP server (confirmed)
`dist/server/touchDesignerServer.js` creates `new McpServer({ name: "TouchDesigner", version: MCP_SERVER_VERSION }, { capabilities: { logging: {}, prompts: {}, tools: {} } })` from `@modelcontextprotocol/sdk/server/mcp.js`; registers tools and prompts; stdio/HTTP transports in `dist/transport/`. This is a full local MCP server, proxying commands into TouchDesigner through its WebServer DAT API.

## CHANNEL: instructions, npm (static)
(not found statically)

Only `name`, `version`, and `capabilities` are passed to the `McpServer` constructor — there is no `instructions` field either in the constructor or anywhere else in dist (grep for "instructions" returns only connection error messages with a link to README).

## CHANNEL: tool descriptions, npm (static, coverage=full)
14 tools: 13 from the `TOOL_DEFINITIONS` table (`dist/features/tools/toolDefinitions.js`) + meta-tool `describe_td_tools` (`dist/features/tools/handlers/tdTools.js`). Registration: `server.tool(definition.name, definition.description, schema, handler)` — the description is passed verbatim, without dynamic reassembly.

1. **get_td_info** — "Get server information from TouchDesigner"
2. **execute_python_script** — "Execute a Python script in TouchDesigner (detailLevel=minimal|summary|detailed, responseFormat=json|yaml|markdown)"
3. **get_td_nodes** — "List nodes under a path with token-optimized output (detailLevel+limit supported)"
4. **get_td_node_parameters** — "Get node parameters with concise/detailed formatting (detailLevel+limit supported)"
5. **get_td_node_errors** — "Check node and descendant errors reported by TouchDesigner"
6. **create_td_node** — "Create a new node in TouchDesigner"
7. **update_td_node_parameters** — "Update parameters of a specific node in TouchDesigner"
8. **delete_td_node** — "Delete an existing node in TouchDesigner"
9. **exec_node_method** — "Execute a method on a specific node in TouchDesigner"
10. **get_td_classes** — "List TouchDesigner Python classes/modules (detailLevel+limit supported)"
11. **get_td_class_details** — "Get information about a TouchDesigner class/module (detailLevel+limit supported)"
12. **get_td_module_help** — "Retrieve Python help() text for a TouchDesigner module or class"
13. **get_top_image** — "Capture the current output of a TOP node as an image so it can be viewed directly (maxSize optionally downscales the longer side)"
14. **describe_td_tools** — "Generate a filesystem-oriented manifest of available TouchDesigner tools"

### Steering markers
No description contains compulsion markers (no "instead of", "primary", "prefer", "MUST use", "takes precedence", "Best for", superlatives). The descriptions are dry, functional. The only external text is `errorComment: "Check reference resources: https://docs.derivative.ca/Python_Classes_and_Modules"`, added only in error messages, not in descriptions.

## CHANNEL: prompts, npm (static) — additional observation
3 MCP prompts are registered (`Check node errors`, `Node connection`, `Search node`) in `dist/features/prompts/handlers/td_prompts.js` — user prompt templates, called explicitly by the client, and they do not carry steering risk in the style of "hidden instructions to the server" (not checked line by line for markers, but this is an opt-in channel).

## NOTES
- The code is NOT minified: tsc output with preserved comments and JSDoc, reads like source.
- Risk of dynamic construction of descriptions: low. Descriptions are literals in TOOL_DEFINITIONS; the only concatenation is REFERENCE_COMMENT (documentation URL) and even that only in the error path.
- Reviewed: ~101 files in the package (full listing), read line by line 5 key ones (touchDesignerServer.js, toolDefinitions.js, register.js, tdTools.js, constants.js) + grep across all dist for "instructions".
- capability `prompts` is declared; `resources` are not registered.
