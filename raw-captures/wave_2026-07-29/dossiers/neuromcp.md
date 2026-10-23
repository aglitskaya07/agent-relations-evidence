# UNIT: neuromcp | npm v0.29.2 (published 2026-07-13T15:25:31.683Z) | рамки: pulsemcp | captured 2026-07-29 (static, tarball)

## VERDICT: MCP-сервер

Да, полноценный MCP-сервер. `dist/chunk-7AGZOABR.js:1763` (src/server.ts в sourcemap): `new McpServer({ name: "neuromcp", version: NEUROMCP_VERSION }, { capabilities: { resources: {}, tools: {}, prompts: {} } })`. Запуск через `bin/neuromcp.mjs`, есть daemon-режим. Тематика: локальная семантическая память для AI-агентов (SQLite + гибридный поиск + knowledge graph).

## CHANNEL: instructions, npm (static)

(не обнаружены статически)

Конструктору `McpServer` передаются только `name`, `version` и `capabilities` — поле `instructions` отсутствует. Grep по строке `instructions` во всех .js в dist/ и bin/ не дал ни одного релевантного попадания (единственное совпадение — имя файла `copilot-instructions.md` в bin/init-wiki.mjs, к MCP initialize отношения не имеет).

## CHANNEL: tool descriptions, npm (static, coverage=marker-scan+sample)

Всего инструментов: 46 (`registerTool`), все описания — статические строковые литералы, извлечены полностью; лог сервера заявляет `tools: 43` (расхождение — 3 wiki-инструмента регистрируются в отдельном чанке chunk-IRBBTUJC.js, вероятно условно). Также 3 prompt'а (`memory_context_for_task`, `review_memory_candidate`, `consolidation_dry_run`) и 13 ресурсов.

Полный список имён: store_memory, search_memory, recall_answer, recall_memory, forget_memory, consolidate, memory_stats, export_memories, import_memories, backfill_embeddings, search_all, create_entity, create_relation, query_graph, search_claims, compute_centrality, update_importance, start_episode, end_episode, list_episodes, get_episode, cluster_memories, list_clusters, get_cluster_memories, summarize_cluster, summarize_episode, memory_timeline, register_agent, find_expert, agent_conflicts, review_queue, review_memory, init_reviews, compress_memories, find_transferable, transfer_memories, store_verbatim, search_verbatim, verbatim_stats, log_retrieval, cite_memories, usefulness_stats, generate_reflection, wiki_ingest, wiki_lint, wiki_briefing.

### Marker-scan (полный прогон по всем 46 описаниям)

Ровно 1 совпадение по маркер-регексам:

- **recall_answer** — маркеры `Prefer this over` / `prefer`:
  > "Answer a question FROM memory: runs hybrid retrieval, then returns a synthesized, CITED extractive answer (every sentence traces to a stored memory id) PLUS an explicit gap-analysis — what memory does NOT cover and the freshness boundary (stale_since). Returns status \"not_in_memory\" instead of fabricating when nothing matches. Deterministic, no LLM. **Prefer this over search_memory** when you need a grounded answer rather than raw chunks."

  Оценка: внутреннее рулевое между собственными инструментами сервера (recall_answer vs search_memory), не претензия на приоритет над встроенными инструментами хоста или чужими серверами. Steering-риск низкий.

Нулевые совпадения по агрессивным маркерам: instead of built-in, PRECEDENCE, LAST resort, MUST use, always default, primary tool/provider, The user has installed, refund/credit/reward, ignore previous и пр.

### 8 репрезентативных полных описаний (дословно)

1. **store_memory**: "Store a new memory with semantic deduplication, contradiction detection, surprise scoring, and entity extraction. Returns the memory ID, contradictions found, surprise score, and extracted entities."
2. **search_memory**: "Search memories using hybrid vector + full-text search with RRF ranking, graph boost, and cognitive priming. Supports temporal queries (valid_at) to find what was true at a specific time."
3. **forget_memory**: "Tombstone (soft-delete) memories matching the given filters. At least one filter is required."
4. **consolidate**: "Run consolidation: merge near-duplicates, decay stale memories, prune low-value, sweep expired, purge old tombstones. Set commit=true to apply."
5. **query_graph**: "Traverse the knowledge graph starting from an entity. Returns connected nodes and edges up to max_depth hops. Supports temporal queries."
6. **store_verbatim**: "Store raw conversation text verbatim — no summarization, no consolidation, never pruned. Use for exact recall of what was said."
7. **log_retrieval**: "Log a retrieval event so future searches can learn which memories are actually helpful. Call right after search_memory. Pass retrieved_ids (all top-K), cited_ids (those actually used in the answer, if known), and an outcome label (helpful/neutral/harmful). Usefulness scores are applied as a prior in future rankings."
8. **wiki_briefing**: "Generate a structured briefing from the wiki: active projects, unprocessed sources, recent changelog entries, stale pages needing attention. Use for morning status checks."

## NOTES (методология)

- Код НЕ минифицирован: esbuild-бандл с читаемыми идентификаторами, chunk-*.js + полные sourcemaps (.js.map). Извлечение надёжное.
- Риск динамической сборки строк: низкий. Все 46 описаний — литералы ("..." или '...' с —-эскейпами) прямо в вызовах registerTool; конкатенации/шаблонов при сборке описаний не обнаружено.
- Просмотрено: package.json, README-структура, все ~73 не-map файла dist/ (grep-скан целиком, чтение chunk-7AGZOABR.js и chunk-IRBBTUJC.js в местах регистрации), bin/ (16 .mjs, grep). Всего файлов в пакете: 254 (включая sourcemaps, шаблоны, docs).
- Извлечённые пары name+description сохранены в scratch/wave/neuromcp_tools.json (все 46).
- Код пакета не исполнялся (ОПСЕК соблюдён).
