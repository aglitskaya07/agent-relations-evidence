# UNIT: touchdesigner-mcp-server | npm v1.5.0 (published 2026-07-11T03:22:00.223Z) | рамки: pulsemcp | captured 2026-07-29 (static, tarball)

## VERDICT: MCP server (confirmed)
`dist/server/touchDesignerServer.js` создаёт `new McpServer({ name: "TouchDesigner", version: MCP_SERVER_VERSION }, { capabilities: { logging: {}, prompts: {}, tools: {} } })` из `@modelcontextprotocol/sdk/server/mcp.js`; регистрирует tools и prompts; транспорты stdio/HTTP в `dist/transport/`. Это полноценный локальный MCP-сервер, проксирующий команды в TouchDesigner через его WebServer DAT API.

## CHANNEL: instructions, npm (static)
(не обнаружены статически)

Конструктору `McpServer` передаются только `name`, `version` и `capabilities` — поля `instructions` нет ни в конструкторе, ни где-либо ещё в dist (grep по "instructions" даёт только сообщения об ошибках подключения с ссылкой на README).

## CHANNEL: tool descriptions, npm (static, coverage=full)
14 инструментов: 13 из таблицы `TOOL_DEFINITIONS` (`dist/features/tools/toolDefinitions.js`) + мета-инструмент `describe_td_tools` (`dist/features/tools/handlers/tdTools.js`). Регистрация: `server.tool(definition.name, definition.description, schema, handler)` — описание передаётся дословно, без динамической досборки.

1. **get_td_info** — "Get server information from TouchDesigner"
2. **execute_python_script** — "Execute a Python script in TouchDesigner (detailLevel=minimal|summary|detailed, responseFormat=json|yaml|markdown)"
3. **get_td_nodes** — "List nodes under a path with token-optimized output (detailLevel+limit supported)"
4. **get_td_node_parameters** — "Get node parameters with concise/detailed formatting (detailLevel+limit supported)"
5. **get_td_node_errors** — "Check node and descendant errors reported by TouchDesigner"
6. **create_td_node** — "Create a new node in TouchDesigner"
7. **update_td_node_parameters** — "Update parameters of a specific node in TouchDesigner"
8. **delete_td_node** — "Delete an existing node in TouchDesigner"
9. **exec_node_method** — "Execute a method on a specific node in TouchDesigner"
10. **get_td_classes** — "List TouchDesigner Python classes/modules (detailLevel+limit supported)"
11. **get_td_class_details** — "Get information about a TouchDesigner class/module (detailLevel+limit supported)"
12. **get_td_module_help** — "Retrieve Python help() text for a TouchDesigner module or class"
13. **get_top_image** — "Capture the current output of a TOP node as an image so it can be viewed directly (maxSize optionally downscales the longer side)"
14. **describe_td_tools** — "Generate a filesystem-oriented manifest of available TouchDesigner tools"

### Steering-маркеры
Ни одно описание не содержит маркеров навязывания (нет "instead of", "primary", "prefer", "MUST use", "takes precedence", "Best for", superlatives). Описания сухие, функциональные. Единственный внешний текст — `errorComment: "Check reference resources: https://docs.derivative.ca/Python_Classes_and_Modules"`, добавляется только в сообщения об ошибках, не в описания.

## CHANNEL: prompts, npm (static) — доп. наблюдение
Зарегистрированы 3 MCP-prompt'а (`Check node errors`, `Node connection`, `Search node`) в `dist/features/prompts/handlers/td_prompts.js` — пользовательские prompt-шаблоны, вызываются явно клиентом, steering-риска в стиле «скрытых инструкций серверу» не несут (не проверялись построчно на маркеры, но это opt-in канал).

## NOTES
- Код НЕ минифицирован: tsc-выхлоп с сохранёнными комментариями и JSDoc, читается как исходник.
- Риск динамической сборки строк описаний: низкий. Описания — литералы в TOOL_DEFINITIONS; единственная конкатенация — REFERENCE_COMMENT (URL документации) и то только в error-путь.
- Просмотрено: ~101 файл в пакете (полный листинг), построчно прочитаны 5 ключевых (touchDesignerServer.js, toolDefinitions.js, register.js, tdTools.js, constants.js) + grep по всему dist на "instructions".
- capability `prompts` заявлена; `resources` не регистрируются.
