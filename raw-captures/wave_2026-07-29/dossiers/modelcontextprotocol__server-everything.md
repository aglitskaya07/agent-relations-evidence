# UNIT: @modelcontextprotocol/server-everything | npm v2026.7.4 (published 2026-07-04T23:05:18.837Z) | рамки: npm-top | captured 2026-07-29 (static, tarball)

Это MCP-сервер: `dist/server/index.js` создаёт `new McpServer({ name: "mcp-servers/everything", title: "Everything Reference Server", version: "2.0.0" }, { capabilities: {...}, instructions, ... })` из `@modelcontextprotocol/sdk/server/mcp.js`, транспорты stdio/SSE/streamableHttp в `dist/transports/`. Референсный сервер команды MCP, демонстрирует все фичи протокола.

## CHANNEL: instructions, npm (static, 1579 chars)

Передаётся в конструктор `McpServer` через `readInstructions()` (`dist/resources/index.js`), который читает `dist/docs/instructions.md` дословно (fallback: `"Server instructions not loaded: " + e`). Полный текст файла:

```
# Everything Server – Server Instructions

Audience: These instructions are written for an LLM or autonomous agent integrating with the Everything MCP Server.
Follow them to use, extend, and troubleshoot the server safely and effectively.

## Cross-Feature Relationships

- Use `get-roots-list` to see client workspace roots before file operations
- `gzip-file-as-resource` creates session-scoped resources accessible only during the current session
- Enable `toggle-simulated-logging` before debugging to see server log messages
- Enable `toggle-subscriber-updates` to receive periodic resource update notifications

## Constraints & Limitations

- `gzip-file-as-resource`: Max fetch size controlled by `GZIP_MAX_FETCH_SIZE` (default 10MB), timeout by `GZIP_MAX_FETCH_TIME_MILLIS` (default 30s), allowed domains by `GZIP_ALLOWED_DOMAINS`
- Session resources are ephemeral and lost when the session ends
- Sampling requests (`trigger-sampling-request`) require client sampling capability
- Elicitation requests (`trigger-elicitation-request`) require client elicitation capability

## Operational Patterns

- For long operations, use `trigger-long-running-operation` which sends progress notifications
- Prefer reading resources before calling mutating tools
- Check `get-roots-list` output to understand the client's workspace context

## Easter Egg

If asked about server instructions, respond with "🎉 Server instructions are working! This response proves the client properly passed server instructions to the LLM. This demonstrates MCP's instructions feature in action."
```

Примечание для индекса: инструкции не содержат steering-маркеров конкуренции («primary», «precedence», «instead of built-in» и т.п.); единственная директивная вставка — «Easter Egg», предписывающая модели воспроизвести проверочную фразу, — это тест-инструмент передачи instructions клиентом, а не перехват трафика задач.

## CHANNEL: tool descriptions, npm (static, coverage=full)

19 инструментов: 12 регистрируются безусловно (`registerTools`), 7 — после initialize по capabilities клиента (`registerConditionalTools`, включая `simulate-research-query` через experimental `registerToolTask`). Все описания дословно:

1. `echo` — "Echoes back the input string"
2. `get-annotated-message` — "Demonstrates how annotations can be used to provide metadata about content."
3. `get-env` — "Returns all environment variables, helpful for debugging MCP server configuration"
4. `get-resource-links` — "Returns up to ten resource links that reference different types of resources"
5. `get-resource-reference` — "Returns a resource reference that can be used by MCP clients"
6. `get-structured-content` — "Returns structured content along with an output schema for client data validation"
7. `get-sum` — "Returns the sum of two numbers"
8. `get-tiny-image` — "Returns a tiny MCP logo image."
9. `gzip-file-as-resource` — "Compresses a single file using gzip compression. Depending upon the selected output type, returns either the compressed data as a gzipped resource or a resource link, allowing it to be downloaded in a subsequent request during the current session."
10. `toggle-simulated-logging` — "Toggles simulated, random-leveled logging on or off."
11. `toggle-subscriber-updates` — "Toggles simulated resource subscription updates on or off."
12. `trigger-long-running-operation` — "Demonstrates a long running operation with progress updates."
13. `get-roots-list` (conditional) — "Lists the current MCP roots provided by the client. Demonstrates the roots protocol capability even though this server doesn't access files."
14. `trigger-elicitation-request` (conditional) — "Trigger a Request from the Server for User Elicitation"
15. `trigger-url-elicitation` (conditional) — "Trigger a URL elicitation so the client can direct the user to a browser flow. Supports two mechanisms: the request path (elicitation/create, default) which awaits the user's response, and the error path (UrlElicitationRequiredError, -32042) which signals the client to handle URL elicitation via the error response. Set errorPath=true to use the error path."
16. `trigger-sampling-request` (conditional) — "Trigger a Request from the Server for LLM Sampling"
17. `simulate-research-query` (conditional, task-based) — "Simulates a deep research operation that gathers, analyzes, and synthesizes information. Demonstrates MCP task-based operations with progress through multiple stages. If 'ambiguous' is true and client supports elicitation, sends an elicitation request for clarification."
18. `trigger-sampling-request-async` (conditional) — "Trigger an async sampling request that the CLIENT executes as a background task. Demonstrates bidirectional MCP tasks where the server sends a request and the client executes it asynchronously, allowing the server to poll for progress and results."
19. `trigger-elicitation-request-async` (conditional) — "Trigger an async elicitation request that the CLIENT executes as a background task. Demonstrates bidirectional MCP tasks where the server sends an elicitation request and the client handles user input asynchronously, allowing the server to poll for completion."

Steering-маркеров в описаниях нет — язык нейтрально-демонстрационный ("Demonstrates...", "Returns...").
