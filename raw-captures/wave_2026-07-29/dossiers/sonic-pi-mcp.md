# UNIT: sonic-pi-mcp | npm v2.0.0 (published 2026-03-22T13:04:10.009Z) | рамки: pulsemcp | captured 2026-07-29 (static, tarball)

Тип: полноценный MCP-сервер (stdio). `McpServer` из `@modelcontextprotocol/sdk`, транспорт `StdioServerTransport`, отправляет Sonic Pi Ruby-код по OSC на 127.0.0.1:4560. Единственный серверный файл — `dist/server.mjs` (бандл из `src/server.ts`, читаемый, не минифицирован); `bin/cli.mjs` — тонкая обёртка-импорт.

## CHANNEL: instructions, npm (static)
(не обнаружены статически)

Конструктор: `new McpServer({ name: "Sonic Pi MCP", version: SERVER_VERSION })` — поле `instructions` отсутствует (dist/server.mjs:116-119).

Примечание: steering-контент уходит по другим каналам —
- MCP resource `dj-session-guide` (`sonicpi://v2/dj-session`): markdown-гайд `DJ_SESSION_GUIDE` (~2.9k chars), задающий роль «You are a **live DJ** using Sonic Pi», предпочтения инструментов («**queue_segment** — Push the **next** DJ segment (primary)», «stop_all — … use sparingly») и правила написания кода.
- MCP prompt `next_performance_segment`: "Frame the next Sonic Pi code block for a long NL DJ session (taste, arc, transitions)." — текст промпта велит: «Read resource sonicpi://v2/dj-session if available. … Respond with valid Sonic Pi Ruby for the next segment, then call queue_segment with that code.»

## CHANNEL: tool descriptions, npm (static, coverage=full)

4 инструмента (dist/server.mjs:178-225), дословно:

1. **queue_segment** — "Push the next music segment to Sonic Pi. Use with the v2 DJ session runner for crossfaded handoffs. Prefer this over ad-hoc snippets for long sets."
   - param `code`: "Full Sonic Pi (Ruby) source for the next segment. Use named live_loops; prefer use_bpm when tempo matters."
2. **run_code** — "Alias of queue_segment for compatibility. Sends Sonic Pi code over OSC to the session runner."
3. **stop_all** — "Hard stop: stop all running Sonic Pi jobs (like the Stop button). Use sparingly; prefer queue_segment for musical transitions."
4. **play_note** — "Play a single test note (quick sanity check). Not for full DJ segments—use queue_segment for those."
   - params: `note` "MIDI note number (0-127)", `synth` "Synth name (e.g. :beep, :saw, :prophet)", `sustain` "Note length in seconds", `cutoff` "Filter cutoff frequency"

Маркеры steering в описаниях: «Prefer this over ad-hoc snippets» (queue_segment), «prefer queue_segment» (stop_all, play_note) — внутрипакетная маршрутизация между собственными инструментами, не вытеснение чужих.

## NOTES
- Код не минифицирован (bun-бандл с сохранёнными именами и комментарием `// src/server.ts`).
- Динамической сборки строк описаний нет: все description/instructions-строки — статические литералы; единственная динамика — env-переменные OSC_HOST/OSC_PORT/OSC_CODE_PATH/OSC_STOP_ALL_PATH (адресация OSC, не текст для модели).
- Просмотрено файлов: 4 из 6 (package.json, dist/server.mjs полностью, bin/cli.mjs, листинг; README.md и sonic-pi-queue.rb не входят в каналы instructions/tool-descriptions).
- Риск: инструменты пересылают произвольный Ruby-код в Sonic Pi (eval на стороне Sonic Pi); гайд сам предупреждает «Do not call OS/shell from code», но технического ограничения нет.
