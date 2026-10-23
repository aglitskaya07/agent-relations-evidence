# UNIT: @softeria/ms-365-mcp-server | npm v0.135.0 (published 2026-07-29T08:04:34.178Z) | рамки: npm-top | captured 2026-07-29 (static, tarball)

## ВЕРДИКТ: MCP-сервер
Полноценный MCP-сервер: `dist/server.js` создаёт `new McpServer(...)` из `@modelcontextprotocol/sdk/server/mcp.js`, регистрирует инструменты через `server.registerTool`/`server.tool`, работает в stdio и HTTP/OAuth режимах. Экспонирует Microsoft Graph (почта, календарь, Teams, OneDrive/SharePoint, Excel, задачи, presence и т.д.).

## CHANNEL: instructions, npm (static, 1647 chars в дефолтной конфигурации)
Instructions передаются конструктору `McpServer` (dist/server.js:63–69) через `buildMcpServerInstructions(opts)` из `dist/mcp-instructions.js`. Строка собирается ДИНАМИЧЕСКИ из фиксированных частей в зависимости от опций запуска (readOnly / multiAccount / orgMode / discovery). Базовые 8 частей (1579 chars, соединяются пробелом), дословно:

> Microsoft 365 MCP exposes Microsoft Graph through MCP tools. Use each tool name, description, and parameter schema as the source of truth.
> Microsoft Graph OData: do not combine $filter with $search on the same request. For lists, prefer modest $top (or top) and $select; avoid very large pages unless the user needs them.
> Mail and message $search uses KQL; the $search query parameter value must be double-quoted per Graph (see search-query-parameter in Microsoft Graph docs).
> When you need an organizational user or recipient address, resolve it with list-users (or another directory tool); do not invent SMTP addresses.
> Directory $search on collections such as /users or /groups requires ConsistencyLevel: eventual when the tool exposes that header.
> Teams chat and channel messages: prefer HTML contentType in the body; plain text is often mangled by Graph.
> Files / binary content: for large drive/SharePoint file content, prefer get-download-url to resolve a pre-authenticated URL for out-of-band download. Use download-bytes for authenticated byte reads such as mail attachments, profile photos, Teams hosted content, and meeting recordings. In stdio mode, download-bytes-to-file writes those same authenticated bytes straight to a local absolute path instead of returning base64 — the only out-of-band option for large mail attachments and meeting recordings, which get-download-url cannot handle. These tools take relative Microsoft Graph paths, not absolute URLs. For uploads, upload-file-content takes a base64 string body up to 4MB; use create-upload-session above that.

Условные добавки:
- readOnly: «This server is read-only; write operations are disabled.»
- multiAccount: «Multiple accounts: pass the account parameter when required (see list-accounts).»
- НЕ org-mode (дефолт): «Work/school-only tools require starting the server with --org-mode.» → дефолтная строка = 1647 chars.
- discovery (+532 chars): «DISCOVERY MODE ADD-ON: Graph is reached via search-tools → get-tool-schema → execute-tool (plus auth helpers). Workflow: (1) call search-tools with short natural-language keywords (BM25-ranked); (2) call get-tool-schema(tool_name) to see the parameters, required fields, and enum values; (3) call execute-tool with tool_name exactly as returned and parameters shaped per the schema. Skipping get-tool-schema is the leading cause of Graph 400 errors here. If search-tools returns no matches, retry with shorter or different keywords.»

Оценка: instructions полностью технические/операционные (правила OData, KQL-кавычки, роутинг бинарного контента между собственными инструментами). НЕТ стиринга против built-in инструментов, нет «primary/precedence/last resort», нет требований использовать сервер вместо памяти или веб-поиска.

## CHANNEL: tool descriptions, npm (static, coverage=marker-scan+sample)
Инвентарь: 324 Graph-инструмента (dist/endpoints.json + сгенерированные описания в dist/generated/client.js / client-beta.js) + 4 utility (parse-teams-url, download-bytes, download-bytes-to-file, get-download-url) + 6 auth (login, logout, verify-login, list-accounts, select-account, remove-account) + 3 discovery-mode (search-tools, get-tool-schema, execute-tool) = 337 статически определённых регистраций (не все активны одновременно: discovery-режим заменяет прямую регистрацию Graph-инструментов тремя мета-инструментами; часть инструментов требует --org-mode / stdio).
Итоговое описание Graph-инструмента = (descriptionOverride ?? описание из OpenAPI-генерации) + "\n\n💡 TIP: <llmTip>"; для beta-эндпоинтов префикс «[beta]». Все 324 имеют реальные описания (0 fallback).

### Маркер-скан (полный, по всем 337 описаниям): 30 совпадений, ВСЕ доброкачественные
- `copilot-retrieve` — маркер `Prefer`: «…unlike search-query/search-onedrive-files/search-sharepoint-sites, which are lexical KQL. Prefer this for paraphrase/intent queries (e.g. resolving an informal project nickname…)» — внутрисерверный роутинг между своими инструментами.
- `download-bytes` (utility) — маркер `prefer`: «For large drive/SharePoint file content, prefer get-download-url, which returns a pre-authenticated URL to stream bytes out-of-band instead of base64 through the agent context.» — внутрисерверный роутинг.
- `get-download-url` (utility) — маркер `Prefer this over`: «Prefer this over download-bytes for any file above a few KB or any bulk download.» — внутрисерверный роутинг.
- `download-bytes-to-file` (utility) — маркер `preferred`: «For OneDrive or SharePoint file content, get-download-url is preferred — it returns a pre-authenticated URL for fully out-of-band download without the server fetching the bytes.» — внутрисерверный роутинг.
- `list-mail-folder-messages-delta` — маркер `Prefer this over`: «Prefer this over full re-list for polling.» — роутинг на самого себя vs полный перелист, техсовет.
- `send-chat-message` / `pin-chat-message` — маркер `must use`: «…you must use the list chats method to retrieve the ID of an existing chat before you can…» — цитата документации Microsoft Graph, техническая зависимость.
- `set-my-presence` — маркер `prefer`: «…if the user also wants to override their *visible* status regardless of activity, prefer set-my-user-preferred-presence.» — внутрисерверный роутинг.
- `execute-tool` — маркер `prefer`: «For list endpoints, prefer modest $top plus $select.» — техсовет по параметрам.
- `get-mailbox-settings`, `update-mailbox-settings`, `list-supported-time-zones`, `list-supported-languages`, `set-my-user-preferred-presence`, `clear-my-user-preferred-presence`, `get-meeting-recording-content` — многочисленные срабатывания на `preferred`/`the user has chosen`/`prefer` — все это доменная лексика Outlook/Teams («preferred time zone», «preferred presence»), не стиринг.

Вывод скана: ни одного случая стиринга против внешних/встроенных инструментов, самовосхваления, «call immediately», precedence-клауз или экономических приманок. Все «prefer/must» — либо внутрисерверный роутинг между собственными инструментами, либо цитаты официальной документации Microsoft Graph.

### 8 репрезентативных полных описаний

**list-mail-messages**

```
List, search, and filter Outlook email messages in the signed-in user's mailbox across all folders. Returns message metadata (subject, from, receivedDateTime, isRead, hasAttachments) plus a body preview. Use $search for keyword queries, $filter to narrow by sender/read state/date, $top to limit page size, and $select to trim fields.

💡 TIP: List read search my Outlook emails across folders. CRITICAL: When searching emails, the $search parameter value MUST be wrapped in double quotes. Format: $search="your search query here". Use KQL (Keyword Query Language) syntax to search specific properties: 'from:', 'subject:', 'body:', 'to:', 'cc:', 'bcc:', 'attachment:', 'hasAttachments:', 'importance:', 'received:', 'sent:'. Examples: $search="from:john@example.com" | $search="subject:meeting AND hasAttachments:true" | $search="body:urgent AND received>=2024-01-01" | $search="from:john AND importance:high". Remember: ALWAYS wrap the entire search expression in double quotes! Reference: https://learn.microsoft.com/en-us/graph/search-query-parameter IMPORTANT: Always use $select to limit returned fields and reduce response size. Recommended default: $select=id,subject,from,toRecipients,receivedDateTime,bodyPreview,isRead,hasAttachments. Use bodyPreview instead of body for listings. To read the full email body, use get-mail-message with the specific message id.
```

**send-mail**

```
Send the message specified in the request body using either JSON or MIME format. When using JSON format, you can include a file attachment in the same sendMail action call. When using MIME format: This method saves the message in the Sent Items folder. Alternatively, create a draft message to send later. To learn more about the steps involved in the backend before a mail is delivered to recipients, see here.

💡 TIP: CRITICAL: Do not try to guess the email address of the recipients. Use the list-users tool to find the email address of the recipients.
```

**copilot-retrieve**

```
Invoke action retrieval

💡 TIP: Semantic/hybrid search over Microsoft 365 content via the Copilot Retrieval API. Grounds a natural-language query against the same hybrid index that powers Microsoft 365 Copilot and returns permission-trimmed text extracts with their source URLs — unlike search-query/search-onedrive-files/search-sharepoint-sites, which are lexical KQL. Prefer this for paraphrase/intent queries (e.g. resolving an informal project nickname, or matching 'packaging requirements' against text that never uses that phrase). Pass the request fields nested under a 'body' object: { queryString, dataSource, filterExpression?, resourceMetadata?, maximumNumberOfResults? }. Returns { retrievalHits: [{ webUrl, extracts: [{ text, relevanceScore }], resourceType, resourceMetadata, sensitivityLabel? }] }. Work/school accounts only (personal accounts are not supported). dataSource 'sharePoint'/'oneDriveBusiness' need delegated Files.Read.All + Sites.Read.All (requested by default); dataSource 'externalItem' (Copilot connectors) needs ExternalItem.Read.All, which is not requested by default - add it with --extra-scopes ExternalItem.Read.All.
```

**graph-batch**

```
Combine up to 20 Graph requests into a single HTTP call. Body: { requests: [{ id: '1', method: 'GET'|'POST'|'PATCH'|'DELETE', url: '/me/messages?$top=5', headers?: {...}, body?: {...}, dependsOn?: ['1'] }, ...] }. Returns { responses: [{ id, status, body, headers }] } in arbitrary order \u2014 match by id. Use cases: (1) parallelize many small reads (e.g. fetch 15 mail messages by id in one round-trip); (2) sequence dependent writes via dependsOn; (3) batch many Excel range writes into one call to dramatically reduce latency on large workbook builds. Note: each sub-request URL is relative to the Graph version root (/me/..., /drives/..., NOT https://graph.microsoft.com/v1.0/...).

💡 TIP: Combine up to 20 Graph requests into a single HTTP call. Body: { requests: [{ id: '1', method: 'GET'|'POST'|'PATCH'|'DELETE', url: '/me/messages?$top=5', headers?: {...}, body?: {...}, dependsOn?: ['1'] }, ...] }. Returns { responses: [{ id, status, body, headers }] } in arbitrary order — match by id. Use cases: (1) parallelize many small reads (e.g. fetch 15 mail messages by id in one round-trip); (2) sequence dependent writes via dependsOn; (3) batch many Excel range writes into one call to dramatically reduce latency on large workbook builds. Note: each sub-request URL is relative to the Graph version root (/me/..., /drives/..., NOT https://graph.microsoft.com/v1.0/...).
```

**list-mail-folder-messages-delta**

```
Get a set of messages added, deleted, or updated in a specified folder. A delta function call for messages in a folder is similar to a GET request, except that by appropriately
applying state tokens in one or more of these calls, you can [query for incremental changes in the messages in
that folder](/graph/delta-query-messages). It allows you to maintain and synchronize a local store of a user's messages without
having to fetch the entire set of messages from the server every time.

💡 TIP: Incremental sync of messages within a mail folder. Graph only supports delta scoped to a folder — use mailFolder-id = 'inbox' for the well-known inbox, or another folder id from list-mail-folders. First call returns all messages plus @odata.deltaLink; subsequent calls with that link return only changes (created/updated/deleted). @odata.nextLink paginates within a single delta window. Deltas expire after ~30 days of inactivity — start over if the server returns 410. Prefer this over full re-list for polling.
```

**download-bytes (utility)**

```
Download binary content from Microsoft Graph and return it as base64. Single tool for any binary read: drive file content, mail attachment, profile photo, Teams hosted content, meeting recording. Returns { contentType, encoding: "base64", contentLength, contentBytes }. For large drive/SharePoint file content, prefer get-download-url, which returns a pre-authenticated URL to stream bytes out-of-band instead of base64 through the agent context.
```

**get-download-url (utility)**

```
Resolve a short-lived, pre-authenticated download URL for Microsoft Graph binary content that exposes one (drive/SharePoint file content). The returned URL streams the bytes with NO Authorization header, so the client can fetch it straight to disk (e.g. curl) without round-tripping base64 through the agent context. Prefer this over download-bytes for any file above a few KB or any bulk download. Returns { downloadUrl, name?, size?, contentType? }. NOTE: mail file attachments (/messages/{id}/attachments/{id}/$value) and meeting recordings do NOT expose a pre-authenticated URL — Graph offers no such link for them; use download-bytes for small ones.
```

**execute-tool (discovery mode)**

```
Execute a Microsoft Graph API tool by name. Workflow: search-tools → get-tool-schema → execute-tool. Call get-tool-schema first for any tool you have not seen before — passing the wrong shape to parameters will fail validation or return a Graph 400. For list endpoints, prefer modest $top plus $select.
```

## NOTES
- Код в dist/ собран tsup, но НЕ минифицирован: читаемые идентификаторы, строки целиком, только escape-последовательности \u2014 и т.п. Src в тарболе частичный (src/endpoints.json + src/generated/*), основной анализ по dist/.
- Риск динамической сборки строк: НИЗКИЙ и полностью прослежен. Instructions собираются из фиксированных литералов по флагам запуска (все ветки процитированы выше); описания инструментов — конкатенация статических литералов (descriptionOverride/OpenAPI-описание + llmTip + «[beta]»-префикс). Никаких загрузок текста с сети/из env в описания не обнаружено.
- Просмотрено ~12 файлов детально (server.js, mcp-instructions.js, graph-tools.js, auth-tools.js, endpoints.json, generated/client.js, generated/client-beta.js, package.json и др.) из 64 файлов пакета; экстракция описаний — программно по всем 324 эндпоинтам + 13 служебным инструментам.
- Особенность: search-tools/BM25-индекс в discovery-режиме ранжирует по name+llmTip+description+path; авторы сознательно «front-load» ключевые слова в описания utility-инструментов (комментарий в коде у download-bytes-to-file) — это оптимизация под собственный поиск, не под хост-агента.
