# UNIT: zapier | Zapier | github zapier/zapier-mcp | тип автора: официальный | captured 2026-07-29 (static source)

## NOT-A-SERVER

Репозиторий `zapier/zapier-mcp` не содержит реализации MCP-сервера. Это дистрибутив клиентского плагина / конфигурации для хостируемого закрытого сервера Zapier.

Обоснование (все 24 файла репозитория просмотрены; исходного кода нет вообще — ни .ts, ни .py, ни .go, только .md/.json/.svg/.mdc/.txt):

- `llms.txt` (дословно): «This repository contains per-client plugin manifests, install assets, skills, and rules. It does **not** contain the MCP server implementation — the server is hosted at `mcp.zapier.com/api/v1/connect` and is closed source.»
- `AGENTS.md` (дословно): «**The MCP server itself is hosted at `mcp.zapier.com`** — it's not in this repo. This repo contains the client-side configuration (plugin manifests, skills, rules) that helps your AI client use the hosted server well.»
- Все манифесты объявляют только удалённый транспорт, без entrypoint-процесса:
  - `plugins/zapier/.mcp.json` и `zapier-power/mcp.json`: `{"mcpServers": {"zapier": {"type": "http", "url": "https://mcp.zapier.com/api/v1/connect"}}}`
  - `gemini-extension.json`: `"httpUrl": "https://mcp.zapier.com/api/v1/connect"` + `"oauth": {"enabled": true}`
- Состав репозитория: README/AGENTS/CLAUDE/CONTRIBUTING/LICENSE/llms.txt, per-client plugin.json (Claude Code, Codex, Cursor, GitHub Copilot CLI), бренд-ассеты (icon.svg, logo.svg), правило `plugins/zapier/rules/zapier-lifecycle.mdc`, агент-персона `plugins/zapier/agents/zapier-mcp.agent.md`, четыре скилла (`zapier-onboard`, `zapier-demo`, `zapier-explore`, `zapier-status`) и `zapier-power/POWER.md` + `zapier-power/steering/*.md` (копии тех же скиллов для Kiro Powers).

Важно для интерпретации: steering в этом юните существует, но живёт не в каналах протокола, а на стороне клиента (skills/rules/agent-персона), поэтому в каналах `instructions` и `tool descriptions` статически измерить нечего.

## CHANNEL: instructions
(не обнаружены статически)

Ни конструктора сервера (`Server`/`McpServer`/`FastMCP`/`mcp.server`/`createServer`), ни ответа `initialize` в репозитории нет — код сервера закрыт. Единственные вхождения слова «instructions» относятся к пользовательским инструкциям по установке/перезагрузке клиента внутри скиллов.

## CHANNEL: tool descriptions (coverage=none)

Определений инструментов в репозитории нет: ни `registerTool`, ни `addTool`, ни `server.tool(`, ни `@mcp.tool`, ни `Tool{...Description}`, ни статических списков tool-определений. Набор инструментов формируется динамически хостируемым сервером по действиям, которые пользователь включил в своём аккаунте Zapier (по README — «9,000+ apps and 40,000+ actions»), и статически недоступен.
