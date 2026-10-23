# UNIT: claude-ai:Granola | коннектор claude.ai | captured 2026-07-29 (connector tool list)

## CHANNEL: instructions
(коннектор не передает блок инструкций, 2026-07-29)

## CHANNEL: tool descriptions, connector (6 tools, via ToolSearch)

### tool: get_account_info
Get the email and active workspace for the Granola account currently connected to this MCP session.

When to use:
- User asks 'who am I signed in as?', 'which Granola account is this?', or 'what's my email?'
- User suspects they connected the wrong Granola account
- Before performing actions, to confirm identity if the user references a specific account

### tool: get_meeting_transcript
Get the full transcript for a specific Granola meeting by ID. Returns only the verbatim transcript content, not summaries or notes.
Speaker labels: `Me` is the note-taker, `Them` is other unidentified participants, and named speakers are shown by name.
Use this when the user needs exact quotes, specific wording, or wants to review what was literally said in a meeting. For summarized content or action items, use query_granola_meetings or list_meetings/get_meetings instead.

### tool: get_meetings
Get detailed meeting information for one or more Granola meetings by ID. Returns private notes, AI-generated summary, attendees, and metadata.
Use this when you already have specific meeting IDs (e.g. from list_meetings results). For open-ended questions about meeting content, use query_granola_meetings instead.

### tool: list_meeting_folders
List the user's Granola meeting folders. Returns folder ID, title, description, and note count including nested folders.

When to use:
- User asks about their folders or wants to browse meetings by folder
- User wants to narrow down meeting searches to a specific folder

Use the returned folder IDs with list_meetings (folder_id parameter) to list meetings within a specific folder.

### tool: list_meetings
List the user's Granola meeting notes within a time range. Returns meeting titles and metadata.

IMPORTANT: For short-term questions about recent meeting details, prefer using query_granola_meetings instead.

When to use:
- User asks to list their meetings
- User asks about action items, decisions, or summaries from meetings over a longer or specific date range
- User asks about content from their meeting transcripts
- User references 'Granola notes' or 'meeting notes' or 'transcripts'

When NOT to use:
- User is asking about upcoming calendar events or scheduling
- User wants to create/modify calendar invites

Use get_meetings to retrieve detailed meeting content after identifying relevant meetings.
Use list_meeting_folders to discover folder IDs, then pass a folder_id to list meetings within a specific folder.

### tool: query_granola_meetings
Query Granola about the user's meetings using natural language. Returns a tailored response with inline citation links in mark  (e.g. [[0]](url)) that reference source meeting notes.

IMPORTANT: The response includes numbered citation links to specific Granola meeting notes. These citations MUST be preserved in your response to the user — they provide transparency and allow the user to verify information by clicking through to the original notes.

When to use:
- User asks about what was discussed, decided, or action-items from meetings
- User asks about follow-ups, todos, or commitments from recent meetings
- User references 'Granola notes' or 'meeting notes'

When NOT to use:
- User is asking about calendar scheduling or upcoming events
- User explicitly asks for a specific meeting by ID (use get_meetings instead)

Prioritize using query_granola_meetings over list_meetings/get_meetings for open-ended or natural language queries about meeting content.
