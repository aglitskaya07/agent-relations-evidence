# UNIT: @21st-dev/magic | npm v0.2.1 (published 2026-07-24T23:30:24.384Z) | frames: pulsemcp | captured 2026-07-29 (static, tarball)

## NOT-A-SERVER

The package does NOT contain MCP server code. This is a compatibility shim: a thin stdio↔HTTP proxy (dist/index.js, ~6 KB, the only JS file) that reads JSON-RPC line by line from stdin and forwards each message as a POST request to the remote endpoint `https://21st.dev/api/mcp` (overridden by env `MCP_URL_21ST`), adding the `x-api-key` and `mcp-session-id` headers. The code has neither an MCP SDK import nor Server/McpServer/FastMCP/createServer, nor handling of `initialize`, nor tool registrations — the only import is `node:readline`.

Comment in the file header confirms: "Since 0.2.0 it is a thin stdio<->HTTP proxy to the unified 21st MCP endpoint … kept alive because the old install command … is baked into countless agent configs and model memories".

The entire steering surface (instructions, tool descriptions for tools `generate`, `get_inspiration`, `search_logo`, legacy names `21st_magic_component_builder` / `21st_magic_component_inspiration` / `21st_magic_component_refiner` / `logo_search`) lives on the remote 21st.dev server and is not statically available from the tarball. The README states directly: "Connect and call `tools/list` to see the full set".

## CHANNEL: instructions, npm (static)
(not found statically — the server is remote, there is no server constructor in the package)

## CHANNEL: tool descriptions, npm (static, coverage=none)
(not found statically — there are no tool registrations in the package; descriptions are provided by the remote endpoint https://21st.dev/api/mcp)

An indirect steering signal from the README (not a tool description): "The old `/ui`, `/21` trigger phrases were a convention of the legacy tools' descriptions, not the protocol" — that is, in legacy versions the tool descriptions contained trigger phrases, but in this version of the package their text is absent.

## NOTES
- The code is NOT minified (readable tsc output with comments).
- Risk of dynamic construction of strings for descriptions: not applicable locally — all descriptions come from the remote server at runtime, static analysis of the tarball fundamentally cannot see them. This is the main unit's "dynamic" risk: the contents of tools/list can change on 21st.dev's side at any moment.
- Reviewed files: 3 of 3 (package/dist/index.js, package/README.md, package/package.json) — full package walkthrough.
