# UNIT: youtube | YouTube Transcripts | github kimtaeyoon83/mcp-server-youtube-transcript | тип автора: комьюнити | captured 2026-07-29 (static source)

## SERVER CONFIRMED

TypeScript, `@modelcontextprotocol/sdk`. `src/index.ts`: `new Server({ name: "mcp-servers-youtube-transcript", version: "0.1.0" }, { capabilities: { tools: {} } })`, транспорт `StdioServerTransport`, обработчики `ListToolsRequestSchema` / `CallToolRequestSchema`. Это полноценный MCP-сервер, не SDK/клиент/прокси.

## CHANNEL: instructions
(не обнаружены статически)

Второй аргумент конструктора `Server` содержит только `capabilities`; поля `instructions` нет нигде в репозитории (grep по `instructions` вне package-lock.json — ноль совпадений).

## CHANNEL: tool descriptions (coverage=full)

Всего инструментов: 2 (единственный источник — литерал `const TOOLS: Tool[]` в `src/index.ts`, строки 17–104).

### 1. `get_transcript`
> Extract transcript from a YouTube video URL or ID. Automatically falls back to available languages if requested language is not available.

annotations: `title: "Get Transcript"`, `readOnlyHint: true`, `openWorldHint: true`

### 2. `analyze_video`
> Analyze a video with TwelveLabs Pegasus (video-understanding model) to generate a summary or answer a question. Unlike get_transcript, this reasons over what is shown on screen, so it works for videos with little or no speech. Requires a TWELVELABS_API_KEY and a publicly reachable direct video URL (e.g. .mp4/.mov/.webm); a YouTube watch page URL is NOT a direct media file and will not work.

annotations: `title: "Analyze Video (TwelveLabs Pegasus)"`, `readOnlyHint: true`, `openWorldHint: true`

## SUPPLEMENTARY: параметрические описания (inputSchema/outputSchema, дословно)

`get_transcript`:
- `url` — "YouTube video URL or ID"
- `lang` — "Language code for transcript (e.g., 'ko', 'en'). Will fall back to available language if not found." (default "en")
- `include_timestamps` — "Include timestamps in output (e.g., '[0:05] text'). Useful for referencing specific moments. Default: false" (default false)
- `strip_ads` — "Filter out sponsored segments from transcript based on chapter markers (e.g., chapters marked as 'Werbung', 'Ad', 'Sponsor'). Default: true" (default true)
- output `meta` — "Title | Author | Subs | Views | Date"

`analyze_video`:
- `url` — "Publicly reachable direct video URL (e.g. an .mp4/.mov/.webm link or pre-signed URL). Not a YouTube watch page."
- `prompt` — "Instruction or question for the model (e.g. 'Summarize this video in 3 sentences' or 'What products are shown?'). Default: a general summary." (default "Summarize this video, highlighting the main topic, key events, and conclusion.")
- `model` — "Pegasus model to use. Default: pegasus1.2" (enum pegasus1.2 / pegasus1.5)
- `max_tokens` — "Maximum response length in tokens (2-4096 for pegasus1.2). Default: 2048"
- output `meta` — "Model | finish reason", `content` — "Generated analysis text"

## SUPPLEMENTARY: рантайм-текст, дописываемый в тело ответа (не описание инструмента)

`handleToolCall` для `get_transcript` конкатенирует в возвращаемый текст служебные пометки, среди них — инструкция модели:
- `[Note: Requested language '${lang}' not available. Using '${result.actualLang}'. Available: ${...}]`
- `[Note: ${result.adsStripped} sponsored segment lines filtered out based on chapter markers]`
- `[Note: No chapter markers found. If summarizing, please exclude any sponsored segments or ads from the summary.]`

Это единственный канал в репозитории, где сервер адресует поведение модели императивно; он находится в результате вызова, а не в instructions или в описании инструмента.
