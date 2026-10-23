#!/usr/bin/env python3
"""Test stand: how much MCP server text reaches the agent in Claude Code (13.10.2026).
The instructions block and the long_tool description are ~30,000 characters each; every ~1,000 characters
there is a random marker. The agent lists the markers it sees; the last visible
marker shows where the client truncated the text. No dependencies, stdio JSON-RPC."""
import json, os, sys

FILL = ("This paragraph is neutral filler text used only to measure length. It describes nothing and asks "
        "for nothing. The weather is mild, the river is calm, and the library opens at nine. ")

def build(prefix, codes, seg=1000):
    parts = []
    for i, c in enumerate(codes, 1):
        head = f"[{prefix}-{i:02d}-{c}] "
        body = (FILL * 20)[: seg - len(head)]
        parts.append(head + body)
    return "".join(parts)

CODES = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "codes.json")))
INSTR = build("I", CODES["I"])
DESC = build("T", CODES["T"])

def out(o):
    sys.stdout.write(json.dumps(o) + "\n"); sys.stdout.flush()

for line in sys.stdin:
    line = line.strip()
    if not line: continue
    try: req = json.loads(line)
    except Exception: continue
    m, rid = req.get("method"), req.get("id")
    if m == "initialize":
        out({"jsonrpc": "2.0", "id": rid, "result": {"protocolVersion": "2025-06-18",
             "capabilities": {"tools": {}}, "serverInfo": {"name": "lengthprobe", "version": "0.1"},
             "instructions": INSTR}})
    elif m == "tools/list":
        out({"jsonrpc": "2.0", "id": rid, "result": {"tools": [
            {"name": "long_tool", "description": DESC,
             "inputSchema": {"type": "object", "properties": {"q": {"type": "string"}}}},
            {"name": "short_tool", "description": "Returns the current time.",
             "inputSchema": {"type": "object", "properties": {}}}]}})
    elif m == "tools/call":
        out({"jsonrpc": "2.0", "id": rid, "result": {"content": [{"type": "text", "text": "ok"}]}})
    elif rid is not None:
        out({"jsonrpc": "2.0", "id": rid, "result": {}})
