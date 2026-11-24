# UNIT: awslabs | AWS (core) | github awslabs/mcp/src/core-mcp-server | author type: official | captured 2026-07-29 (static source)

## PATH MISSING

The target directory of the unit `src/core-mcp-server` is absent in the repository snapshot.

Checked:
- The snapshot root exists: `scratch/brands/src/awslabs/mcp-HEAD` (there is `src/` with ~60 other servers: aws-api-mcp-server, cloudwatch-mcp-server, dynamodb-mcp-server, etc.).
- `src/core-mcp-server` — does not exist (`find` returns the error "No such file or directory").
- Grep across the entire snapshot for `core-mcp-server` yields only mentions: `README.md` (JSON config examples left over from the old version), `docs/migration-core.md`, `.github/CODEOWNERS`, issue templates, `docusaurus/sidebars.ts`, `.secrets.baseline`. Not a single server source file.
- Grep for `prompt_understanding` (the only custom tool of this server) gives a single match — `docs/migration-core.md`, that is, the description text, not code.

Reason recorded in the repository itself (`docs/migration-core.md`, verbatim):

> This guide helps you migrate from `awslabs.core-mcp-server` to configuring individual MCP servers directly in your client.

> The `core-mcp-server` was designed as a proxy that bundles 45+ MCP servers behind role-based environment variables. While useful early on, it has several issues:
>
> - **Modern MCP clients handle multi-server configs natively** — Kiro, Cursor, and VS Code all support configuring multiple MCP servers directly, making the proxy pattern unnecessary
> - **Massive dependency footprint** — Installing core-mcp-server pulls in every bundled server, causing slow installs and build failures (e.g., cassandra-driver compilation issues)
> - **Tool name overflow** — Proxied tool names with prefixes can exceed the 64-character API limit in some clients
> - **Bundles deprecated servers** — Several servers included in the core bundle have been deprecated

> The core server's only unique tool, `prompt_understanding`, returns a static Markdown document with AWS architecture guidance. This content can be included directly in your project's CLAUDE.md, `.cursorrules`, or equivalent AI assistant configuration file instead.

Additional note (important for classification, if the unit is replaced): according to the repository description itself, core-mcp-server was a proxy/bundler over other MCP servers with a single in-house tool `prompt_understanding`, so by type it is closer to a proxy than to a substantive server. But there are no sources for static verification in the snapshot, so the verdict is PATH MISSING, not NOT-A-SERVER.

## CHANNEL: instructions
(not found statically — the server source is not in the snapshot)

## CHANNEL: tool descriptions (coverage=none)
(not found statically — the server source is not in the snapshot)
