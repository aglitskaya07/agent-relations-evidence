# UNIT: n8n | n8n | github czlonkowski/n8n-mcp | тип автора: комьюнити | captured 2026-07-29 (static source)

Подтверждение сервера: да, MCP-сервер. `src/mcp/server.ts:250` — `this.server = new Server({ name: 'n8n-documentation-mcp', version: PROJECT_VERSION, ... }, { capabilities: { tools: {}, resources: {} } })` из `@modelcontextprotocol/sdk`; транспорты stdio (`src/mcp/stdio-wrapper.ts`) и HTTP (`src/http-server.ts`, `src/http-server-single-session.ts`).

## CHANNEL: instructions
(не обнаружены статически)

Конструктор `new Server(...)` получает только `name`/`version`/`icons`/`websiteUrl` и `capabilities`; поля `instructions` нет. Ручной обработчик `InitializeRequestSchema` (`src/mcp/server.ts:758-803`) возвращает ответ ровно из `protocolVersion`, `capabilities`, `serverInfo` — без `instructions`. То же в HTTP-путях (`src/http-server.ts:397-411`, `src/http-server-single-session.ts:~1098`).

## CHANNEL: tool descriptions (coverage=full)

Всего 24 инструмента: 7 документационных (`src/mcp/tools.ts`, массив `n8nDocumentationToolsFinal`) + 17 управляющих (`src/mcp/tools-n8n-manager.ts`, массив `n8nManagementTools`, добавляются, если сконфигурирован n8n API / включён multi-tenant).

### Документационные инструменты (src/mcp/tools.ts)

**tools_documentation**
Get documentation for n8n MCP tools. Call without parameters for quick start guide. Use topic parameter to get documentation for specific tools. Use depth='full' for comprehensive documentation.

**search_nodes**
Search n8n nodes by keyword with optional real-world examples. Pass query as string. Example: query="webhook" or query="database". Returns max 20 results. Use includeExamples=true to get top 2 template configs per node.

**get_node**
Get node info with progressive detail levels and multiple modes. Detail: minimal (~200 tokens), standard (~1-2K, default), full (~3-8K). Modes: info (default), docs (markdown documentation), search_properties (find properties), versions/compare/breaking/migrations (version info). Use format='docs' for readable documentation, mode='search_properties' with propertyQuery for finding specific fields.

**validate_node**
Validate n8n node configuration. Use mode='full' for comprehensive validation with errors/warnings/suggestions, mode='minimal' for quick required fields check. Example: nodeType="nodes-base.slack", config={resource:"channel",operation:"create"}

**get_template**
Get template by ID. Use mode to control response size: nodes_only (minimal), structure (nodes+connections), full (complete workflow).

**search_templates**
Search templates with multiple modes. Use searchMode='keyword' for text search, 'by_nodes' to find templates using specific nodes, 'by_task' for curated task-based templates, 'by_metadata' for filtering by complexity/setup time/services, 'patterns' for lightweight workflow pattern summaries mined from 2700+ templates.

**validate_workflow**
Full workflow validation: structure, connections, expressions, AI tools. Returns errors/warnings/fixes. Essential before deploy.

### Управляющие инструменты (src/mcp/tools-n8n-manager.ts)

**n8n_create_workflow**
Create workflow. Requires: name, nodes[], connections{}. Created inactive. Returns workflow with ID.

**n8n_get_workflow**
Get workflow by ID with different detail levels. n8n has a draft/publish model: the workflow body holds the draft (latest edits); use mode='active' to see the published graph that is actually running. Modes: 'full' (draft + metadata), 'details' (full + execution stats), 'active' (published graph only), 'structure' (nodes/connections topology), 'filtered' (full config of only the nodes named in nodeNames - use to read one heavy node without the whole workflow), 'minimal' (id/name/active/tags).

**n8n_update_full_workflow**
Full workflow update. Requires complete nodes[] and connections{}. For incremental use n8n_update_partial_workflow.

**n8n_update_partial_workflow**
Update workflow incrementally with diff operations. Types: addNode, removeNode, updateNode, patchNodeField, moveNode, enable/disableNode, addConnection, removeConnection, rewireConnection, cleanStaleConnections, replaceConnections, updateSettings, updateName, setNodeGroups, add/removeTag, activate/deactivateWorkflow, transferWorkflow. patchNodeField requires fieldPath (dot path, e.g. "parameters.jsCode") and patches: [{find, replace}]. setNodeGroups replaces all canvas groups: [{name, nodeNames|nodeIds}] (or [] to ungroup). See tools_documentation("n8n_update_partial_workflow", "full") for details.

**n8n_delete_workflow**
Permanently delete a workflow. This action cannot be undone.

**n8n_list_workflows**
List workflows (minimal metadata only). Returns id/name/active/dates/tags. Check hasMore/nextCursor for pagination.

**n8n_validate_workflow**
Validate workflow by ID. Checks nodes, connections, expressions. Returns errors/warnings/suggestions.

**n8n_autofix_workflow**
Automatically fix common workflow validation errors. Preview fixes or apply them. Fixes expression format, typeVersion, error output config, webhook paths, connection structure issues (numeric keys, invalid types, ID-to-name, duplicates, out-of-bounds indices).

**n8n_test_workflow**
Test/trigger workflow execution. Auto-detects trigger type (webhook/form/chat). Supports: webhook (HTTP), form (fields), chat (message). Note: Only workflows with these trigger types can be executed externally.

**n8n_executions**
Manage workflow executions: get details, list, or delete. Use action='get' with id for execution details, action='list' for listing executions, action='delete' to remove execution record.

**n8n_evaluations**
Run and read evaluation test runs for a workflow. Reading requires n8n >= 2.30, run/cancel require n8n >= 2.32, and the API key must be created on the matching release to carry the testRun scopes; run/cancel also need the key owner to hold workflow:execute on the workflow. Actions: list_runs=list runs for a workflow, get_run=single run with aggregated metrics, list_cases=per-case results (paginate - cases can be large), run=trigger a run on a workflow with an evaluation trigger, cancel=stop a running run.

**n8n_health_check**
Check n8n instance health and API connectivity. Use mode='diagnostic' for detailed troubleshooting with env vars and tool status.

**n8n_workflow_versions**
Manage workflow version history, rollback, and cleanup. Versions are scoped to your n8n instance. Five modes:
- list: Show version history for a workflow
- get: Get details of specific version
- rollback: Restore workflow to previous version (creates backup first)
- delete: Delete specific version or all versions for a workflow
- prune: Manually trigger pruning to keep N most recent versions
Old backups are also pruned automatically (10 most recent per workflow, plus an age-based retention window).

**n8n_deploy_template**
Deploy a workflow template from n8n.io directly to your n8n instance. Deploys first, then auto-fixes common issues (expression format, typeVersions). Returns workflow ID, required credentials, and fixes applied.

**n8n_manage_datatable**
Manage n8n data tables and rows. Actions: createTable, listTables, getTable, updateTable, deleteTable, getRows, insertRows, updateRows, upsertRows, deleteRows.

**n8n_manage_credentials**
Manage n8n credentials. Actions: list, get, create, update, delete, getSchema. Use getSchema to discover required fields before creating. For list, page beyond 100 results with cursor (from the previous response's nextCursor). NOTE: list/get need an n8n deployment whose public API permits credential reads — older n8n versions, restricted API keys, or instance settings can reject them, returning NOT_SUPPORTED (create, delete, getSchema — and update where the API version supports it — still work). SECURITY: credential data values are never logged.

**n8n_audit_instance**
Security audit of n8n instance. Combines n8n's built-in audit API (credentials, database, nodes, instance, filesystem risks) with deep workflow scanning (hardcoded secrets via 50+ regex patterns, unauthenticated webhooks, error handling gaps, data retention risks). Returns actionable markdown report with remediation steps using n8n_manage_credentials and n8n_update_partial_workflow.

### Альтернативный набор описаний (клиент-зависимая подмена)

`src/mcp/tools-n8n-friendly.ts` содержит карту `n8nFriendlyDescriptions` — сокращённые описания тех же инструментов, применяемые через `makeToolsN8nFriendly` (импортируется в `src/mcp/server.ts:19`), когда клиентом выступает n8n AI Agent. Примеры дословно:

- validate_node: Validate n8n node config. Pass nodeType (string) and config (object). Use mode="full" for comprehensive validation, mode="minimal" for quick check. Example: {"nodeType": "nodes-base.slack", "config": {"resource": "channel", "operation": "create"}}
- search_nodes: Search nodes. Pass query (string). Example: {"query": "webhook"}
- get_node: Get node info with multiple modes. Pass nodeType (string). Use mode="info" for config, mode="docs" for documentation, mode="search_properties" with propertyQuery for finding fields. Example: {"nodeType": "nodes-base.httpRequest", "detail": "standard"}
