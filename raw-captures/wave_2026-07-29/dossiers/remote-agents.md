# UNIT: remote-agents | npm v0.1.37 (published 2026-07-12T11:24:48.243Z) | scope: pulsemcp | captured 2026-07-29 (static, tarball)

## VERDICT: server exists, but NOT in the tarball (binary-download launcher)

The product is indeed an MCP server (“Unified MCP server for controlling fleets of remote machines”, mode `remote-agents mcp` = MCP stdio server). But the npm tarball contains only:

- `run.js` — launcher: `spawn(./bin/remote-agent, argv, {stdio:"inherit"})` + notify-only update checks via registry.npmjs.org
- `install.js` — postinstall: downloads the precompiled Rust binary `remote-agent-<triple>` from `https://github.com/47-ronn/tunshell_mcp_agents/releases/download/v0.1.37/...` (SHA-256 sidecar verification, but the sidecar may be absent — then skip)
- `README.md`, `package.json`, `LICENSE`

All server-side MCP code (tool registration, instructions, schemas) is inside the downloadable native binary (Rust, `crates/mcp-server` per README). It is not in the tarball; static extraction of model-control channels from this artifact is impossible.

## CHANNEL: instructions, npm (static)
(not found statically — server code is absent from the tarball; instructions, if present, are compiled into a Rust binary)

## CHANNEL: tool descriptions, npm (static, coverage=none)
The factual description strings for the tools are not extractable (in the binary). For context, the README documents 28 tools (this is DOCUMENTATION, not runtime descriptions):
`exec`, `read_file`, `write_file`, `list_dir`, `get_info`, `set_mode`, `git_status`, `git_pull`, `git_commit`, `git_push`, `schedule_add`, `schedule_remove`, `schedule_list`, `task_dispatch`, `task_get`, `task_list`, `task_wait`, `list_agents`, `fleet_exec`, `fleet_read`, `fleet_write`, `fleet_git`, `fleet_search`, `file_search`, `file_stat`, `send_file`, `transfer_get`, `sync_dir`, `tunnel_start`, `tunnel_list`, `tunnel_stop`, `mapreduce`.
The README tone is neutrally technical; a marker scan of the README for stirring regexes found no matches (no "primary", "takes precedence", "instead of built-in", etc.).

## SECURITY / SUPPLY-CHAIN NOTES
- Postinstall network fetch of an executable binary from GitHub Releases — a classic supply-chain vector: release contents can change independently of the npm publication (the checksum sidecar sits next to the binary in the same release, so it protects against corruption, not release tampering).
- The product itself is intended for remote execution of commands/files/cron/tunnels on a fleet of machines through relay; `bypass` mode = unrestricted.
- The tarball code is not minified, readable, with no dynamic string construction; but this is only a wrapper.
- Files examined: 5 out of 5 (entire tarball).
