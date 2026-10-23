# UNIT: claude-ai:Google_Calendar | коннектор claude.ai | captured 2026-07-29 (connector tool list)

## CHANNEL: instructions
(коннектор не передает блок инструкций, 2026-07-29)

## CHANNEL: tool descriptions, connector (9 tools, via ToolSearch)
### tool: create_event
Creates an event on the given calendar.

### tool: delete_event
Deletes an event on the given calendar.

### tool: get_event
Returns a single event on the given calendar.

### tool: list_calendars
Returns the calendars this user has access to (their calendar list). Use this tool to resolve calendar identifying data (for example, 'my family calendar') into its corresponding `calendar_id` (email identifier)

### tool: list_events
Returns events on the given calendar matching all specified constraints. Time constraints should not be specified unless requested by the user. For open-ended keyword or topic-based searches on the primary calendar, the search_events tool must be used instead.

### tool: respond_to_event
Responds to an event on a calendar.

### tool: search_events
Searches events on the user's primary calendar using semantic search.

### tool: suggest_time
Suggests time periods across one or more calendars.

### tool: update_event
Updates an event on the given calendar.
