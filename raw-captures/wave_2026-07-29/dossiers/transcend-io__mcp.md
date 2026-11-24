# UNIT: @transcend-io/mcp | npm v0.6.11 (published 2026-07-22T19:12:03.008Z) | scope: npm-top,smithery-top20 | captured 2026-07-29 (static, tarball)

## VERDICT: MCP server (umbrella aggregator)

Yes, this is an MCP server: `dist/cli.mjs` creates `ToolRegistry`, calls `buildMcpServer({name: "transcend-mcp", version, instructions, tools})` from `@transcend-io/mcp-server-base` and attaches `StdioServerTransport` (or HTTP mode via `runMcpHttp`). However the tarball is a thin wrapper: the tools themselves (descriptions, schemas, handlers) are imported from 9 external dependency packages (`@transcend-io/mcp-server-{admin,assessment,base,consent,discovery,docs,dsr,inventory,preferences,workflows}`), which are NOT in the tarball (no node_modules, no bundled code for them).

## CHANNEL: instructions, npm (static, 322 chars)

Found in `dist/cli.mjs` (constant `UMBRELLA_DOCS_SERVER_INSTRUCTIONS`, passed to `buildMcpServer` as `instructions`), verbatim:

> For how-to, product concepts, setup guides, or "what is X" questions about Transcend (e.g. airgap, consent, DSR): (1) call docs_list with a keyword, (2) call docs_fetch on the best matching URL, (3) answer from that content. API tools return data from the signed-in organization; they do not replace product documentation.

Comment: soft steering — prescribes a three-step workflow (docs_list → docs_fetch → answer from that content) for product questions; without "primary/precedence/last resort" rhetoric.

## CHANNEL: tool descriptions, npm (static, coverage=none)

(not statically extractable from this tarball)

- README states: "access to all 73 Transcend tools at once".
- Registration: `dist/oauth-scopes-uzulgUw_.mjs` → `ToolRegistry.registerAllTools()` calls `getDocsTools`, `getDSRTools`, `getConsentTools`, `getPreferenceTools`, `getInventoryTools`, `getDiscoveryTools`, `getAssessmentTools`, `getWorkflowTools`, `getAdminTools` — all from external npm packages.
- There is no tool description line in the tarball (checked dist/*.mjs, *.map, *.d.mts, README). Names known from the code/README: `docs_list`, `docs_fetch` (mentioned in instructions).
- For full coverage of descriptions, tarballs of 9 domain packages @transcend-io/mcp-server-* are needed (versions 0.3.4–0.7.0 are fixed exactly in package.json).

## NOTES

- The code is NOT minified (tsdown bundle with preserved names and comments, source maps attached).
- Risk of dynamic string assembly: low in the tarball itself; instructions are a static literal. The real content of tool descriptions is outside the tarball (supply-chain transfer of surface into dependencies).
- Reviewed files: 7 (package.json, README.md, dist/cli.mjs, dist/index.mjs, dist/oauth-scopes-uzulgUw_.mjs, dist/*.d.mts, *.map via grep).
- Authentication: OAuth (UMBRELLA_OAUTH_SCOPES — merge of scopes from 8 domains) or TRANSCEND_API_KEY; deep links in tool responses to app.transcend.io.
