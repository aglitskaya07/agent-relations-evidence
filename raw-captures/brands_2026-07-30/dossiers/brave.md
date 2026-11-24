# UNIT: brave | Brave Search | github brave/brave-search-mcp-server | author type: official | captured 2026-07-29 (static source)

MCP server confirmation: `src/server.ts` creates `new McpServer(...)` from `@modelcontextprotocol/sdk/server/mcp.js`, stdio/http transports in `src/protocols/`, tool registration via `mcpServer.registerTool`. This is a full-fledged MCP server.

## CHANNEL: instructions (85 chars)

```
Use this server to search the Web for various types of data via the Brave Search API.
```

Source: `src/server.ts:18`, the `instructions` field in the `McpServer` constructor options. The string is literal, without concatenation or interpolation.

## CHANNEL: tool descriptions (coverage=full)

Total tools: 8. All are included verbatim.

### 1. brave_web_search
```
Performs web searches using the Brave Search API and returns comprehensive search results with rich metadata.

    When to use:
        - General web searches for information, facts, or current topics
        - Location-based queries (restaurants, businesses, points of interest)
        - News searches for recent events or breaking stories
        - Finding videos, discussions, or FAQ content
        - Research requiring diverse result types (web pages, images, reviews, etc.)

    Returns a JSON list of web results with title, description, and URL.
    
    When the "results_filter" parameter is empty, JSON results may also contain FAQ, Discussions, News, and Video results.
```

### 2. brave_local_search
```
Brave Local Search API provides enrichments for location search results. Access to this API is available only through the Brave Search API Pro plans; confirm the user's plan before using this tool (if the user does not have a Pro plan, use the brave_web_search tool). Searches for local businesses and places using Brave's Local Search API. Best for queries related to physical locations, businesses, restaurants, services, etc.
    
    Returns detailed information including:
        - Business names and addresses
        - Ratings and review counts
        - Phone numbers and opening hours

    Use this when the query implies 'near me', 'in my area', or mentions specific locations (e.g., 'in San Francisco'). This tool automatically falls back to brave_web_search if no local results are found.
```

### 3. brave_video_search
```
Searches for videos using Brave's Video Search API and returns structured video results with metadata.

    When to use:
        - When you need to find videos related to a specific topic, keyword, or query.
        - Useful for discovering video content, getting video metadata, or finding videos from specific creators/publishers.

    Returns a JSON list of video-related results with title, url, description, duration, and thumbnail_url.
```

### 4. brave_image_search
(the only description in the repository without `.trim()` — passed with a leading newline and indentation)
```
    Performs an image search using the Brave Search API. Helpful for when you need pictures of people, places, things, graphic design ideas, art inspiration, and more. When relaying results in a markdown environment, it may be helpful to include images in the results (e.g., ![image.title](image.properties.url)).
```

### 5. brave_news_search
```
This tool searches for news articles using Brave's News Search API based on the user's query. Use it when you need current news information, breaking news updates, or articles about specific topics, events, or entities.
    
    When to use:
        - Finding recent news articles on specific topics
        - Getting breaking news updates
        - Researching current events or trending stories
        - Gathering news sources and headlines for analysis

    Returns a JSON list of news-related results with title, url, and description. Some results may contain snippets of text from the article.
    
    When relaying results in markdown-supporting environments, always cite sources with hyperlinks.
    
    Examples:
        - "According to [Reuters](https://www.reuters.com/technology/china-bans/), China bans uncertified and recalled power banks on planes".
        - "The [New York Times](https://www.nytimes.com/2025/06/27/us/technology/ev-sales.html) reports that Tesla's EV sales have increased by 20%".
        - "According to [BBC News](https://www.bbc.com/news/world-europe-65910000), the UK government has announced a new policy to support renewable energy".
```

### 6. brave_summarizer
```
Retrieves AI-generated summaries of web search results using Brave's Summarizer API. This tool processes search results to create concise, coherent summaries of information gathered from multiple sources.

    When to use:

    - When you need a concise overview of complex topics from multiple sources
    - For quick fact-checking or getting key points without reading full articles
    - When providing users with summarized information that synthesizes various perspectives
    - For research tasks requiring distilled information from web searches

    Returns a text summary that consolidates information from the search results. Optional features include inline references to source URLs and additional entity information.

    Requirements: Must first perform a web search using brave_web_search with summary=true parameter. Requires a Pro AI subscription to access the summarizer functionality.
```

### 7. brave_llm_context
```
Retrieves pre-extracted, relevance-ranked web content using Brave's LLM Context API, optimized for AI agents, LLM grounding, and RAG pipelines. Unlike a traditional web search that returns links and short descriptions, this tool returns the actual substance of matching pages — text chunks, tables, code blocks, and structured data — so the model can reason over it directly.

    When to use:
        - Grounding answers in fresh, relevant web content (RAG)
        - Giving an AI agent ready-to-use page content from a single search call
        - Question answering and fact-checking against current sources
        - Gathering source material for research without manually fetching pages
        - When you need the contents of pages, not just titles, descriptions, and URLs

    When relaying results in markdown-supporting environments, cite the source URLs from the "sources" map.
```

### 8. brave_place_search
```
Searches Brave's Place Search API. A single call may populate any combination of 'results' (POIs), 'cities', 'addresses', 'streets', and 'location' (the resolved search area), depending on the query's shape.

    When to use:
        - POIs near coordinates or a named area (e.g. "coffee shops in Paris") -> 'results', each with structured business data (postal address, hours, contact, ratings, photos, categories, timezone).
        - Browsing general POIs (omit 'query'; supply 'latitude'+'longitude' or 'location').
        - Disambiguating a bare city name (e.g. "springfield") -> 'cities'.
        - Resolving a specific address (e.g. "350 5th avenue" with NYC coords) -> 'addresses' (often plus 'streets').
        - Looking up a street by name (e.g. "michigan avenue" with Chicago coords) -> 'streets'.

    Inputs:
        - Anchor the search via 'latitude'+'longitude' or 'location' (or both). With neither, 'query' is required.
        - 'addresses' / 'streets' only surface when the query is address-/street-shaped AND geographically anchored.
        - 'location' format: US -- '<city> <state> <country>' (e.g. 'san francisco ca united states'); non-US -- '<city> <country>' (e.g. 'tokyo japan'). Capitalization and commas don't matter.
        - 'count' caps results (max 50, default 20). 'radius' (meters) biases toward closer results; it does NOT hard-limit the search area.
```

## Other observations (neutral, for channel context)

- Tool registration is conditional: `isToolPermittedByUser(tool.name)` in `src/server.ts` — the set of exposed tools depends on the user configuration (`src/config.ts`), i.e. the actual list may be a subset of these 8.
- Part of the text that reaches the model context lives not in tool descriptions, but in execute response texts (for example, in `src/tools/local/index.ts` lines saying that the user's plan does not support local search, and about switching to general web search).
