# UNIT: sonic-pi-mcp | npm v2.0.0 (published 2026-03-22T13:04:10.009Z) | scope: pulsemcp | captured 2026-07-29 (static, tarball)

Type: full MCP server (stdio). `McpServer` from `@modelcontextprotocol/sdk`, transport `StdioServerTransport`, sends Sonic Pi Ruby code via OSC to 127.0.0.1:4560. The only server file is `dist/server.mjs` (bundle from `src/server.ts`, readable, not minified); `bin/cli.mjs` is a thin import wrapper.

## CHANNEL: instructions, npm (static)
(not found statically)

Constructor: `new McpServer({ name: "Sonic Pi MCP", version: SERVER_VERSION })` — the `instructions` field is absent (dist/server.mjs:116-119).

Note: steering content goes through other channels —
- MCP resource `dj-session-guide` (`sonicpi://v2/dj-session`): markdown guide `DJ_SESSION_GUIDE` (~2.9k chars), defining the role "You are a **live DJ** using Sonic Pi", instrument preferences ("**queue_segment** — Push the **next** DJ segment (primary)", "stop_all — … use sparingly") and code-writing rules.
- MCP prompt `next_performance_segment`: "Frame the next Sonic Pi code block for a long NL DJ session (taste, arc, transitions)." — the prompt text instructs: "Read resource sonicpi://v2/dj-session if available. … Respond with valid Sonic Pi Ruby for the next segment, then call queue_segment with that code."

## CHANNEL: tool descriptions, npm (static, coverage=full)

4 tools (dist/server.mjs:178-225), verbatim:

1. **queue_segment** — "Push the next music segment to Sonic Pi. Use with the v2 DJ session runner for crossfaded handoffs. Prefer this over ad-hoc snippets for long sets."
   - param `code`: "Full Sonic Pi (Ruby) source for the next segment. Use named live_loops; prefer use_bpm when tempo matters."
2. **run_code** — "Alias of queue_segment for compatibility. Sends Sonic Pi code over OSC to the session runner."
3. **stop_all** — "Hard stop: stop all running Sonic Pi jobs (like the Stop button). Use sparingly; prefer queue_segment for musical transitions."
4. **play_note** — "Play a single test note (quick sanity check). Not for full DJ segments—use queue_segment for those."
   - params: `note` "MIDI note number (0-127)", `synth` "Synth name (e.g. :beep, :saw, :prophet)", `sustain` "Note length in seconds", `cutoff` "Filter cutoff frequency"

Steering markers in the descriptions: "Prefer this over ad-hoc snippets" (queue_segment), "prefer queue_segment" (stop_all, play_note) — intra-package routing between its own tools, not displacing another tool.

## NOTES
- Code is not minified (bun bundle with preserved names and comment `// src/server.ts`).
- There is no dynamic construction of description strings: all description/instructions strings are static literals; the only dynamic part is env variables OSC_HOST/OSC_PORT/OSC_CODE_PATH/OSC_STOP_ALL_PATH (OSC addressing, not text for the model).
- Reviewed files: 4 of 6 (package.json, dist/server.mjs in full, bin/cli.mjs, listing; README.md and sonic-pi-queue.rb are not included in the instructions/tool-descriptions channels).
- Risk: tools forward arbitrary Ruby code to Sonic Pi (eval on the Sonic Pi side); the guide itself warns "Do not call OS/shell from code", but there is no technical restriction.
