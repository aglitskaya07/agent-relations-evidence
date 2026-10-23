# UNIT: claude-ai:Gmail | коннектор claude.ai | captured 2026-07-29 (session ToolSearch)

## CHANNEL: instructions
(не доставлены в системный промпт сессии 2026-07-29)

## CHANNEL: tool descriptions, connector (16 tools, via ToolSearch)

### tool: search_threads
Lists email threads from the authenticated user's Gmail account.

This tool can filter threads based on a query string and supports pagination. It returns a list of threads, including their IDs and related messages. Each related message contains details like a snippet of the message body, the subject, the sender, the recipients etc. The `view` parameter controls which fields are populated in the related messages. By default (or with `THREAD_VIEW_MINIMAL`), it includes subject and snippet. Use `THREAD_VIEW_METADATA_ONLY` to exclude subject and snippet. Note that the full message bodies are not returned by this tool; use the 'get_thread' tool with a thread ID to fetch the full message body if needed. Threads with excluded criteria may still appear in the results. This occurs because Gmail identifies matching messages first. For example, if you search for -is:starred, Gmail will find an entire thread if it contains at least one unstarred message, even if other emails in that same conversation are starred.

### tool: get_thread
Retrieves a specific email thread from the authenticated user's Gmail account, including a list of its messages.

The optional `messageFormat` parameter controls the format of the messages returned. By default (or with `FULL_CONTENT`), it returns the full content of messages. Use `MINIMAL` to include only subject and snippet (excluding body). Use `METADATA_ONLY` to include only basic metadata (message ID, thread ID, labels, timestamp, and size estimate).

### tool: get_message
Retrieves a specific email message from the authenticated user's Gmail account by its unique message ID.

Use this tool to inspect a single, individual email when you already know its message ID. If the user wants to read a specific email in detail, check the exact wording of a message, or examine attachment metadata for a single email, this is the right tool. It is not suitable for retrieving entire conversations or viewing back-and-forth discussion threads; use the 'get_thread' tool instead.
Key indicators include if the user asks for the full content of a specific message ID returned by a previous search, or if the query asks to inspect a specific individual email rather than an entire thread.
Example user prompts are: "Get the full text of message ID 18f123456789abcd.", "Read the latest message in that thread from Alice.", and "What are the attachment names in the email I just received from HR?"

The optional `messageFormat` parameter controls the format of the message returned. By default (or with `FULL_CONTENT`), it returns the full content of the message. Use `MINIMAL` to include only subject and snippet (excluding body). Use `METADATA_ONLY` to include only basic metadata (message ID, thread ID, labels, timestamp, and size estimate).

### tool: create_draft
Creates a new draft email in the authenticated user's Gmail account.

This tool takes recipient addresses, a subject, and body content as inputs. If the draft is created as a reply to an existing message, the ID of the original message should be passed to the tool in the replyToMessageId field.

Returns only the unique ID (id) of the draft message.

Limitation: Creating drafts with attachments is not supported yet.

### tool: update_draft
Updates an existing draft email in the authenticated user's Gmail account.

### tool: list_drafts
Lists draft emails from the authenticated user's Gmail account.

This tool can filter drafts based on a query string and supports pagination. It returns a list of drafts, including their IDs and subjects (unless `view` is set to `DRAFT_VIEW_METADATA_ONLY`). `page_token` can be used to paginate the results. To retrieve subsequent pages of results, use the `page_token` returned in the previous response.

The `view` parameter controls which fields are populated in the response. By default (or with `DRAFT_VIEW_FULL`), it returns full content. Use `DRAFT_VIEW_METADATA_ONLY` to exclude sensitive content like subject and body.

### tool: list_labels
Lists all labels available in the authenticated user's Gmail account. Use this tool to discover the `id` of a label before calling `label_thread`, `unlabel_thread`, `label_message`, or `unlabel_message`. Note: the system labels, `DRAFT` and `SENT`, cannot be set on messages and are read only.

### tool: create_label
Creates a new label in the authenticated user's Gmail account.
Supports creating nested labels (sub-labels) using a forward slash (e.g., 'Projects/Alpha/Sprint-1').
By default, parent labels will be automatically created if they do not exist.

### tool: update_label
Modifies an existing label's name and color in the user's Gmail account.

### tool: delete_label
Deletes a label in the authenticated user's Gmail account.

### tool: label_message
Adds one or more labels to a specific message in the authenticated user's Gmail account.

To find the message ID, use tools like `search_threads` or `get_thread`. If unsure of a user label's ID, use the `list_labels` tool first to discover available labels and their IDs. To add a trash label or a spam label on to a message, please use the `apply_sensitive_message_label` tool instead.

### tool: unlabel_message
Removes one or more labels from a specific message in the authenticated user's Gmail account. To find the message ID, use tools like `search_threads` or `get_thread`. If unsure of a user label's ID, use the `list_labels` tool first to discover available labels and their IDs.

### tool: label_thread
Adds labels to an entire thread in the authenticated user's Gmail account. This operation affects all messages currently in the thread and any future messages added to it.

If unsure of the thread ID, use the `search_threads` tool first.

If unsure of a user label's ID, use the `list_labels` tool first to discover available labels and their IDs. To add a trash label or a spam label on to a thread, please use the `apply_sensitive_thread_label` tool instead.

### tool: unlabel_thread
Removes labels from an entire thread in the authenticated user's Gmail account. If unsure of the thread ID, use the `search_threads` tool first. If unsure of a user label's ID, use the `list_labels` tool first.

### tool: apply_sensitive_message_label
Adds a sensitive label (Trash or Spam) to a specific message in the authenticated user's Gmail account.

Use this tool to trash or mark a message as spam. To find the message ID, use tools like `search_threads` or `get_thread`.

### tool: apply_sensitive_thread_label
Adds a sensitive label (Trash or Spam) to an entire thread in the authenticated user's Gmail account. This operation affects all messages currently in the thread and any future messages added to it.

Use this tool to trash or mark a thread as spam. If unsure of the thread ID, use the `search_threads` tool first.
