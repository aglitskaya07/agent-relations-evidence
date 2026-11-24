# UNIT: discord | Discord | github barryyip0625/mcp-discord | author type: community | captured 2026-07-29 (static source)

Source: `brands/src/discord/mcp-discord-HEAD` (TypeScript, MCP SDK). Server confirmed: `new McpServer(...)` in `src/app.ts:24`, `new Server(...)` in `src/server.ts:69`, handlers `ListToolsRequestSchema` / `CallToolRequestSchema`, stdio + StreamableHTTP transports.

## CHANNEL: instructions
(not found statically)

The `McpServer` constructor receives only `{ name: 'discord-mcp-server', version: '1.0.0' }` and `{ capabilities: { tools: {}, logging: {} } }`; the `Server` constructor — `{ name: "MCP-Discord", version: "1.0.0" }` and `{ capabilities: { tools: {} } }`. There is no `instructions` field in any of them, and there is no custom `initialize` handler in the repository.

## CHANNEL: tool descriptions (coverage=marker-scan+sample, N=43)

The only source of descriptions is the static array `toolList` in `src/toolList.ts` (used by the ListTools handler in `src/server.ts`). The alternative entry point `src/app.ts` registers the same tools via `server.tool(name, t.schema?.description ?? '', ...)`, but the zod schemas in `src/schemas.ts` do not contain `.describe()`/`description`, so the descriptions there end up as empty strings.

Marker scan across all 43 descriptions: 0 matches.

Below are all 43 tools with verbatim descriptions (the full set, not a sample):

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
