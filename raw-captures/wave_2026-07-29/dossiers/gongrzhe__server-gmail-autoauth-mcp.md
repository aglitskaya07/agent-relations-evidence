# UNIT: @gongrzhe/server-gmail-autoauth-mcp | npm v1.1.11 (published 2025-08-06T01:16:22.211Z) | рамки: npm-top,smithery-top20 | captured 2026-07-29 (static, tarball)

Тип: подтверждённый MCP-сервер (stdio). `new Server({ name: "gmail", version: "1.0.0", capabilities: { tools: {} } })` в `dist/index.js:256`, транспорт `StdioServerTransport`, SDK `@modelcontextprotocol/sdk`.

## CHANNEL: instructions, npm (static)
(не обнаружены статически)

Конструктор Server получает только `name`, `version`, `capabilities` — поля `instructions` нет ни в конструкторе, ни где-либо ещё в пакете (grep по `instructions` дал только импорт-нерелевантные нули; единственное вхождение — отсутствует).

## CHANNEL: tool descriptions, npm (static, coverage=full)

19 инструментов, все зарегистрированы статически в одном ListTools-хендлере (`dist/index.js:264-362`). Описания дословно:

| # | name | description |
|---|------|-------------|
| 1 | `send_email` | Sends a new email |
| 2 | `draft_email` | Draft a new email |
| 3 | `read_email` | Retrieves the content of a specific email |
| 4 | `search_emails` | Searches for emails using Gmail search syntax |
| 5 | `modify_email` | Modifies email labels (move to different folders) |
| 6 | `delete_email` | Permanently deletes an email |
| 7 | `list_email_labels` | Retrieves all available Gmail labels |
| 8 | `batch_modify_emails` | Modifies labels for multiple emails in batches |
| 9 | `batch_delete_emails` | Permanently deletes multiple emails in batches |
| 10 | `create_label` | Creates a new Gmail label |
| 11 | `update_label` | Updates an existing Gmail label |
| 12 | `delete_label` | Deletes a Gmail label |
| 13 | `get_or_create_label` | Gets an existing label by name or creates it if it doesn't exist |
| 14 | `create_filter` | Creates a new Gmail filter with custom criteria and actions |
| 15 | `list_filters` | Retrieves all Gmail filters |
| 16 | `get_filter` | Gets details of a specific Gmail filter |
| 17 | `delete_filter` | Deletes a Gmail filter |
| 18 | `create_filter_from_template` | Creates a filter using a pre-defined template for common scenarios |
| 19 | `download_attachment` | Downloads an email attachment to a specified location |

Маркер-скан по steering-регексам (instead of built-in, most powerful, always default, PRECEDENCE, MUST use, primary, prefer, whenever the user и т.д.): 0 совпадений. Описания короткие, нейтральные, функциональные — steering-лексики нет.

## NOTES (static-анализ)
- Код НЕ минифицирован: читаемый tsc-выхлоп с комментариями, строки-описания — литералы.
- Риск динамической сборки строк: низкий. Все descriptions — статические строковые литералы; никаких template literals / конкатенации в ListTools-хендлере.
- Просмотрено: `package.json`, `dist/index.js` (основной, 51.8 KB, весь серверный код), grep по `dist/filter-manager.js`, `dist/label-manager.js`, `dist/utl.js`, `dist/evals/evals.js` — вспомогательные модули без регистрации инструментов. Всего 6 файлов кода + README/LICENSE.
- Единственная точка регистрации Server — index.js:256; других Server/McpServer/FastMCP в пакете нет.
