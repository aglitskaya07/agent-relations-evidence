# UNIT: expo-mcp | npm v0.2.4 (published 2026-02-12T15:15:26.248Z) | scope: npm-top | captured 2026-07-29 (static, tarball)

Publisher: 650 Industries, Inc. (Expo). "Local MCP capabilities provider for Expo" — a stdio MCP server (or composite proxy via MCP tunnel) for local Expo/React Native development: logs, devtools, simulator/emulator automation.

Architecture: `bin/expo-mcp.mjs` → `dist/cli.js` creates `StdioMcpServerProxy` or `CompositeMcpServerProxy` from the external dependency `@expo/mcp-tunnel` (not included in the tarball), then `addMcpCapabilities(server, projectRoot)` registers tools and one prompt (`expo_router_sitemap`, only for expo-router projects).

## CHANNEL: instructions, npm (static)
(not found statically)

Only `tunnelServerUrl / devServerUrl / projectRoot / mcpServerName / mcpServerVersion` are passed to the proxy constructor in `dist/cli.js` — there is no `instructions` field; grep for `instructions` across all of `dist/` — zero matches. Caveat: the actual call to `new McpServer(...)` is inside the non-included dependency `@expo/mcp-tunnel` (~0.2.3); in theory, it may add its own instructions string there — outside the scope of this tarball.

## CHANNEL: tool descriptions, npm (static, coverage=full)

6 tools (1 conditional), all descriptions verbatim:

1. **expo_router_sitemap** (registered only if the project uses expo-router)
   - title: `Query the sitemap of the current expo-router project`
   - description: `Query the all routes of the current expo-router project. This is useful if you were using expo-router and want to know all the routes of the app`

2. **open_devtools**
   - title: `Open devtools`
   - description: `Open the React Native DevTools`

3. **collect_app_logs**
   - title: `Collect app logs`
   - description: `Collect logs from native device (logcat/syslog) or JavaScript console`
   - parameters with descriptions: sources — `Log sources: logcat, syslog, or console.log`; filter — `Regex or string pattern to filter logs. Only logs matching this pattern will be returned`; logLevel — `Log level filter (e.g., error, warn, info, debug). Only logs with this level will be returned`

4. **automation_tap**
   - title: `Tap on device`
   - description: `Tap on the device at the given coordinates (x, y) or by react-native testID. Provide either (x AND y) or testID.`

5. **automation_take_screenshot**
   - title: `Take screenshot of the app`
   - description: `Take screenshot of the full app or a specific view by react-native testID. Optionally provide testID to screenshot a specific view.`

6. **automation_find_view**
   - title: `Find view properties`
   - description: `Find view and dump its properties. This is useful to verify the view is rendered correctly`

Prompt (not a tool): **expo_router_sitemap** — description: `Query the all routes of the current expo-router project using \`expo-router-sitemap\`.`

Steering markers: none. The descriptions are neutral, functional, without "primary/prefer/instead of/MUST" rhetoric. The only soft turns are "This is useful if/to …" (x2), which is a normal context hint, not displacement of competitors.

## NOTES
- Code is NOT minified: plain tsc output with sourcemaps and .d.ts, readable in full.
- All descriptions are static string literals; the risk of dynamic assembly of description strings is zero within the tarball.
- Residual risk: server-level instructions could live in `@expo/mcp-tunnel` (external dependency, not in the tarball).
- Side observation (not steering, but a supply-chain note): the tool and prompt `expo_router_sitemap` when called execute `npx -y expo-router-sitemap@latest` — pulling a fresh package from npm at runtime.
- Reviewed: all 5 JS files of the server logic (index.js, cli.js, mcp/tools.js, mcp/prompts.js, mcp/tools/automation.js) in full + package.json + grep across all dist/ (~30 js/d.ts files); assets/ — binary iOS automation drivers, contain no textual descriptions.
