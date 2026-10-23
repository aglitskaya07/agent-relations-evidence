# UNIT: slack | Slack | github modelcontextprotocol/servers-archived/src/slack | тип автора: референсный | captured 2026-07-29 (static source)

Подтверждение MCP-сервера: `src/slack/index.ts` импортирует `Server` из `@modelcontextprotocol/sdk/server/index.js`, поднимает `StdioServerTransport`, регистрирует `ListToolsRequestSchema` и `CallToolRequestSchema`. Это полноценный MCP-сервер.

## CHANNEL: instructions
(не обнаружены статически)

Конструктор сервера (index.ts:395–405) получает только `{ name: "Slack MCP Server", version: "1.0.0" }` и `{ capabilities: { tools: {} } }`. Поля `instructions` нет; собственного обработчика `initialize` в репозитории нет.

## CHANNEL: tool descriptions (coverage=full)

Всего инструментов: 8. Определения — статические литералы `const <name>Tool: Tool = {...}` в `index.ts`, возвращаются списком в обработчике `ListToolsRequestSchema` (строки 556–570).

1. **slack_list_channels**
"List public or pre-defined channels in the workspace with pagination"

2. **slack_post_message**
"Post a new message to a Slack channel"

3. **slack_reply_to_thread**
"Reply to a specific message thread in Slack"

4. **slack_add_reaction**
"Add a reaction emoji to a message"

5. **slack_get_channel_history**
"Get recent messages from a channel"

6. **slack_get_thread_replies**
"Get all replies in a message thread"

7. **slack_get_users**
"Get a list of all users in the workspace with their basic profile information"

8. **slack_get_user_profile**
"Get detailed profile information for a specific user"

### Описания параметров (дословно, для полноты канала)

- slack_list_channels.limit: "Maximum number of channels to return (default 100, max 200)"
- slack_list_channels.cursor: "Pagination cursor for next page of results"
- slack_post_message.channel_id: "The ID of the channel to post to"
- slack_post_message.text: "The message text to post"
- slack_reply_to_thread.channel_id: "The ID of the channel containing the thread"
- slack_reply_to_thread.thread_ts: "The timestamp of the parent message in the format '1234567890.123456'. Timestamps in the format without the period can be converted by adding the period such that 6 numbers come after it."
- slack_reply_to_thread.text: "The reply text"
- slack_add_reaction.channel_id: "The ID of the channel containing the message"
- slack_add_reaction.timestamp: "The timestamp of the message to react to"
- slack_add_reaction.reaction: "The name of the emoji reaction (without ::)"
- slack_get_channel_history.channel_id: "The ID of the channel"
- slack_get_channel_history.limit: "Number of messages to retrieve (default 10)"
- slack_get_thread_replies.channel_id: "The ID of the channel containing the thread"
- slack_get_thread_replies.thread_ts: "The timestamp of the parent message in the format '1234567890.123456'. Timestamps in the format without the period can be converted by adding the period such that 6 numbers come after it."
- slack_get_users.cursor: "Pagination cursor for next page of results"
- slack_get_users.limit: "Maximum number of users to return (default 100, max 200)"
- slack_get_user_profile.user_id: "The ID of the user"
