# UNIT: @ui5/mcp-server | npm v0.2.17 (published 2026-07-27T11:08:36.651Z) | scope: npm-top | captured 2026-07-29 (static, tarball)

Type: full MCP server (`McpServer` from `@modelcontextprotocol/sdk`, stdio transport, `lib/server.js`). Official SAP UI5 tooling server.

## CHANNEL: instructions, npm (static)
(not found statically)

The constructor `new McpServer({name: "UI5", version: PKG_VERSION}, {capabilities: {tools: {}}})` — the `instructions` parameter is not passed. Grep for `instructions` in lib/ gives only a fragment of the description of the tool get_typescript_conversion_guidelines.

## CHANNEL: tool descriptions, npm (static, coverage=full)

10 tools, registration through the `registerTool` wrapper → `server.registerTool` (`lib/registerTools.js`). The registration order is intentional: the comment in the code is — "The guidelines tool should be registered first to ensure it is displayed first in MCP clients."

1. **get_guidelines** — "This tool MUST be called once to retrieve UI5 guidelines before working on any UI5 (SAPUI5/OpenUI5) related task or project or creating a UI5 project. The guidelines provided by this tool MUST be followed to ensure best practices and avoid common pitfalls in UI5 development."

2. **run_ui5_linter** — "Run UI5 linter on a UI5 project to find and optionally fix UI5 related problems like the usage of deprecated API. After making changes, you should always run the linter again to verify that no new problems have been introduced."

3. **get_api_reference** — "Search the UI5 API reference for module names and symbols"

4. **get_project_info** — "Get general information about a local UI5 project."

5. **create_ui5_app** — "Create a new basic SAPUI5 application implemented in TypeScript or JavaScript"

6. **get_version_info** — "Get version information for UI5 (OpenUI5 or SAPUI5)"

7. **get_integration_cards_guidelines** — "This tool MUST be called once to retrieve Integration Cards guidelines before working on any Integration Card related task or creating an Integration Card. The guidelines provided by this tool MUST be followed to ensure best practices and avoid common pitfalls in Integration Cards development.Integration Cards are also called 'UI Integration Cards' or 'UI5 Integration Cards'."

8. **create_integration_card** — "Create a new Integration Card, UI Integration Card, or UI5 Integration Card"

9. **run_manifest_validation** — "Validates UI5 manifest file. After making changes, you should always run the validation again to verify that no new problems have been introduced."

10. **get_typescript_conversion_guidelines** — "This tool MUST be called once before converting a UI5 (SAPUI5/OpenUI5) project from JavaScript to TypeScript. The instructions provided by this tool MUST be followed to ensure that the project setup and code is correctly converted."

### Steering markers
- "MUST be called once … MUST be followed" — in three guidelines tools (get_guidelines, get_integration_cards_guidelines, get_typescript_conversion_guidelines). Imperative, but scoped: only for UI5 tasks, does not claim priority over other servers/built-in tools.
- "you should always run the … again" — run_ui5_linter, run_manifest_validation (self-check loop).
- There are no markers of displacing competitors ("instead of built-in", "takes precedence", "LAST resort", "primary", "faster and cheaper", etc.) — none.

## NOTES
- Code is NOT minified: transpiled TypeScript (ESM) with sourcemaps and .d.ts, reads freely.
- All descriptions are static string literals/concatenations of string literals; there is no risk of dynamic description assembly. Dynamic content exists only in the responses of guidelines tools (text is pulled from lib/resources and tools/*/guidelines.js at runtime — this does not affect the descriptions channel).
- Reviewed: lib/server.js, lib/registerTools.js, all 10 tools/*/index.js in full; grep for "instructions" across all lib/ (77 JS files without sourcemaps in the package).
