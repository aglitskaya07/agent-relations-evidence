# UNIT: nexus-mcp | npm v3.4.0 (published 2026-02-28T23:37:40.470Z) | scope: pulsemcp | captured 2026-07-29 (static, tarball)

This is an MCP server: `dist/index.js` creates `new Server({name: 'nexus', ...})` from `@modelcontextprotocol/sdk`, registers ListTools/CallTool/ListResources/ReadResource, stdio transport. One tool (`search`) is a wrapper over OpenRouter (Perplexity Sonar / Grok).

## CHANNEL: instructions, npm (static, 737 chars)

```
AI-powered web search and knowledge retrieval via Perplexity Sonar and Grok models.

MODEL SELECTION:
- sonar: Fast Q&A, current web info (30s timeout)
- sonar-pro: Multi-step research queries (60s timeout, premium)
- sonar-reasoning-pro: Complex reasoning with citations (120s timeout, premium)
- sonar-deep-research: Exhaustive multi-source reports (300s timeout, premium)
- grok-4: Training data knowledge, no web search (60s timeout, premium)

CONSTRAINTS:
- Queries: 1-2000 chars
- Response caching enabled (reduces API costs for repeat queries)
- Concurrent identical requests automatically deduplicated
- Premium models (sonar-pro+, grok-4) have higher API costs

RESOURCES:
- config://status: Server health and configuration info
```

## CHANNEL: tool descriptions, npm (static, coverage=full)

Tools: 1 (the only `tools.push` in the ListTools handler, `dist/index.js:117-164`).

### search
> Nexus AI-powered search using Perplexity and Grok models via OpenRouter. Perplexity models (sonar, sonar-pro, sonar-reasoning-pro, sonar-deep-research) search the web for current information. Grok 4 provides responses from training data without real-time search.

Parameter descriptions (verbatim):
- `query`: "The search query to process (required, 1-2000 characters)"
- `model`: "Model to use for search. Options: sonar (fast Q&A, 30s timeout), sonar-pro (multi-step queries, 60s timeout), sonar-reasoning-pro (chain-of-thought reasoning, 120s timeout), sonar-deep-research (exhaustive research reports, 300s timeout), grok-4 (training-data knowledge, 60s timeout). Premium models (sonar-pro and above, including grok-4) have higher API costs."
- `maxTokens`: "Maximum number of tokens in the response (1-4000)"
- `temperature`: "Controls randomness in the response (0-2)"
- `timeout`: "Override the model-specific default timeout in milliseconds (5000-600000). Use this to extend or reduce the wait time for API responses."

Marker scan for steering regexes: no matches — neither in instructions nor in the tool description are there priority/displacement formulations ("instead of built-in", "primary", "precedence", "MUST use", etc.). Neutral factual tone.

## NOTES

- The code is not minified: tsc compilation with names and comments preserved, .js.map and .d.ts are present.
- Risk of dynamic string assembly: low. instructions — a static template literal with no interpolations; tool description — a static literal; the only dynamic part is the conditional inclusion of `search` in the list if OPENROUTER_API_KEY is set.
- Reviewed: package.json, README was not read in full, dist/index.js (fully in the relevant part), grep across all 30 .js files in dist for Server/McpServer/setRequestHandler/instructions/tools.push.
