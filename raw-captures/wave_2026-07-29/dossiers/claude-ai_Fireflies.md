# UNIT: claude-ai:Fireflies | коннектор claude.ai | captured 2026-07-29 (connector tool list)

## CHANNEL: instructions
(коннектор не передает блок инструкций, 2026-07-29)

## CHANNEL: tool descriptions, connector (20 tools, via ToolSearch)

### tool: fireflies_get_active_meetings
Retrieves a list of currently active (in-progress) meetings from Fireflies.ai. Returns meeting details including ID, title, organizer, meeting link, start/end time, privacy, and state. Admins can query active meetings for any user; regular users can only query their own.

### tool: fireflies_get_analytics
Retrieves team and per-user meeting and conversation analytics from Fireflies.ai. Returns meeting counts, durations, conversation metrics (filler words, questions, monologues, sentiment, talk-listen ratio, words per minute), and comparison data against previous periods. Accepts optional start_time and end_time filters in ISO 8601 format. Team-level analytics require admin privileges.

### tool: fireflies_create_soundbite
Creates a soundbite (clip) from a meeting transcript. A soundbite is a short audio/video segment extracted from a meeting. The authenticated user must have write access to the meeting. Requires the transcript ID and start/end times (in seconds).

### tool: fireflies_fetch
Retrieve complete meeting transcript with full conversation, metadata, and insights for a specific meeting ID. Use this after search to get detailed content.

### tool: fireflies_get_channel
Retrieves details of a specific channel/folder by its ID. Returns channel title, privacy setting, and member list.

### tool: fireflies_get_rule_executions
Retrieves rule execution logs grouped by meeting. Shows which automation rules were triggered on meetings, including the actions taken (sharing, moving to channels, changing privacy). Requires Enterprise tier access. Results are paginated.

### tool: fireflies_get_soundbites
Fetches soundbites (short shareable audio/transcript clips from meetings). Can filter by transcript, ownership, or team. At least one of mine, transcript_id, or my_team must be provided.

### tool: fireflies_get_summary
Fetches meeting summary by ID, with optional field filtering. Returns summary data (keywords, action items, overview, etc.) and basic metadata, but excludes transcript content. If you need transcript content, use fireflies_get_transcript instead.

### tool: fireflies_get_transcript
Fetches detailed meeting transcript by ID, with optional field filtering. Returns transcript content (sentences, speakers) and metadata, but excludes summary data. Each sentence is prefixed with its timestamp range (e.g. "[00:05 - 00:08] Speaker: text") so moments can be anchored back to the recording. If you need summary data, use fireflies_get_summary instead. If the meeting is currently live (is_live: true), the transcript returned is a point-in-time snapshot of the live transcript with sentences captured so far.

### tool: fireflies_get_transcripts
Queries multiple meeting transcripts using filter properties (date, keyword, email, etc.). Returns basic metadata and transcript summary. Does NOT accept transcriptId as input - use fireflies_get_transcript() multiple times to get detailed transcript content.

### tool: fireflies_get_user
Fetches user account details. Returns profile info, transcript counts, meeting activity, and admin status. If no user ID provided, returns current authenticated user data.

### tool: fireflies_get_user_contacts
Fetches contact list for the authenticated user. Returns contacts with their names, emails, profile pictures, and last meeting dates sorted by most recent interaction.

### tool: fireflies_get_usergroups
Fetches user groups for the authenticated user or their team. Returns group details including name, handle, and members. Use mine=true to get only groups the user belongs to, or mine=false (default) to get all groups in the team.

### tool: fireflies_list_channels
Lists all channels/folders available to the authenticated user. Returns channel details including ID, title, privacy setting, and members.

### tool: fireflies_move_meeting
Moves one or more meeting transcripts to a specified channel/folder. The authenticated user must be the owner of the meetings or a team admin. Up to 5 meeting IDs can be provided.

### tool: fireflies_revoke_meeting_access
Revokes a previously shared meeting access for a specific email address. The authenticated user must be the owner of the meeting or a team admin.

### tool: fireflies_search
Advanced search for meeting transcripts using a mini grammar. Supports complex queries with multiple filters.

GRAMMAR SYNTAX:
- keyword:"search term" - Search for keywords in the content. If no scope is specified, the default scope is 'all'.
- scope:title|sentences|all - Define the search scope. Options are 'title', 'sentences', or 'all'. The default is 'all'.
- from:YYYY-MM-DD - Filter meetings from this date (ISO format)
- to:YYYY-MM-DD - Filter meetings until this date (ISO format)
- limit:N - Limit results (max 50)
- skip:N - Skip N results for pagination
- organizers:email1@x.com,email2@x.com - Filter by organizer emails (comma-separated)
- participants:email1@x.com,email2@x.com - Filter by participant emails (comma-separated)
- mine:true|false - Filter to only include user's own meetings

EXAMPLES:
- "engineering standup" (simple keyword search)
- "keyword:\"performance\" scope:sentences limit:20"

### tool: fireflies_share_meeting
Shares a meeting transcript with specified email addresses. The authenticated user must be the owner of the meeting or a team admin. Up to 100 emails can be provided. Optionally set an expiry period for the shared access.

### tool: fireflies_update_meeting_privacy
Updates the privacy setting of a meeting transcript. The authenticated user must be the owner of the meeting or a team admin. Privacy options: "owner" (only the owner can view), "participants" (only meeting participants can view), "participatingteammates" (only participants who are teammates can view), "teammates" (all teammates can view), "teammatesandparticipants" (teammates and participants can view), "link" (teammates and anyone with the link can view).

### tool: fireflies_update_meeting_title
Updates the title of a meeting transcript. The authenticated user must be the owner of the meeting or a team admin. The title must be between 5 and 256 characters.
