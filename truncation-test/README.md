# How much MCP server text reaches the agent in Claude Code — 13.10.2026

The stand server [`stub_long.py`](stub_long.py) (no dependencies) serves an `instructions` block and a description of the tool `long_tool`, each 30,000 characters long. Every 1,000 characters there is a random marker of the form `[I-NN-XXXXX]` or `[T-NN-XXXXX]`; the codes are in [`codes.json`](codes.json). The agent is asked to list the markers it sees verbatim. The codes cannot be guessed, so the last marker named shows where the client truncated the text.

Client: Claude Code 2.1.292, `claude -p` with `--mcp-config mcp.json --strict-mcp-config`, no user servers. ([`mcp.json`](mcp.json) points to `stub_long.py` by a relative path, so run it from this folder.)

| Run | Channel | What the agent saw | Truncation |
|---|---|---|---|
| [`run1_no_load.txt`](run1_no_load.txt) (tools loaded immediately) | instructions | I-01, I-02, I-03, then `This paragraph is neutral filler te… [truncated]` | at character 2,048 |
| | long_tool description | T-01, T-02, T-03, then `… [truncated]` | at character 2,048 |
| [`run2_toolsearch.txt`](run2_toolsearch.txt) (`ENABLE_TOOL_SEARCH=true`: the tool is deferred and loaded via ToolSearch) | long_tool description | T-01, T-02, T-03, then `… [truncated]` | at character 2,048 |

All markers named matched `codes.json`. Not a single invented one; the fourth (`I-04-M25JC`, `T-04-KXPL6`) was never named.

## Conclusion

In Claude Code 2.1.292 no more than **2,048 characters** reach the agent, both from the instructions block and from the description of each tool. With lazy loading via ToolSearch the limit is the same. The tail is cut off, the agent sees a `[truncated]` marker, the user sees nothing.

For AnySite this means: of its 24,652 characters of instructions, the first ~2,000 get through, and the duplicate in the `discover` description is also truncated to ~2,000. In both cases the surviving beginning is the PRECEDENCE block. The list of 565 sources does not reach the agent in Claude Code through either channel.

## Limitations

- One client of one version was tested. Other clients and other versions of Claude Code were not measured.
- The agent itself reports what it sees. This is self-report, but the markers are random, and the match with `codes.json` was checked.
