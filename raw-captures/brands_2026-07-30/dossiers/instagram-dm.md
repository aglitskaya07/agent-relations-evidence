# UNIT: instagram-dm | Instagram DM | github trypeggy/instagram_dm_mcp | тип автора: комьюнити | captured 2026-07-29 (static source)

## SERVER CONFIRMED

Python MCP-сервер на `mcp.server.fastmcp.FastMCP`. Единственный файл сервера: `src/mcp_server.py` (902 строки), 25 инструментов через декоратор `@mcp.tool()`. Транспорт/бэкенд — библиотека `instagrapi` (приватный Instagram API).

Конструктор:
```python
mcp = FastMCP(
   name="Instagram DMs",
   instructions=INSTRUCTIONS
)
```

## CHANNEL: instructions (62 chars)

Определено в `src/mcp_server.py:17-19` как литерал `INSTRUCTIONS`, передаётся в `FastMCP(instructions=...)`. Дословно (включая ведущий и завершающий перевод строки):

```

This server is used to send messages to a user on Instagram.

```

## CHANNEL: tool descriptions (coverage=full)

Все 25 инструментов. Описание = docstring функции (FastMCP берёт docstring как `description`). Приведены дословно.

### 1. send_message
```
Send an Instagram direct message to a user by username.

    Args:
        username: Instagram username of the recipient.
        message: The message text to send.
    Returns:
        A dictionary with success status and a status message.
```

### 2. send_photo_message
```
Send a photo via Instagram direct message to a user by username.

    Args:
        username: Instagram username of the recipient.
        photo_path: Path to the photo file to send.
        message: Optional message text to accompany the photo.
    Returns:
        A dictionary with success status and a status message.
```

### 3. send_video_message
```
Send a video via Instagram direct message to a user by username.

    Args:
        username: Instagram username of the recipient.
        video_path: Path to the video file to send.
    Returns:
        A dictionary with success status and a status message.
```

### 4. list_chats
```
Get Instagram Direct Message threads (chats) from the user's account, with optional filters and limits.

    Args:
        amount: Number of threads to fetch (default 20).
        selected_filter: Filter for threads ("", "flagged", or "unread").
        thread_message_limit: Limit for messages per thread.
        full: If True, return the full thread object for each chat (default False).
        fields: If provided, return only these fields for each thread.
    Returns:
        A dictionary with success status and the list of threads or error message.
```

### 5. list_messages
```
Get messages from a specific Instagram Direct Message thread by thread ID, with an optional limit.

    Args:
        thread_id: The thread ID to fetch messages from.
        amount: Number of messages to fetch (default 20).
    Returns:
        A dictionary with success status and the list of messages or error message.
```

### 6. mark_message_seen
```
Mark a message as seen in a direct message thread.

    Args:
        thread_id: The thread ID containing the message.
        message_id: The ID of the message to mark as seen.
    Returns:
        A dictionary with success status and a status message.
```

### 7. list_pending_chats
```
Get Instagram Direct Message threads (chats) from the user's pending inbox.

    Args:
        amount: Number of pending threads to fetch (default 20).
    Returns:
        A dictionary with success status and the list of pending threads or error message.
```

### 8. search_threads
```
Search Instagram Direct Message threads by username or keyword.

    Args:
        query: The search term (username or keyword).
    Returns:
        A dictionary with success status and the search results or error message.
```

### 9. get_thread_by_participants
```
Get an Instagram Direct Message thread by participant user IDs.

    Args:
        user_ids: List of user IDs (ints).
    Returns:
        A dictionary with success status and the thread or error message.
```

### 10. get_thread_details
```
Get details and messages for a specific Instagram Direct Message thread by thread ID, with an optional message limit.

    Args:
        thread_id: The thread ID to fetch details for.
        amount: Number of messages to fetch (default 20).
    Returns:
        A dictionary with success status and the thread details or error message.
```

### 11. get_user_id_from_username
```
Get the Instagram user ID for a given username.

    Args:
        username: Instagram username.
    Returns:
        A dictionary with success status and the user ID or error message.
```

### 12. get_username_from_user_id
```
Get the Instagram username for a given user ID.

    Args:
        user_id: Instagram user ID.
    Returns:
        A dictionary with success status and the username or error message.
```

### 13. get_user_info
```
Get detailed information about an Instagram user.

    Args:
        username: Instagram username to get information about.
    Returns:
        A dictionary with success status and user information.
```

### 14. check_user_online_status
```
Check the online status of Instagram users.

    Args:
        usernames: List of Instagram usernames to check status for.
    Returns:
        A dictionary with success status and users' presence information.
```

### 15. search_users
```
Search for Instagram users by name or username.

    Args:
        query: Search term (name or username).
        count: Maximum number of users to return (default 10, max 50).
    Returns:
        A dictionary with success status and search results.
```

### 16. get_user_stories
```
Get Instagram stories from a user.

    Args:
        username: Instagram username to get stories from.
    Returns:
        A dictionary with success status and stories information.
```

### 17. like_media
```
Like or unlike an Instagram post.

    Args:
        media_url: URL of the Instagram post.
        like: True to like, False to unlike the post.
    Returns:
        A dictionary with success status and a status message.
```

### 18. get_user_followers
```
Get followers of an Instagram user.

    Args:
        username: Instagram username to get followers for.
        count: Maximum number of followers to return (default 20).
    Returns:
        A dictionary with success status and followers list.
```

### 19. get_user_following
```
Get users that an Instagram user is following.

    Args:
        username: Instagram username to get following list for.
        count: Maximum number of following to return (default 20).
    Returns:
        A dictionary with success status and following list.
```

### 20. get_user_posts
```
Get recent posts from an Instagram user.

    Args:
        username: Instagram username to get posts from.
        count: Maximum number of posts to return (default 12).
    Returns:
        A dictionary with success status and posts list.
```

### 21. list_media_messages
```
List all messages containing media in an Instagram direct message thread.
    Args:
        thread_id: The ID of the thread to check for media messages
        limit: Maximum number of messages to check (default 100, max 200)
    Returns:
        A dictionary containing success status and list of all media messages found
```

### 22. download_media_from_message
```
Download media from a specific Instagram direct message and get the local file path.
    Args:
        message_id: The ID of the message containing the media
        thread_id: The ID of the thread containing the message
        download_path: Directory to save the downloaded file (default: ./downloads)
    Returns:
        A dictionary containing success status, a status message, and the file path if successful
```

### 23. download_shared_post_from_message
```
Download media from a shared post/reel/clip in a DM message and get the local file path.
    Args:
        message_id: The ID of the message containing the shared post/reel/clip
        thread_id: The ID of the thread containing the message
        download_path: Directory to save the downloaded file (default: ./downloads)
    Returns:
        A dictionary containing success status, a status message, and the file path if successful
```

### 24. delete_message
```
Delete a message from a direct message thread.

    Args:
        thread_id: The thread ID containing the message.
        message_id: The ID of the message to delete.
    Returns:
        A dictionary with success status and a status message.
```

### 25. mute_conversation
```
Mute or unmute a direct message conversation.

    Args:
        thread_id: The thread ID to mute/unmute.
        mute: True to mute, False to unmute the conversation.
    Returns:
        A dictionary with success status and a status message.
```
