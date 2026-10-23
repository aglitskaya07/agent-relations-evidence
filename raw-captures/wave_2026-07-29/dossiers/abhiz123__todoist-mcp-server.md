# UNIT: @abhiz123/todoist-mcp-server | npm v0.1.0 (published 2024-12-04T00:06:57.078Z) | рамки: pulsemcp | captured 2026-07-29 (static, tarball)

## VERDICT: MCP server

Полноценный stdio MCP-сервер: `new Server({name: "todoist-mcp-server", version: "0.1.0"}, {capabilities: {tools: {}}})` из `@modelcontextprotocol/sdk` 0.5.0, транспорт `StdioServerTransport`, обёртка над Todoist REST API (`@doist/todoist-api-typescript`). Единственный файл кода: `package/dist/index.js` (333 строки, скомпилированный tsc, не минифицирован).

## CHANNEL: instructions, npm (static)
(не обнаружены статически)

Конструктору Server передаются только `name`/`version` и `capabilities: {tools: {}}` — поля `instructions` нет нигде в пакете.

## CHANNEL: tool descriptions, npm (static, coverage=full)

5 инструментов, все описания дословно:

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

Маркер-скан steering-паттернов (instead of built-in, most powerful, always default, precedence, LAST resort, MUST use, primary, prefer, Perfect for и т.д.): 0 совпадений. Описания чисто функциональные, без попыток управлять приоритетами агента.

## NOTES

- Код не минифицирован (обычный tsc-вывод с комментариями).
- Все строки описаний — статические литералы в объектах-константах; риска динамической сборки строк нет (нет конкатенации/шаблонов в definitions, нет fetch внешних текстов).
- Файлов в пакете 5: LICENSE, README.md, package.json, dist/index.js, dist/index.d.ts. Просмотрены dist/index.js (весь) и package.json; README — маркетинговый, серверного текста не содержит (не канал instructions).
- Особенность поведения (не steering, но заметно): update/delete/complete ищут задачу по substring-совпадению имени без подтверждения — риск удаления/закрытия не той задачи при неоднозначном имени.
