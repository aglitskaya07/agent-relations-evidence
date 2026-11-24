# UNIT: zapier | Zapier | github zapier/zapier-mcp | author type: official | captured 2026-07-29 (static source)

## NOT-A-SERVER

The repository `zapier/zapier-mcp` does not contain an MCP server implementation. It is a distribution of a client plugin / configuration for Zapier's hosted closed server.

Justification (all 24 repository files were reviewed; there is no source code at all — no .ts, no .py, no .go, only .md/.json/.svg/.mdc/.txt):

- `llms.txt` (verbatim): "This repository contains per-client plugin manifests, install assets, skills, and rules. It does **not** contain the MCP server implementation — the server is hosted at `mcp.zapier.com/api/v1/connect` and is closed source."
- `AGENTS.md` (verbatim): "**The MCP server itself is hosted at `mcp.zapier.com`** — it's not in this repo. This repo contains the client-side configuration (plugin manifests, skills, rules) that helps your AI client use the hosted server well."
- All manifests declare only remote transport, without an entrypoint process:
  - `plugins/zapier/.mcp.json` and `zapier-power/mcp.json`: `{"mcpServers": {"zapier": {"type": "http", "url": "https://mcp.zapier.com/api/v1/connect"}}}`
  - `gemini-extension.json`: `"httpUrl": "https://mcp.zapier.com/api/v1/connect"` + `"oauth": {"enabled": true}`
- Repository contents: README/AGENTS/CLAUDE/CONTRIBUTING/LICENSE/llms.txt, per-client plugin.json (Claude Code, Codex, Cursor, GitHub Copilot CLI), brand assets (icon.svg, logo.svg), rule `plugins/zapier/rules/zapier-lifecycle.mdc`, agent persona `plugins/zapier/agents/zapier-mcp.agent.md`, four skills (`zapier-onboard`, `zapier-demo`, `zapier-explore`, `zapier-status`) and `zapier-power/POWER.md` + `zapier-power/steering/*.md` (copies of the same skills for Kiro Powers).

Important for interpretation: steering in this unit exists, but it lives not in the protocol channels, but on the client side (skills/rules/agent persona), so there is nothing statically measurable in the `instructions` and `tool descriptions` channels.

## CHANNEL: instructions
(not found statically)

Neither a server constructor (`Server`/`McpServer`/`FastMCP`/`mcp.server`/`createServer`) nor an `initialize` response exists in the repository — the server code is closed. The only occurrences of the word "instructions" refer to user instructions for installing/restarting the client inside skills.

## CHANNEL: tool descriptions (coverage=none)

There are no tool definitions in the repository: neither `registerTool`, nor `addTool`, nor `server.tool(`, nor `@mcp.tool`, nor `Tool{...Description}`, nor static lists of tool definitions. The set of tools is formed dynamically by the hosted server based on the actions that the user has enabled in their Zapier account (per README — "9,000+ apps and 40,000+ actions"), and is not statically available.
