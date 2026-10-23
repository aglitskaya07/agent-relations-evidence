# UNIT: nothumanallowed | npm v16.0.64 (published 2026-05-23T07:49:19.717Z) | рамки: pulsemcp | captured 2026-07-29 (static, tarball)

## NOT-A-SERVER

Пакет — CLI-лончер/бутстраппер локального AI-ассистента «NHA», а не MCP-сервер. Обоснование:

1. **MCP-серверного кода в tarball нет.** Нет зависимости `@modelcontextprotocol/sdk` (deps: acorn, imapflow, mailparser, typescript, ws, better-sqlite3). Grep по всем 73 .mjs-файлам не находит `new Server(`, `McpServer`, `FastMCP`, `registerTool`, `server.tool(`, `ListTools` — только обычные `http.createServer` для локального Web UI и OAuth-коллбэков.
2. **Команда `nha mcp` запускает КОД, КОТОРОГО НЕТ В ПАКЕТЕ.** `src/cli.mjs:171-172`: `case 'mcp': return spawnCore('pif', ['mcp']);` — spawnCore (`src/spawn.mjs`) исполняет `~/.nha/core/pif.mjs`. Этот файл скачивается при первом запуске из `https://nothumanallowed.com/cli/pif.mjs` (см. `src/bootstrap.mjs:66-67`, `BASE_URL` в `src/constants.mjs:9`). Аналогично скачиваются `legion-x.mjs` и 38 файлов агентов. Реальный MCP-сервер — удалённый рантайм-артефакт, статически ненаблюдаемый.
3. **Внутренние «80 tools» — не MCP-регистрации.** `src/services/tool-executor.mjs` (5598 строк) содержит текстовый системный промпт для LLM с перечислением инструментов вида `14. calendar_create(summary, start, end, ...)` — это собственный prompt-based tool-calling локального ассистента, не MCP `tools/list`. Как эти инструменты экспонируются в MCP-режиме, решает скачиваемый pif.mjs.

## CHANNEL: instructions, npm (static)
(не обнаружены статически — конструктора MCP-сервера в пакете нет)

## CHANNEL: tool descriptions, npm (static, coverage=none)
(MCP-регистраций инструментов в пакете нет; описания инструментов существуют только как LLM-промпт внутреннего ассистента в tool-executor.mjs и как неизвестное содержимое скачиваемого pif.mjs)

## NOTES
- Код не минифицирован (читаемый ESM с комментариями), кроме бандла Web UI `src/ui-dist/assets/index-DNzlAbYu.js`.
- **Высокий риск динамики:** вся серверная логика (legion-x.mjs, pif.mjs, агенты, расширения) подтягивается с nothumanallowed.com при bootstrap и обновляется командой `nha update` — поведение MCP-канала может меняться без публикации новой npm-версии. Для оценки steering-контента нужен захват https://nothumanallowed.com/cli/pif.mjs отдельным (не-статическим) этапом.
- Просмотрено: package.json, README.md, bin/, все ключевые src/*.mjs (constants, bootstrap, spawn, cli, downloader), grep по всем 89 файлам пакета.
