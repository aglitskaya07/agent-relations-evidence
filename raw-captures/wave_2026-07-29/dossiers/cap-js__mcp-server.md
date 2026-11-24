# UNIT: @cap-js/mcp-server | npm v0.0.5 (published 2026-04-27T10:04:39.260Z) | frames: npm-top | captured 2026-07-29 (static, tarball)

Verdict: a full MCP server (SAP SE, official for CAP/CDS). `lib/run.js` creates `new McpServer({ name: 'cds-mcp', version: '0.1.0' })` from `@modelcontextprotocol/sdk`, connects `StdioServerTransport`, and registers tools via `server.registerTool`. It is also distributed as a Claude plugin (`.claude-plugin/plugin.json`, `.mcp.json`).

## CHANNEL: instructions, npm (static)
(not found statically)

Only `{ name: 'cds-mcp', version: '0.1.0' }` is passed to the `McpServer` constructor — there is no `instructions` field. Grep for `instructions` in all .js/.json files in the package — zero matches.

## CHANNEL: tool descriptions, npm (static, coverage=full)

A total of 2 tools (the only registry is the `tools` object in `lib/tools.js`, registration by loop in `lib/run.js:21`).

### 1. search_model
- title: `Search for CDS definitions`
- description (verbatim): `Returns CDS model definitions (CSN), including elements, annotations, parameters, file locations and HTTP endpoints. Useful for building queries, OData URLs, or modifying models.`
- annotations: readOnlyHint: true, destructiveHint: false, idempotentHint: false
- parameters (descriptions verbatim):
  - `projectPath` (string): `Root path of the project`
  - `name` (string, optional): `Definition name (fuzzy search; no regex or special characters)`
  - `kind` (string, optional): `Definition kind to filter by (e.g., service, entity, action)`
  - `topN` (number, default 1): `Maximum number of results`
  - `namesOnly` (boolean, default false): `If true, only return definition names (for overview)`

### 2. search_docs
- title: `Search in CAP Documentation`
- description (verbatim): `Searches code snippets of CAP documentation for the given query. You MUST use this tool if you're unsure about CAP APIs for CDS, Node.js or Java. Optionally returns only code blocks.`
- annotations: readOnlyHint: true, destructiveHint: false, idempotentHint: true
- parameters (descriptions verbatim):
  - `query` (string): `Search string`
  - `maxResults` (number, default 10): `Maximum number of results`

### Steering markers
- search_docs: match on the marker `MUST (use|run|be executed)` — "**You MUST use this tool** if you're unsure about CAP APIs for CDS, Node.js or Java". A moderate imperative, the scope is limited to the CAP domain (it does not claim to replace the agent's general tools). There are no other markers (precedence/primary/instead of/last resort, etc.).

## NOTES
- The code is not minified: readable ES module source (index.js + 7 files in lib/), 15 files total in the package; index.js, lib/run.js, lib/tools.js were reviewed in full + grep across all .js/.json, manifest.json, .mcp.json, .claude-plugin/plugin.json, package.json.
- Risk of dynamic string assembly: low — tool descriptions are stored as literals in `lib/tools.js`, the only dynamic part is registration by the `for (const t in tools)` loop over a static object.
- Auxiliary files (searchMarkdownDocs.js, calculateEmbeddings.js, embeddings.js, getModel.js, fuzzyTopN.js) — implementation of local embedding search over docs (onnxruntime-web) and loading of the project's CSN model; they contain no texts for the LLM (per grep).
- Downloads embeddings/model from the network when `--download` is used (searchMarkdownDocs.downloadEmbeddings, forceDownloadModel) — content for docs, not instructions to the agent; statically it does not affect the steering channel.
