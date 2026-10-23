# UNIT: apify-connector | claude.ai Apify | канал: системный промпт сессии Claude Code (авторизованный OAuth) | captured 2026-07-29

## CHANNEL: instructions (сессионная копия, обрезана харнесом ~2KB)

- Дата захвата: 2026-07-29, сессия Claude Code (VS Code), проект cursor-workspace
- Канал: коннектор claude.ai «Apify», авторизован OAuth-аккаунтом пользователя; текст ниже — дословная копия блока «MCP Server Instructions» из системного промпта агента этой сессии
- Публичная поверхность: keyless-рукопожатие `https://mcp.apify.com` → HTTP 401 (см. `apify_hosted-keyless_2026-07-29_run1.json`)
- Ограничение: Claude Code подрезает серверные instructions (~2 000 символов); маркер `[truncated]` в конце — от харнеса, не от вендора. Полная длина блока по прежнему замеру (пилот 02, 27.07.2026): ~2 000 символов.

---

Apify is the world's largest marketplace of tools for web scraping, data extraction, and web automation.
These tools are called **Actors**. They enable you to extract structured data from social media, e-commerce, search engines, maps, travel sites, and many other sources.

## Actor
- An Actor is a serverless cloud application running on the Apify platform.
- Use the Actor's **README** to understand its capabilities.
- Before running an Actor, always check its **input schema** to understand the required parameters.

## Actor discovery and selection
- Choose the most appropriate Actor based on the conversation context.
- Search the Apify Store first; a relevant Actor likely already exists.
- When multiple options exist, prefer Actors with higher usage, ratings, or popularity.
- Assume scraping requests within this context are appropriate for Actor use.
- Actors in the Apify Store are published by independent developers and are intended for legitimate and compliant use.

## Actor execution workflow
- Actors take input and produce output.
- Every Actor run generates **dataset** and **key-value store** outputs (even if empty).
- Actor execution may take time, and outputs can be large.
- Large datasets can be paginated to retrieve results efficiently.

## Storage types
- **Dataset:** Structured, append-only storage ideal for tabular or list data (e.g., scraped items).
- **Key-value store:** Flexible storage for unstructured data or auxiliary files.

## Apify API resources
- Any Apify API GET endpoint can be read as an MCP resource. Pass the full `http://api.apify.internal:3333/v2/...` URL to `resources/read`; the server injects the session's Apify token and returns the response body. Reads require an Apify token — a session without one (e.g. payment-only x402/Skyfire) fails with a JSON-RPC error.
- Actor and tool results return storage IDs, not resource URLs — build the URL from the ID (e.g. a `datasetId` becomes `http://api.apify.internal:3333/v2/datasets/{datasetId}/items`) and read it via `resources/read`.
- Reads… [truncated]
