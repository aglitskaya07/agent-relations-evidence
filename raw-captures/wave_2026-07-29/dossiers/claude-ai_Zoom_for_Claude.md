# UNIT: claude-ai:Zoom_for_Claude | коннектор claude.ai | captured 2026-07-29 (connector tool list)

## CHANNEL: instructions
(коннектор не передает блок инструкций, 2026-07-29)

## CHANNEL: tool descriptions, connector (9 tools, via ToolSearch)

### tool: get_file_content
## Tool Description
[DEPRECATED] This tool is deprecated. Please use `hub_get_file_content` instead for all future file content retrieval tasks.

Retrieves the full Markdown content and file name of an existing Zoom Docs (Zoom Canvas) document using its file ID.

## When to Use
⚠️ **This tool is deprecated. Use `hub_get_file_content` as the replacement.**

Only use this tool as a fallback if `hub_get_file_content` is unavailable. Use this tool when you need to read the full content of a Zoom Docs file by its file ID, in either structured XML format (for block-level editing) or plain Markdown format (for reading only).

## Must Do
- Always prefer `hub_get_file_content` over this tool for all new tasks.
- Use `xml` format when block-level editing is planned, as it is the ONLY format that exposes block IDs required by block-level edit tools (docs_file_insert_blocks, docs_file_update_block, docs_file_delete_block, docs_file_replace_range_of_blocks).
- Use `markdown` format only when plain text reading is sufficient and no block-level editing is needed.

## Must NOT Do
- Do NOT use `markdown` format when block-level editing is planned, as it does not expose block IDs.

### tool: get_meeting_assets
# Get Meeting Assets V4.0

**READ-ONLY**

Retrieve all available assets for a specific Zoom meeting, including AI summaries, My Notes, cloud recordings, whiteboards, Zoom Docs, agenda documents, and participants.

## When to use this tool

- User wants to retrieve assets for a completed meeting
- User needs access to meeting summaries,My Notes, recordings, whiteboards, Zoom Docs, agenda, or participant information
- User provides a meeting identifier (numeric meeting ID or UUID)

**Required condition:** User must provide a meeting ID (numeric or UUID format) to use this tool.

## Parameters

### `meetingId` (String, Required)

The meeting identifier. Accepts either:

1. **UUID** (preferred) — e.g., `"38DCDB7C-74B1-442F-BE85-390DF0BB96CC"`. Targets a specific meeting instance.
2. **Numeric meeting ID** — e.g., `"123456789"`. Returns assets for the latest meeting instance when multiple instances exist.


Always prefer UUID when available; numeric ID cannot target specific past instances of recurring meetings.

## Response

Returns a JSON object containing the following asset fields (each may be `null` if unavailable):

- `meeting_summary` — AI-generated summary with quick recap, full text, and next steps
- `my_notes` — User notes and participant transcripts recorded during the meeting
- `recording` — Cloud recording with play URL, duration, and processing status
- `whiteboards` — Whiteboards shared or created during the meeting
- `docs` — Zoom Docs linked to the meeting
- `agenda_doc` — Agenda document associated with the meeting
- `participants` — Meeting participant list

## Access Control

Only the meeting host or participants explicitly granted access by the host can retrieve meeting assets. Unauthorized requests return a permission error.

## Error Handling

| Error | Meaning |
|-------|---------|
| 403 / Permission denied | User lacks access to this meeting's assets. |
| 404 / Not found | Invalid, expired, or unrecognized meeting ID/UUID. |

## Usage Notes

- Cloud recordings may show `processing: true` while… [обрезано механизмом ToolSearch]

### tool: get_recording_resource
**Description:**

Retrieves detailed content and metadata for a specific Zoom recording, including transcript text, topic summaries, next steps/action items, and playback URLs. Use this tool when the user explicitly mentions "recording" or requests content-level details (e.g., "What did they say about X?", "Play the recording", "Find the part where they discussed pricing"). For general meeting discovery or meeting-level metadata without recording context, prefer the Assets tool.

**Parameters:**

- **types** *(string, optional)*: Comma-separated list of resource types to retrieve. Valid values: `transcript`, `summary`, `nextStep`, `playUrl`. If omitted or empty, all available types are returned. Include `transcript` when answering content questions; include both `transcript` and `playUrl` when the user wants to jump to a specific moment.

- **raw_passcode** *(string, optional)*: Plaintext passcode for the recording (up to 10 characters; letters, digits, or special characters).

- **encode_passcode** *(string, optional)*: Encrypted passcode from the `pwd=` parameter of a Zoom share link.

- **clip_num** *(integer, optional)*: 1-based index of the clip to retrieve for multi-clip recordings. Returns null if the index exceeds available clips.

- **play_time** *(integer, optional)*: Playback start time in seconds within the selected clip (e.g., `20` = start 20 seconds in). Use transcript timestamps to determine the appropriate value when the user asks to jump to a specific topic.

**Return Schema Overview:**

```json
{
  "transcripts": [{ "timeline": [{ "text", "ts", "end_ts", "display_name" }], "recording_id", "meeting_id", "recording_start", "recording_end" }],
  "summaries":   [{ "overall_summary", "items": [{ "label", "summary" }], "recording_start", "total_items" }],
  "next_steps":  [{ "items": [{ "text" }], "recording_start", "total_items" }],
  "play_urls":   [{ "urls": ["string"], "recording_start", "play_time" }]
}
```

Fields are omitted if no data exists for that type.

**Usage Notes:**

- Recording durati… [обрезано механизмом ToolSearch]

### tool: hub_create_file_from_content
## Tool Description
Creates a new Zoom Hub file (doc, paper_doc, or spreadsheet) from plain-text content and returns the file ID and deep link.

## Prerequisites
- `parent_id` is OPTIONAL.
- DO NOT specify `parent_id` unless the user explicitly tells you where to save the file.
- If the user does not mention a folder or location, omit `parent_id` entirely — do not default it to "root" or empty string.
- Only provide `parent_id` when the user explicitly provides a valid folder ID or path.

✅ Correct: omit parent_id when user says "Generate a sample sales spreadsheet for me."
❌ Wrong:   parent_id = "root"  ← do not assume this as default

## When to Use
Use this tool when the user wants to create a new document, paper document, or spreadsheet in Zoom Hub with specific text content (Markdown for docs/paper_docs, CSV for spreadsheets).

## Prerequisites
- For `parent_id`: use empty string or `"root"` to place in the caller's My Files folder, or provide a valid folder ID owned by or shared with the caller

## Must Do
- Set `file_type` to one of: `doc`, `paper_doc`, or `spreadsheet`
- Use **Markdown format** for `doc` or `paper_doc` content
- Use **CSV format** for `spreadsheet` content
- Keep `content` size ≤ 100 KB

## Must NOT Do
- Do **not** use `file_type=presentation` — slide-deck import is not supported

## Error Handling
- `400 REASON_PARAMS_INVALID`: Invalid parameters (e.g., attempting to create a presentation or exceeding content size limit)

### tool: hub_get_file_content
## Tool Description
Exports the plain-text content of a Zoom Hub file (doc, spreadsheet, presentation, or paper_doc) in a specified format (markdown, xml, or csv).

## File ID Extraction from URL
If the user provides a Zoom Hub spreadsheet URL, extract file_id using this rule:

URL pattern:
https://<host>/spreadsheet/{file_id}
https://<host>/spreadsheet/{file_id}/{sheet_id}
https://<host>/spreadsheet/{file_id}/{sheet_id}?...

- Always extract ONLY the first path segment after `/spreadsheet/` as `file_id`
- The second path segment is the Sheet Tab ID — it is NOT part of file_id, ignore it
- Query parameters (e.g., ?from=sheets) should also be ignored

✅ Examples:
https://sheets.zoomd.us/spreadsheet/orLkROyAQvuIBEWFnj6F7g
→ file_id = "orLkROyAQvuIBEWFnj6F7g"

https://sheets.zoomd.us/spreadsheet/orLkROyAQvuIBEWFnj6F7g/q2sbq?from=sheets
→ file_id = "orLkROyAQvuIBEWFnj6F7g"

❌ Wrong:
file_id = "orLkROyAQvuIBEWFnj6F7g/q2sbq"  ← never include sheet_id in file_id

## When to Use
Use this tool when you need to read or extract the textual content of a Zoom Hub file for analysis, display, or processing.

## Prerequisites
- You must have a valid `file_id` for an existing Hub file
- The file type must support the requested export format (see format compatibility below)

## Must Do
- Provide both `file_id` and `format` parameters (both required)
- Ensure the `format` matches the file type:
    - **doc**: use `markdown` or `xml`
    - **spreadsheet**: use `csv` (only first sheet exported)
    - **presentation**: use `markdown`
    - **paper_doc**: use `markdown`

## Must NOT Do
- Do not request a format incompatible with the file type (returns 400 error)
- Do not attempt to export files larger than 100 KB (bounded by size limit, returns 400 error)

## Error Handling
- **400 REASON_PARAMS_INVALID**: Mismatched file type and format combination, or file size exceeds 100 KB limit

### tool: recordings_list
List user all recordings
Lists all [cloud recordings](https://support.zoom.us/hc/en-us/articles/203741855-Cloud-Recording) for a user.

### tool: search_zoom
# Search Zoom

**READ-ONLY**

Advanced search functionality for `chat` and `zoom_doc`. Performed keyword and semantic search across the user's collaboration content to build search experiences and knowledge discovery workflows across Team Chat Message and Zoom Docs Notes. Returns relevance-ranked results(top-K) with rich metadata.


## Parameters

- **`query`** (string, optional) — Keyword or phrase to search. Omit to browse without a keyword.
- **`page_size`** (integer, optional) — Results per page, 1–100, default 10. No pagination cursor; only a single page is returned.
- **`search_entities`** (array, required) — One or more source types. Each item contains `entity_type` (`chat` or `zoom_doc`) and an optional `filters` object.

### Chat filters (`entity_type: "chat"`)

- `channel_names` (string array) — Filter by channel display name.
- `hsession_ids` (string array) — Scope to sessions returned by a previous search response.
- `from` / `to` (ISO 8601 UTC) — Time range.
- `unread` (boolean) — Return only channels with unread messages.

### Zoom Doc filters (`entity_type: "zoom_doc"`)

- `doc_view` (string enum): `recent`, `my_docs`, `shared_with_me`, `starred`, `notes`.
  - `notes` refers to AI-generated meeting notes from Zoom AI Companion, not user-created documents.
- `from` / `to` (ISO 8601 UTC) — Time range filtered by the document's last modified time.

## Response

Returns `{ "data": [...] }` where each item is discriminated by `entity_type`:

- **Chat**: `channel_name`, `message_list` (with `message`, `send_user`, `created_time`, `modified_time`, `comments`). Internal IDs: `hsession_id`, `message_id`, `thread_id`.
- **Zoom Doc**: `title`, `file_type`, `link`, `create_time`, `modify_time`. Internal IDs: `file_id`, `ancestors`.

## Usage Notes

- All `from`/`to` values accept ISO 8601 UTC only. Interpret time references in the user's timezone, convert to UTC, then format as ISO 8601. Relative expressions (e.g. "yesterday", "last week") follow the same local → UTC → ISO 8601 pipeline.
- When the user mentio… [обрезано механизмом ToolSearch]

### tool: create_new_file_with_markdown
## Tool Description
⚠️ DEPRECATED: This tool has been replaced by `hub_create_file_from_content`. 
DO NOT use this tool. Use `hub_create_file_from_content` instead for creating files with Markdown content.

## When to Use
DO NOT use this tool. It is deprecated and no longer maintained.

## Must NOT Do
- DO NOT call this tool for any new requests.
- DO NOT use this tool when the user wants to create a file with content.

## Migration
Use `hub_create_file_from_content` as the direct replacement for all file creation with Markdown content tasks.

### tool: search_meetings
# Search Meetings V4.4

**READ-ONLY**

Advanced search functionality for user meetings. AI analyzes user input to identify keywords (`q`) and time ranges (`from`, `to`), then uses these extracted parameters to query the user's meeting list, sorting results by relevance.
Additionally, there is a specific query condition: whether to include "My Notes" (`include_zoom_my_notes`) in the results. When the user explicitly indicates a desire to search for "My Notes or Notes," please set `include_zoom_my_notes` to `true`.
Before invoking this tool, you must first obtain the user's current time zone; invoking this tool without knowing the user's current time zone is strictly prohibited. If the current time zone is unknown, please ask the user for it first.

## When to use this tool

- User asks about meetings without providing a specific Meeting ID (e.g., "Find the budget review", "What meetings did I have last week?")
- User wants to locate a meeting by topic, summary content, transcript content, attendee name, or date range

## Response

Returns a JSON object containing:

- `total` — Total number of matching meetings
- `meetings` — Array of meeting objects, each including:
  - `meeting_uuid` — UUID identifier for the specific meeting instance
  - `meeting_number` — Numeric meeting ID
  - `topic` — Meeting title
  - `schedule_start_time` — Scheduled start time (UTC)
  - `meeting_status` — e.g., `HISTORY` (past) or `SCHEDULED` (upcoming)
  - Additional meeting metadata (host, duration, timezone, etc.)
- `next_page_token` — Token for retrieving the next page (if more results exist)

## Usage Notes

- When passing `meeting_uuid` from search results to downstream tools (e.g., `get_meeting_assets`).
- Prefer `meeting_uuid` over `meeting_number` for downstream tool calls — it identifies the exact meeting instance.
- For "recent" or "today" queries, set `from` to the start of the current day in UTC rather than using the default 7-day window.
- For upcoming/future meeting queries, set `from` to the current time.
- The user's time… [обрезано механизмом ToolSearch]
