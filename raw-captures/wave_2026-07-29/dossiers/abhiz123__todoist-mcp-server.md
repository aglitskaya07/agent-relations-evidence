# UNIT: @abhiz123/todoist-mcp-server | npm v0.1.0 (published 2024-12-04T00:06:57.078Z) | frames: pulsemcp | captured 2026-07-29 (static, tarball)

## VERDICT: MCP server

Full stdio MCP server: `new Server({name: "todoist-mcp-server", version: "0.1.0"}, {capabilities: {tools: {}}})` from `@modelcontextprotocol/sdk` 0.5.0, transport `StdioServerTransport`, wrapper over Todoist REST API (`@doist/todoist-api-typescript`). The only code file: `package/dist/index.js` (333 lines, compiled by tsc, not minified).

## CHANNEL: instructions, npm (static)
(not found statically)

Only `name`/`version` and `capabilities: {tools: {}}` are passed to the Server constructor — there is no `instructions` field anywhere in the package.

## CHANNEL: tool descriptions, npm (static, coverage=full)

5 tools, all descriptions verbatim:

1. **todoist_create_task** — "Create a new task in Todoist with optional description, due date, and priority"
   - content: "The content/title of the task"
   - description: "Detailed description of the task (optional)"
   - due_string: "Natural language due date like 'tomorrow', 'next Monday', 'Jan 23' (optional)"
   - priority: "Task priority from 1 (normal) to 4 (urgent) (optional)"

2. **todoist_get_tasks** — "Get a list of tasks from Todoist with various filters"
   - project_id: "Filter tasks by project ID (optional)"
   - filter: "Natural language filter like 'today', 'tomorrow', 'next week', 'priority 1', 'overdue' (optional)"
   - priority: "Filter by priority level (1-4) (optional)"
   - limit: "Maximum number of tasks to return (optional)"

3. **todoist_update_task** — "Update an existing task in Todoist by searching for it by name and then updating it"
   - task_name: "Name/content of the task to search for and update"
   - content: "New content/title for the task (optional)"
   - description: "New description for the task (optional)"
   - due_string: "New due date in natural language like 'tomorrow', 'next Monday' (optional)"
   - priority: "New priority level from 1 (normal) to 4 (urgent) (optional)"

4. **todoist_delete_task** — "Delete a task from Todoist by searching for it by name"
   - task_name: "Name/content of the task to search for and delete"

5. **todoist_complete_task** — "Mark a task as complete by searching for it by name"
   - task_name: "Name/content of the task to search for and complete"

Marker scan of steering patterns (instead of built-in, most powerful, always default, precedence, LAST resort, MUST use, primary, prefer, Perfect for, etc.): 0 matches. The descriptions are purely functional, with no attempts to direct the agent's priorities.

## NOTES

- The code is not minified (ordinary tsc output with comments).
- All description strings are static literals in constant objects; there is no risk of dynamic string construction (no concatenation/templates in definitions, no fetching of external texts).
- There are 5 files in the package: LICENSE, README.md, package.json, dist/index.js, dist/index.d.ts. dist/index.js (entire file) and package.json were examined; README is marketing text and contains no server text (not an instructions channel).
- Behavioral feature (not steering, but noticeable): update/delete/complete look up the task by substring match on the name without confirmation — risk of deleting/closing the wrong task when the name is ambiguous.
