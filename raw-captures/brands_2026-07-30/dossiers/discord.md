# UNIT: discord | Discord | github barryyip0625/mcp-discord | тип автора: комьюнити | captured 2026-07-29 (static source)

Источник: `brands/src/discord/mcp-discord-HEAD` (TypeScript, MCP SDK). Сервер подтверждён: `new McpServer(...)` в `src/app.ts:24`, `new Server(...)` в `src/server.ts:69`, обработчики `ListToolsRequestSchema` / `CallToolRequestSchema`, stdio + StreamableHTTP транспорты.

## CHANNEL: instructions
(не обнаружены статически)

Конструктор `McpServer` получает только `{ name: 'discord-mcp-server', version: '1.0.0' }` и `{ capabilities: { tools: {}, logging: {} } }`; конструктор `Server` — `{ name: "MCP-Discord", version: "1.0.0" }` и `{ capabilities: { tools: {} } }`. Поля `instructions` нет ни в одном из них, кастомного обработчика `initialize` в репозитории нет.

## CHANNEL: tool descriptions (coverage=marker-scan+sample, N=43)

Единственный источник описаний — статический массив `toolList` в `src/toolList.ts` (используется обработчиком ListTools в `src/server.ts`). Альтернативная точка входа `src/app.ts` регистрирует те же инструменты через `server.tool(name, t.schema?.description ?? '', ...)`, но zod-схемы в `src/schemas.ts` не содержат `.describe()`/`description`, поэтому там описания оказываются пустыми строками.

Маркер-скан по всем 43 описаниям: совпадений 0.

Ниже все 43 инструмента с дословными описаниями (полный набор, не выборка):

- **discord_create_category** — "Creates a new category in a Discord server."
- **discord_edit_category** — "Edits an existing Discord category (name and position)."
- **discord_delete_category** — "Deletes a Discord category by ID."
- **discord_login** — "Logs in to Discord using the configured token"
- **discord_send** — "Sends a message to a specified Discord text channel. Optionally reply to another message by providing its message ID."
- **discord_get_forum_channels** — "Lists all forum channels in a specified Discord server (guild)"
- **discord_create_forum_post** — "Creates a new post in a Discord forum channel with optional tags"
- **discord_get_forum_post** — "Retrieves details about a forum post including its messages"
- **discord_list_forum_threads** — "Lists all threads (posts) in a Discord forum channel, including both active and archived threads"
- **discord_reply_to_forum** — "Adds a reply to an existing forum post or thread"
- **discord_create_text_channel** — "Creates a new text channel in a Discord server with an optional topic and parent category"
- **discord_create_forum_channel** — "Creates a new forum channel in a Discord server, optionally under a category"
- **discord_edit_channel** — "Edits a Discord channel's name, topic, parent category, or position"
- **discord_delete_channel** — "Deletes a Discord channel with an optional reason"
- **discord_read_messages** — "Retrieves messages from a Discord text channel. Supports date-based filtering via before/after/around params (accepts snowflake IDs or ISO 8601 dates)."
- **discord_get_server_info** — "Retrieves detailed information about a Discord server including channels and member count"
- **discord_add_reaction** — "Adds an emoji reaction to a specific Discord message"
- **discord_add_multiple_reactions** — "Adds multiple emoji reactions to a Discord message at once"
- **discord_remove_reaction** — "Removes a specific emoji reaction from a Discord message"
- **discord_get_reaction_users** — "Lists the users who reacted with a specific emoji to a Discord message. Uses REST fetch and does not require Gateway intents. Returns up to 100 users per call."
- **discord_delete_forum_post** — "Deletes a forum post or thread with an optional reason"
- **discord_get_forum_tags** — "Gets all available tags for a Discord forum channel, including tag IDs, names, and emoji"
- **discord_set_forum_tags** — "Sets the available tags for a Discord forum channel. Replaces all existing tags."
- **discord_update_forum_post** — "Updates a forum post's title, applied tags, archived status, or locked status. Tags can be specified by name or ID."
- **discord_edit_message** — "Edits a message previously sent by the bot. Only messages authored by the bot can be edited."
- **discord_delete_message** — "Deletes a specific message from a Discord text channel"
- **discord_create_webhook** — "Creates a new webhook for a Discord channel"
- **discord_send_webhook_message** — "Sends a message to a Discord channel using a webhook"
- **discord_edit_webhook** — "Edits an existing webhook for a Discord channel"
- **discord_delete_webhook** — "Deletes an existing webhook for a Discord channel"
- **discord_list_servers** — "Lists all Discord servers the bot is a member of"
- **discord_search_messages** — "Searches for messages in a Discord server"
- **discord_list_roles** — "Lists all roles in a Discord server with their properties"
- **discord_create_role** — "Creates a new role in a Discord server"
- **discord_edit_role** — "Edits an existing role in a Discord server"
- **discord_delete_role** — "Deletes a role from a Discord server"
- **discord_assign_role** — "Assigns a role to a member in a Discord server"
- **discord_remove_role** — "Removes a role from a member in a Discord server"
- **discord_list_members** — "Lists members in a Discord server with their roles"
- **discord_get_member** — "Gets detailed information about a specific member in a Discord server"
- **discord_create_voice_channel** — "Creates a new voice channel in a Discord server with an optional parent category"
- **discord_set_channel_permissions** — "Sets permission overrides for a role or user on a channel or category"
- **discord_remove_channel_permissions** — "Removes all permission overrides for a role or user on a channel or category"
