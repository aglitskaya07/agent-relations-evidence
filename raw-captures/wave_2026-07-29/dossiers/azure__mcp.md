# UNIT: @azure/mcp | npm v3.0.0-beta.30 (published 2026-07-28T18:30:16.996Z) | рамки: npm-top,smithery-top20 | captured 2026-07-29 (static, tarball)

## VERDICT: server, but binary-wrapper — payload не в tarball

Это официальный Azure MCP Server (Microsoft, `mcpName: com.microsoft/azure`), т.е. по сути MCP-сервер, НЕ SDK/клиент. Но npm-тарболл `@azure/mcp` — тонкая обёртка-лаунчер (4 файла: `index.js` 3.7 KB, `package.json`, `scripts/post-install-script.js`, `README.md`, LICENSE). `index.js` лишь делает `require('@azure/mcp-<platform>-<arch>')` (шесть optionalDependencies: linux/darwin/win32 × x64/arm64) и вызывает `platformPackage.runExecutable(process.argv.slice(2))`. Реальный сервер — скомпилированный .NET-бинарь в платформенных пакетах, которых в анализируемом источнике нет. При отсутствии платформенного пакета лаунчер сам запускает `npm install <platformPackageName>@<version>` (execSync, с fallback `--no-save --prefer-online`) — supply-chain-примечательное поведение, но не steering.

## CHANNEL: instructions, npm (static)
(не обнаружены статически) — в тарболле нет ни строки instructions, ни конструктора Server/McpServer: серверная инициализация целиком внутри .NET-бинаря платформенного пакета, вне охвата этого юнита.

## CHANNEL: tool descriptions, npm (static, coverage=none)
(не извлекаемы статически) — регистраций инструментов (registerTool/addTool/server.tool/схем) в тарболле нет; README заявляет «40+ different Azure services», но сами name+description инструментов зашиты в скомпилированный бинарь. Маркер-скан README.md (35 KB) по всем регексам стирингового словаря — ноль совпадений; README нейтрален (setup-инструкции, таблицы конфигурации клиентов, разделы Permissions and Risk / Data Collection / Compliance).

## NOTES
- Код не минифицирован, читаемый; просмотрено 5 файлов (все файлы пакета).
- Динамической сборки строк instructions/descriptions в JS нет — их в JS нет вовсе.
- Для полного покрытия описаний инструментов нужен отдельный юнит по платформенному пакету (например `@azure/mcp-darwin-arm64`) с извлечением строк из .NET-бинаря, либо динамический стенд.
- Риск-заметка (не steering): auto-install через execSync npm при первом запуске — код тянет и исполняет платформенный пакет той же версии из registry.
