# UNIT: neuromcp | npm v0.29.2 (published 2026-07-13T15:25:31.683Z) | scope: pulsemcp | captured 2026-07-29 (static, tarball)

## VERDICT: MCP server

Yes, a full MCP server. `dist/chunk-7AGZOABR.js:1763` (src/server.ts in sourcemap): `new McpServer({ name: "neuromcp", version: NEUROMCP_VERSION }, { capabilities: { resources: {}, tools: {}, prompts: {} } })`. Started via `bin/neuromcp.mjs`, there is a daemon mode. Theme: local semantic memory for AI agents (SQLite + hybrid search + knowledge graph).

## CHANNEL: instructions, npm (static)

(not found statically)

Only `name`, `version`, and `capabilities` are passed to the `McpServer` constructor — the `instructions` field is absent. Grep for the string `instructions` in all .js files under dist/ and bin/ found no relevant hits (the only match is the file name `copilot-instructions.md` in bin/init-wiki.mjs, which is unrelated to MCP initialize).

## CHANNEL: tool descriptions, npm (static, coverage=marker-scan+sample)

Total tools: 46 (`registerTool`), all descriptions are static string literals, extracted in full; the server log claims `tools: 43` (the discrepancy is 3 wiki tools registered in a separate chunk `chunk-IRBBTUJC.js`, presumably conditionally). Also 3 prompts (`memory_context_for_task`, `review_memory_candidate`, `consolidation_dry_run`) and 13 resources.

Full list of names: store_memory, search_memory, recall_answer, recall_memory, forget_memory, consolidate, memory_stats, export_memories, import_memories, backfill_embeddings, search_all, create_entity, create_relation, query_graph, search_claims, compute_centrality, update_importance, start_episode, end_episode, list_episodes, get_episode, cluster_memories, list_clusters, get_cluster_memories, summarize_cluster, summarize_episode, memory_timeline, register_agent, find_expert, agent_conflicts, review_queue, review_memory, init_reviews, compress_memories, find_transferable, transfer_memories, store_verbatim, search_verbatim, verbatim_stats, log_retrieval, cite_memories, usefulness_stats, generate_reflection, wiki_ingest, wiki_lint, wiki_briefing.

### Marker-scan (full run over all 46 descriptions)

Exactly 1 match by marker regexes:

- **recall_answer** — markers `Prefer this over` / `prefer`:
  > "Answer a question FROM memory: runs hybrid retrieval, then returns a synthesized, CITED extractive answer (every sentence traces to a stored memory id) PLUS an explicit gap-analysis — what memory does NOT cover and the freshness boundary (stale_since). Returns status \"not_in_memory\" instead of fabricating when nothing matches. Deterministic, no LLM. **Prefer this over search_memory** when you need a grounded answer rather than raw chunks."

  Assessment: internal steering between its own server tools (recall_answer vs search_memory), not a claim of priority over the host's built-in tools or other servers'. Steering risk is low.

Zero matches for aggressive markers: instead of built-in, PRECEDENCE, LAST resort, MUST use, always default, primary tool/provider, The user has installed, refund/credit/reward, ignore previous, etc.

### 8 representative full descriptions (verbatim)

1. **store_memory**: "Store a new memory with semantic deduplication, contradiction detection, surprise scoring, and entity extraction. Returns the memory ID, contradictions found, surprise score, and extracted entities."
2. **search_memory**: "Search memories using hybrid vector + full-text search with RRF ranking, graph boost, and cognitive priming. Supports temporal queries (valid_at) to find what was true at a specific time."
3. **forget_memory**: "Tombstone (soft-delete) memories matching the given filters. At least one filter is required."
4. **consolidate**: "Run consolidation: merge near-duplicates, decay stale memories, prune low-value, sweep expired, purge old tombstones. Set commit=true to apply."
5. **query_graph**: "Traverse the knowledge graph starting from an entity. Returns connected nodes and edges up to max_depth hops. Supports temporal queries."
6. **store_verbatim**: "Store raw conversation text verbatim — no summarization, no consolidation, never pruned. Use for exact recall of what was said."
7. **log_retrieval**: "Log a retrieval event so future searches can learn which memories are actually helpful. Call right after search_memory. Pass retrieved_ids (all top-K), cited_ids (those actually used in the answer, if known), and an outcome label (helpful/neutral/harmful). Usefulness scores are applied as a prior in future rankings."
8. **wiki_briefing**: "Generate a structured briefing from the wiki: active projects, unprocessed sources, recent changelog entries, stale pages needing attention. Use for morning status checks."

## NOTES (methodology)

- The code is NOT minified: esbuild bundle with readable identifiers, chunk-*.js + full sourcemaps (.js.map). Extraction is reliable.
- Risk of dynamic string assembly: low. All 46 descriptions are literals ("..." or '...' with —-escapes) directly in registerTool calls; no concatenation/template assembly of descriptions was found.
- Reviewed: package.json, README structure, all ~73 non-map files in dist/ (full grep scan, reading chunk-7AGZOABR.js and chunk-IRBBTUJC.js at registration points), bin/ (16 .mjs, grep). Total files in the package: 254 (including sourcemaps, templates, docs).
- The extracted name+description pairs are saved in scratch/wave/neuromcp_tools.json (all 46).
- The package code was not executed (OPSEC observed).
