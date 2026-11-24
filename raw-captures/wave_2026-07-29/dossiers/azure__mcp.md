# UNIT: @azure/mcp | npm v3.0.0-beta.30 (published 2026-07-28T18:30:16.996Z) | frames: npm-top,smithery-top20 | captured 2026-07-29 (static, tarball)

## VERDICT: server, but binary-wrapper — payload is not in tarball

This is the official Azure MCP Server (Microsoft, `mcpName: com.microsoft/azure`), i.e. in essence an MCP server, NOT an SDK/client. But the npm tarball `@azure/mcp` is a thin launcher wrapper (4 files: `index.js` 3.7 KB, `package.json`, `scripts/post-install-script.js`, `README.md`, LICENSE). `index.js` only does `require('@azure/mcp-<platform>-<arch>')` (six optionalDependencies: linux/darwin/win32 × x64/arm64) and calls `platformPackage.runExecutable(process.argv.slice(2))`. The real server is a compiled .NET binary in the platform packages, which are not present in the analyzed source. If the platform package is absent, the launcher itself runs `npm install <platformPackageName>@<version>` (execSync, with fallback `--no-save --prefer-online`) — supply-chain-notable behavior, but not steering.

## CHANNEL: instructions, npm (static)
(not found statically) — the tarball contains neither the string instructions nor a Server/McpServer constructor: server initialization is entirely inside the .NET binary of the platform package, outside the scope of this unit.

## CHANNEL: tool descriptions, npm (static, coverage=none)
(not statically extractable) — there are no tool registrations (registerTool/addTool/server.tool/schema) in the tarball; README claims "40+ different Azure services", but the tool name+description values themselves are embedded in the compiled binary. Marker-scan of README.md (35 KB) against all regexes in the string dictionary — zero matches; README is neutral (setup instructions, client configuration tables, Permissions and Risk / Data Collection / Compliance sections).

## NOTES
- The code is not minified, readable; 5 files were reviewed (all package files).
- There is no dynamic construction of strings instructions/descriptions in JS — they are not present in JS at all.
- For full coverage of tool descriptions, a separate unit is needed for the platform package (for example `@azure/mcp-darwin-arm64`) with extraction of strings from a .NET binary, or a dynamic stand.
- Risk note (not steering): auto-install via execSync npm on first run — the code fetches and executes the platform package of the same version from the registry.
