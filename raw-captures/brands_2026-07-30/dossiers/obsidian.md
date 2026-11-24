# UNIT: obsidian | Obsidian | github docker/mcp-obsidian | author type: community | captured 2026-07-29 (static source)

Confirmation of the MCP server: Python package `mcp_obsidian`, uses `from mcp.server import Server`, creates `app = Server("mcp-obsidian")`, registers `@app.list_tools()` / `@app.call_tool()` and runs via `mcp.server.stdio.stdio_server()` in `src/mcp_obsidian/server.py`. This is a full MCP server (stdio), a wrapper over the Obsidian Local REST API.

## CHANNEL: instructions
(not found statically)

The `Server("mcp-obsidian")` constructor is called only with the name; `app.create_initialization_options()` is called without arguments (server.py:88-92). There is neither `instructions=` nor custom InitializationOptions in the repository. The only occurrences of the word "instructions" are in `openapi.yaml` (description of the PATCH REST endpoint, link to migration documentation), not in the MCP channel.

## CHANNEL: tool descriptions (coverage=full)

Total tools: 12. Definitions — in `src/mcp_obsidian/tools.py` (subclasses of `ToolHandler`, method `get_tool_description()` returns `Tool(name=..., description=...)`). Registration — in `src/mcp_obsidian/server.py:44-55`.

### 1. obsidian_list_files_in_dir
```
Lists all files and directories that exist in a specific Obsidian directory.
```

### 2. obsidian_list_files_in_vault
```
Lists all files and directories in the root directory of your Obsidian vault.
```

### 3. obsidian_get_file_contents
```
Return the content of a single file in your vault.
```

### 4. obsidian_simple_search
```
Simple search for documents matching a specified text query across all files in the vault. 
            Use this tool when you want to do a simple text search
```

### 5. obsidian_patch_content
```
Insert content into an existing note relative to a heading, block reference, or frontmatter field.
```

### 6. obsidian_append_content
```
Append content to a new or existing file in the vault.
```

### 7. obsidian_delete_file
```
Delete a file or directory from the vault.
```

### 8. obsidian_complex_search
```
Complex search for documents using a JsonLogic query. 
           Supports standard JsonLogic operators plus 'glob' and 'regexp' for pattern matching. Results must be non-falsy.

           Use this tool when you want to do a complex search, e.g. for all documents with certain tags etc.
           
```

### 9. obsidian_batch_get_file_contents
```
Return the contents of multiple files in your vault, concatenated with headers.
```

### 10. obsidian_get_periodic_note
```
Get current periodic note for the specified period.
```

### 11. obsidian_get_recent_periodic_notes
```
Get most recent periodic notes for the specified period type.
```

### 12. obsidian_get_recent_changes
```
Get recently modified files in the vault.
```
