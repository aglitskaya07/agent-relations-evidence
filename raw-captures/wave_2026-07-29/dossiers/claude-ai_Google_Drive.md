# UNIT: claude-ai:Google_Drive | коннектор claude.ai | captured 2026-07-29 (connector tool list)

## CHANNEL: instructions
(коннектор не передает блок инструкций, 2026-07-29)

## CHANNEL: tool descriptions, connector (8 tools, via ToolSearch)

### tool: copy_file
Call this tool to copy an existing File in Google Drive.
The tool allows specifying a new title and a parent folder for the copy.
If the title is not specified, the copy title will be 'Copy of {original title}'If the parent folder is not specified, the copy will be created in the same folder as the original file, unless the requesting user does not have write access to that folder, in which case the copy will be created in the user's root folder.Returns the newly created File object upon successful copying.

### tool: create_file
Call this tool to create or upload a File to Google Drive.

If uploading content, prefer "text_content" for text content. For non-UTF8 contents, use the "base64_content" field and base64 encode the data to set on that field.

Returns a single File object upon successful creation.

The following Google first-party mime types can be created without providing content:

 - `application/vnd.google-apps.document` 
 - `application/vnd.google-apps.spreadsheet` 
 - `application/vnd.google-apps.presentation` 

Folders can be created by setting the mime type to `application/vnd.google-apps.folder`.

When uploading content, the `content_mime_type` field is required and should match the type of the content being uploaded.

By default, supported content will be converted to Google first-party mime types.

To disable conversions for first-party mime types, set `disable_conversion_to_google_type` to true.

### tool: download_file_content
Call this tool to download the content of a Drive file as a base64 encoded string.

If the file is a Google Drive first-party mime type, the `exportMimeType` field is required and will determine the format of the downloaded file.

If the file is not found, try using other tools like `search_files` to find the file the user is requesting.

If the user wants a natural language representation of their Drive content, use the `read_file_content` tool (`read_file_content` should be smaller and easier to parse).

### tool: get_file_metadata
Call this tool to find general metadata about a user's Drive file.

If the file is not found, try using other tools like `search_files` to find the file the user is requesting.

### tool: get_file_permissions
Call this tool to list the permissions of a Drive File.

### tool: read_file_content
Call this tool to fetch a natural language representation of a known Drive file, and if specified, its comments.

REQUIREMENTS & WORKFLOW:
 - `fileId` is required. You MUST pass an exact Drive file ID returned by a previous discovery tool (`search_files` or `list_recent_files`) or provided explicitly in the user prompt.
 - NEVER guess, invent, or hallucinate a `fileId` string from a file title or name.
 - If given a file title, name, or topic without an explicit `fileId`, you MUST FIRST call `search_files` to find the file and retrieve its `fileId` before invoking this tool.

The file content may be incomplete for very large files. The text representation will change over time, so don't make assumptions about the particular format of the text returned by this tool. If supported and specified, comment tags will be included in the content.

Supported Mime Types:

 - `application/vnd.google-apps.document` (supports comments)
 - `application/vnd.google-apps.presentation` (supports comments)
 - `application/vnd.google-apps.spreadsheet` (supports comments)
 - `application/pdf` 
 - `application/msword` 
 - `application/vnd.openxmlformats-officedocument.wordprocessingml.document` 
 - `application/vnd.openxmlformats-officedocument.spreadsheetml.sheet` 
 - `application/vnd.openxmlformats-officedocument.presentationml.presentation` 
 - `application/vnd.oasis.opendocument.spreadsheet` 
 - `application/vnd.oasis.opendocument.presentation` 
 - `application/x-vnd.oasis.opendocument.text` 
 - `image/png` 
 - `image/jpeg` 
 - `image/jpg` 

If the file is not found, try using other tools like `search_files` to find the file the user is requesting using keywords.

### tool: search_files
Search for Drive files using a structured query (syntax: `query_term operator values`). Only terms in this list are supported.
Combine clauses with `and`, `or`, `not`, and parentheses. String values must be single-quoted; escape embedded quotes as `\'`.
Do NOT include document type terms (e.g., 'presentation', 'slides', 'deck', 'document', 'doc', 'spreadsheet', 'sheet', 'pdf', 'folder') inside `title contains '...'` or `fullText contains '...'` clauses. Separate title keywords from file type terms. Instead map them to `mimeType` clauses in the query (e.g., 'slides' -> `mimeType = 'application/vnd.google-apps.presentation'`).

Query terms & operators:

 - `title` (ops: contains, =, !=) — file title
 - `fullText` (ops: contains) — title or body text
 - `mimeType` (ops: contains, =, !=) — MIME type
 - `modifiedTime`, `viewedByMeTime`, `createdTime` (ops: `<=`, `<`, `=`, `!=`, `>`, `>=`). Use RFC 3339 UTC, e.g., `2012-06-04T12:00:00-08:00`. Date types not comparable.
 - `parentId` (ops: `=`, `!=`). Use `'root'` for the user's "My Drive".
 - `owner` (ops: `=`, `!=`). Use `'me'` for the requesting user.
 - `sharedWithMe` (ops: `=`, `!=`). Values: `true` or `false`.

Other operators: `and`, `or`, `not`.

Examples:

 - `title contains 'hello' and title contains 'goodbye'`
 - `modifiedTime > '2024-01-01T00:00:00Z' and (mimeType contains 'image/' or mimeType contains 'video/')`
 - `parentId = '1234567'`
 - `fullText contains 'hello'`
 - `owner = 'test@example.org'`
 - `sharedWithMe = true`
 - `owner = 'me'` (for files owned by the user)

Use `next_page_token` to paginate. An empty response means no more results.

### tool: list_recent_files
Call this tool to find recent files for a user specified a sort order. Default sort order is `recency`.

Supported sort orders are:

 - `recency`: The most recent timestamp from the file's date-time fields.
 - `lastModified`: The last time the file was modified by anyone.
 - `lastModifiedByMe`: The last time the file was modified by the user.

The default page size is 10. Utilize `next_page_token` to paginate through the results.
