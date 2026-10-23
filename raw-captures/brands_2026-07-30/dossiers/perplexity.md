# UNIT: perplexity | Perplexity | github perplexityai/modelcontextprotocol | тип автора: официальный | captured 2026-07-29 (static source)

Это MCP-сервер: TypeScript, `new McpServer({name: "ai.perplexity/mcp-server", ...})` в `src/server.ts:541`, четыре `server.registerTool(...)`, транспорты stdio (`src/index.ts`) и HTTP (`src/http.ts`).

## CHANNEL: instructions (660 chars)

Perplexity AI server for web-grounded search, research, and reasoning, backed by the Perplexity Agent API. Use perplexity_search for finding URLs, facts, and recent news. Supports recency filters and domain restrictions. Use perplexity_ask for quick AI-answered questions with citations. Supports recency filters, domain restrictions, and search context size control. Use perplexity_research for in-depth multi-source investigation (slow, can take minutes). Use perplexity_reason for complex analysis requiring step-by-step logic. Supports recency filters, domain restrictions, and search context size control. All tools are read-only and access live web data.

## CHANNEL: tool descriptions (coverage=full)

Всего инструментов: 4.

### perplexity_ask
title: Ask Perplexity

Answer a question using web-grounded AI (Perplexity Agent API, fast preset). Best for: quick factual questions, summaries, explanations, and general Q&A. Returns a text response with numbered citations. Fastest and cheapest option. Supports filtering by recency (hour/day/week/month/year), domain restrictions, and search context size. For in-depth multi-source research, use perplexity_research instead. For step-by-step reasoning and analysis, use perplexity_reason instead.

(в коде `ASK_PRESET` подставляется конкатенацией; `ASK_PRESET = "fast"`, server.ts:24)

### perplexity_research
title: Deep Research

Conduct deep, multi-source research on a topic (Perplexity Agent API, high preset). Best for: literature reviews, comprehensive overviews, investigative queries needing many sources. Returns a detailed response with numbered citations. Significantly slower than other tools (can take minutes). For quick factual questions, use perplexity_ask instead. For logical analysis and reasoning, use perplexity_reason instead.

(`RESEARCH_PRESET = "high"`, server.ts:26)

### perplexity_reason
title: Advanced Reasoning

Analyze a question using step-by-step reasoning with web grounding (Perplexity Agent API, medium preset). Best for: math, logic, comparisons, complex arguments, and tasks requiring chain-of-thought. Returns a reasoned response with numbered citations. Supports filtering by recency (hour/day/week/month/year), domain restrictions, and search context size. For quick factual questions, use perplexity_ask instead. For comprehensive multi-source research, use perplexity_research instead.

(`REASON_PRESET = "medium"`, server.ts:25)

### perplexity_search
title: Search the Web

Search the web and return a ranked list of results with titles, URLs, snippets, and dates. Best for: finding specific URLs, checking recent news, verifying facts, discovering sources. Returns formatted results (title, URL, snippet, date) with no AI synthesis. Supports recency filters and domain restrictions. For AI-generated answers with citations, use perplexity_ask instead.

## Параметры (описания полей ввода, дословно)

- `messages`: "Array of conversation messages"; role: "Role of the message sender"; content: "The content of the message"
- `search_recency_filter`: "Filter search results by recency. Use 'hour' for very recent news, 'day' for today's updates, 'week' for this week, etc."
- `search_domain_filter`: "Restrict search results to specific domains (e.g., ['wikipedia.org', 'arxiv.org']). Use '-' prefix for exclusion (e.g., ['-reddit.com'])."
- `search_context_size`: "Controls how much web context is retrieved. 'low' is fastest, 'high' provides more comprehensive results."
- `query`: "Search query string"
- `max_results`: "Maximum number of results to return (1-20, default: 10)"
- `max_tokens_per_page`: "Maximum tokens to extract per webpage (default: 1024)"
- `country`: "ISO 3166-1 alpha-2 country code for regional results (e.g., 'US', 'GB')"

Аннотации у всех четырёх инструментов: readOnlyHint: true, openWorldHint: true, idempotentHint: false, destructiveHint: false.
