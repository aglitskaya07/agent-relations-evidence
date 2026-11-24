# UNIT: @abhaybabbar/retellai-mcp-server | npm v1.0.4 (published 2026-04-09T22:28:23.696Z) | frames: pulsemcp | captured 2026-07-29 (static, tarball)

## VERDICT: MCP server

A real TypeScript MCP server: `src/index.ts` creates `new McpServer({ name: "Retell MCP", version: "0.1.0" })` from `@modelcontextprotocol/sdk`, connects `StdioServerTransport`, registers tools via `registerAllTools`. A wrapper over the Retell AI API (voice agents/calls), key `RETELL_API_KEY` from env.

## CHANNEL: instructions, npm (static)
(not found statically)

Only `name` and `version` are passed to the `McpServer` constructor; grep for `instructions` in `src/` and `build/` — 0 matches.

## CHANNEL: tool descriptions, npm (static, coverage=full)

24 tools, all are registered as `server.tool(name, description, schema, handler)`. Descriptions verbatim:

### call.ts (6)
1. `create_phone_call` — "Creates a new phone call"
2. `create_web_call` — "Creates a new web call"
3. `get_call` — "Gets a call by ID"
4. `list_calls` — "Lists all calls"
5. `update_call` — "Updates an existing call"
6. `delete_call` — "Deletes a call"

### agent.ts (6)
7. `list_agents` — "Lists all Retell agents"
8. `create_agent` — "Creates a new Retell agent"
9. `get_agent` — "Gets a Retell agent by ID"
10. `update_agent` — "Updates an existing Retell agent"
11. `delete_agent` — "Deletes a Retell agent"
12. `get_agent_versions` — "Gets all versions of a Retell agent"

### retell-llm.ts (5)
13. `list_retell_llms` — "Lists all Retell LLMs"
14. `create_retell_llm` — "Creates a new Retell LLM"
15. `get_retell_llm` — "Gets a Retell LLM by ID"
16. `update_retell_llm` — "Updates an existing Retell LLM"
17. `delete_retell_llm` — "Deletes a Retell LLM"

### phone-number.ts (5)
18. `list_phone_numbers` — "Lists all Retell phone numbers"
19. `create_phone_number` — "Creates a new phone number"
20. `get_phone_number` — "Gets details of a specific phone number"
21. `update_phone_number` — "Updates a phone number"
22. `delete_phone_number` — "Deletes a phone number"

### voice.ts (2)
23. `list_voices` — "Lists all available Retell voices"
24. `get_voice` — "Gets details of a specific voice"

## MARKER SCAN

No description contains steering markers (instead of / prefer / MUST / primary / precedence / whenever the user, etc.). All descriptions are neutral CRUD one-liners.

## NOTES

- The code is not minified: the tarball contains both src/*.ts and build/*.js (readable tsc output); build mirrors src, the number of registrations matches (24/24).
- Risk of dynamic assembly of description strings: low — all names and descriptions are specified as string literals directly in `server.tool(...)` calls.
- A nested tarball of the previous version `abhaybabbar-retellai-mcp-server-1.0.3.tgz` is in the package/ root (not analyzed as a separate unit, not executed).
- Reviewed ~12 text files (package.json, README.md, src/index.ts, src/client.ts, src/tools/*.ts ×7, plus grep across build/ ×9).
- Metadata mismatch: package.json version 1.0.4, but version "0.1.0" is hardcoded into the McpServer constructor.
