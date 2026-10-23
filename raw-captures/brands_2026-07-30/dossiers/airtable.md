# UNIT: airtable | Airtable | github domdomegg/airtable-mcp-server | тип автора: комьюнити | captured 2026-07-29 (static source)

## SERVER CONFIRMED
TypeScript MCP-сервер на `@modelcontextprotocol/sdk`. `src/index.ts` → `createServer()` создаёт `new McpServer({name: 'airtable-mcp-server', version})`; `src/main.ts` подключает stdio или StreamableHTTP транспорт. Инструменты регистрируются через `server.registerTool(...)` в `src/tools/*.ts`, агрегация в `src/tools/index.ts` (`registerAll`).

## CHANNEL: instructions
(не обнаружены статически)

Конструктор `McpServer` получает только `{name, version}` — поля `instructions` нет; в репозитории нет ни ручного хендлера `initialize`, ни строки `instructions` в коде (единственное совпадение слова — прозаический текст в README).

## CHANNEL: tool descriptions (coverage=full)

Всего 16 инструментов (все включены, дословно).

1. **list_records** — `List records from a table`
2. **search_records** — `Search for records containing specific text`
3. **list_bases** — `List all accessible Airtable bases`
4. **list_tables** — `List all tables in a specific base`
5. **describe_table** — `Get detailed information about a specific table`
6. **get_record** — `Get a specific record by ID`
7. **create_record** — `Create a new record in a table`
8. **update_records** — `Update up to 10 records in a table`
9. **delete_records** — `Delete records from a table`
10. **create_table** — `Create a new table in a base`
11. **update_table** — `Update a table's name or description`
12. **create_field** — `Create a new field in a table`
13. **update_field** — `Update a field's name or description`
14. **create_comment** — `Create a comment on a record`
15. **list_comments** — `List comments on a record`
16. **upload_attachment** — `Upload a file directly to an attachment field on an existing record using Airtable's upload API. Supports files up to 5 MB. For larger files, use create_record or update_records with a public URL. The record must already exist.`

### Заметки по каналу
- Все описания — одна фраза с фактическим действием; единственное многосоставное описание у `upload_attachment` (лимит 5 МБ + отсылка к альтернативным инструментам, чисто операционная).
- Присутствуют `annotations` (`readOnlyHint`, `destructiveHint`) — машиночитаемые подсказки, не текстовые директивы.
- Нет ни `registerResource`, ни `registerPrompt` — других текстовых каналов в сервере нет.
