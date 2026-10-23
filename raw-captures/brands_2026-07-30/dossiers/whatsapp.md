# UNIT: whatsapp | WhatsApp | github lharries/whatsapp-mcp | тип автора: комьюнити | captured 2026-07-29 (static source)

Подтверждение: это MCP-сервер. `whatsapp-mcp-server/main.py:2,19` — `from mcp.server.fastmcp import FastMCP`; `mcp = FastMCP("whatsapp")`; запуск `mcp.run(transport='stdio')`. Второй компонент репозитория (`whatsapp-bridge/main.go`) — Go-мост к whatsmeow с REST API, не MCP.

## CHANNEL: instructions
(не обнаружены статически)

Конструктор вызван как `FastMCP("whatsapp")` — только имя, без параметра `instructions`. Слово `instructions` в исходниках сервера, моста и README не встречается.

## CHANNEL: tool descriptions (coverage=full)

Всего 12 инструментов, все зарегистрированы через декоратор `@mcp.tool()` в `whatsapp-mcp-server/main.py`. Описание = docstring функции (дословно ниже, включая блоки Args/Returns).

### 1. search_contacts
```
Search WhatsApp contacts by name or phone number.
    
    Args:
        query: Search term to match against contact names or phone numbers
```

### 2. list_messages
```
Get WhatsApp messages matching specified criteria with optional context.
    
    Args:
        after: Optional ISO-8601 formatted string to only return messages after this date
        before: Optional ISO-8601 formatted string to only return messages before this date
        sender_phone_number: Optional phone number to filter messages by sender
        chat_jid: Optional chat JID to filter messages by chat
        query: Optional search term to filter messages by content
        limit: Maximum number of messages to return (default 20)
        page: Page number for pagination (default 0)
        include_context: Whether to include messages before and after matches (default True)
        context_before: Number of messages to include before each match (default 1)
        context_after: Number of messages to include after each match (default 1)
```

### 3. list_chats
```
Get WhatsApp chats matching specified criteria.
    
    Args:
        query: Optional search term to filter chats by name or JID
        limit: Maximum number of chats to return (default 20)
        page: Page number for pagination (default 0)
        include_last_message: Whether to include the last message in each chat (default True)
        sort_by: Field to sort results by, either "last_active" or "name" (default "last_active")
```

### 4. get_chat
```
Get WhatsApp chat metadata by JID.
    
    Args:
        chat_jid: The JID of the chat to retrieve
        include_last_message: Whether to include the last message (default True)
```

### 5. get_direct_chat_by_contact
```
Get WhatsApp chat metadata by sender phone number.
    
    Args:
        sender_phone_number: The phone number to search for
```

### 6. get_contact_chats
```
Get all WhatsApp chats involving the contact.
    
    Args:
        jid: The contact's JID to search for
        limit: Maximum number of chats to return (default 20)
        page: Page number for pagination (default 0)
```

### 7. get_last_interaction
```
Get most recent WhatsApp message involving the contact.
    
    Args:
        jid: The JID of the contact to search for
```

### 8. get_message_context
```
Get context around a specific WhatsApp message.
    
    Args:
        message_id: The ID of the message to get context for
        before: Number of messages to include before the target message (default 5)
        after: Number of messages to include after the target message (default 5)
```

### 9. send_message
```
Send a WhatsApp message to a person or group. For group chats use the JID.

    Args:
        recipient: The recipient - either a phone number with country code but no + or other symbols,
                 or a JID (e.g., "123456789@s.whatsapp.net" or a group JID like "123456789@g.us")
        message: The message text to send
    
    Returns:
        A dictionary containing success status and a status message
```

### 10. send_file
```
Send a file such as a picture, raw audio, video or document via WhatsApp to the specified recipient. For group messages use the JID.
    
    Args:
        recipient: The recipient - either a phone number with country code but no + or other symbols,
                 or a JID (e.g., "123456789@s.whatsapp.net" or a group JID like "123456789@g.us")
        media_path: The absolute path to the media file to send (image, video, document)
    
    Returns:
        A dictionary containing success status and a status message
```

### 11. send_audio_message
```
Send any audio file as a WhatsApp audio message to the specified recipient. For group messages use the JID. If it errors due to ffmpeg not being installed, use send_file instead.
    
    Args:
        recipient: The recipient - either a phone number with country code but no + or other symbols,
                 or a JID (e.g., "123456789@s.whatsapp.net" or a group JID like "123456789@g.us")
        media_path: The absolute path to the audio file to send (will be converted to Opus .ogg if it's not a .ogg file)
    
    Returns:
        A dictionary containing success status and a status message
```

### 12. download_media
```
Download media from a WhatsApp message and get the local file path.
    
    Args:
        message_id: The ID of the message containing the media
        chat_jid: The JID of the chat containing the message
    
    Returns:
        A dictionary containing success status, a status message, and the file path if successful
```
