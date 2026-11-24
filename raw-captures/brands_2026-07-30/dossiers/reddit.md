# UNIT: reddit | Reddit | github karanb192/reddit-mcp-buddy | author type: community | captured 2026-07-29 (static source)

Type: MCP server (TypeScript, @modelcontextprotocol/sdk, `new Server(...)` in `src/mcp-server.ts:183`, stdio + HTTP transport). Confirmed.

## CHANNEL: instructions (1082 chars)

Source: `src/mcp-server.ts:194-211`, second argument of the constructor `new Server(...)`, field `instructions`. Template literal with two interpolations (`${rateLimit}`, `${cacheTTL / 60000}`) — reproduced verbatim, including placeholders.

```
Reddit content browser and analyzer. Access posts, comments, and user data from Reddit.

KEY CONCEPTS:
- Subreddits: Communities like "technology", "science". Use without r/ prefix
- Special subreddits: "all" (entire Reddit), "popular" (trending/default)
- Sorting: "hot" (trending), "new" (recent), "top" (highest score), "rising" (gaining traction), "controversial" (disputed)
- Time ranges: For "top" sort - "hour", "day", "week", "month", "year", "all"
- Post IDs: Short codes like "abc123" from Reddit URLs
- Usernames: Without u/ prefix (use "spez" not "u/spez")

COMMON QUERIES:
- "What's trending on Reddit?" → browse_subreddit with subreddit="all" and sort="hot"
- "Top posts this week in technology" → browse_subreddit with subreddit="technology", sort="top", time="week"
- "Search for AI discussions" → search_reddit with query="artificial intelligence"
- "Get comments on a Reddit post" → get_post_details with URL or just post_id
- "Analyze a Reddit user" → user_analysis with username

Rate limits: ${rateLimit} requests/minute. Cache TTL: ${cacheTTL / 60000} minutes.
```

Nearby in the code is the author's comment (`src/mcp-server.ts:192-193`), not part of the channel:
```
// Guidance the client shows the model. This must be `instructions` —
// a `description` field on serverInfo is dropped by the protocol.
```

## CHANNEL: tool descriptions (coverage=full)

Source: `src/mcp-server.ts:217-248`, the `const toolDefinitions: Tool[]` array. 5 tools total, all included verbatim. All are marked `annotations: { readOnlyHint: true }`.

### 1. browse_subreddit
```
Fetch posts from a subreddit sorted by your choice (hot/new/top/rising/controversial). Returns a post list with content, metadata, and a data_source field. With Reddit credentials (data_source "api") posts include score, num_comments, and upvote_ratio; without credentials, results come from Reddit's public RSS feed (data_source "rss") and those fields plus nsfw are null — see the response note and do not infer popularity from them.
```

### 2. search_reddit
```
Search for posts across Reddit or specific subreddits. Returns matching posts with content and metadata.
```

### 3. get_post_details
```
Fetch a Reddit post with its comments. Requires EITHER url OR post_id. IMPORTANT: When using post_id alone, an extra API call is made to fetch the subreddit first (2 calls total). For better efficiency, always provide the subreddit parameter when known (1 call total).
```

### 4. user_analysis
```
Analyze a Reddit user's posting history, karma, and activity patterns. Returns posts, comments, and statistics.
```

### 5. reddit_explain
```
Get explanations of Reddit terms, slang, and culture. Returns definition, origin, usage, and examples.
```

## CHANNEL: parameter descriptions (additional, not counted)

The Zod schemas in `src/tools/index.ts:26-76`; `.describe()` goes into inputSchema via `zodSchemaToMCPInputSchema`. Literal examples of directive wording in the parameters:

- `browse_subreddit.limit` — `Default 25, range (1-100). Change ONLY IF user specifies.`
- `search_reddit.limit` — `Default 25, range (1-100). Override ONLY IF user requests.`
- `get_post_details.comment_limit` — `Default 20, range (1-500). Change ONLY IF user asks.`
- `get_post_details.comment_depth` — `Default 3, range (1-10). Override ONLY IF user specifies.`
- `get_post_details.max_top_comments` — `Default 5, range (1-20). Change ONLY IF user requests.`
- `user_analysis.posts_limit` — `Default 10, range (0-100). Change ONLY IF user specifies.`
- `user_analysis.comments_limit` — `Default 10, range (0-100). Override ONLY IF user asks.`
- `user_analysis.top_subreddits_limit` — `Default 10, range (1-50). Change ONLY IF user requests.`
- `browse_subreddit.include_subreddit_info` — `Include subreddit metadata like subscriber count and description. Requires Reddit credentials; silently omitted when browsing anonymously via the RSS fallback`
