# UNIT: @salesforce/mcp | npm v0.30.15 (published 2026-07-09T14:42:18.783Z) | рамки: npm-top,smithery-top20 | captured 2026-07-29 (static, tarball)

## VERDICT: MCP-сервер (оболочка/хост)

Настоящий stdio MCP-сервер (oclif-команда `lib/index.js` → `SfMcpServer extends McpServer` из `@modelcontextprotocol/sdk` → `StdioServerTransport`). Однако сам тарболл — это **хост-оболочка**: почти все рабочие Salesforce-инструменты живут во внешних провайдер-пакетах (`@salesforce/mcp-provider-dx-core`, `-code-analyzer`, `-lwc-experts`, `-aura-experts`, `-mobile-web`, `-devops`, `-scale-products`, `-metadata-enrichment` — реестр в `lib/registry.js`), которые НЕ входят в тарболл (bundleDependencies: none, node_modules отсутствует). Статически в пакете определены только 2 «динамических» инструмента ядра: `list_tools` и `enable_tools`.

## CHANNEL: instructions, npm (static)
(не обнаружены статически)

Конструктор в `lib/index.js:151` передаёт только `{ name: 'sf-mcp-server', version, capabilities: { resources: {}, tools: {} } }` + опцию telemetry. Ни `instructions`, ни кастомного initialize-текста нет ни в одном файле пакета (grep по `instructions` в JS — 0 совпадений).

## CHANNEL: tool descriptions, npm (static, coverage=full — для инструментов, присутствующих в тарболле; 2 шт.)

### 1. list_tools (`lib/tools/list_tools.js`)
title: "List all individual tools"

description (дословно):
```
List all available tools this Salesforce MCP server can offer, providing the enabled status and description of each.

AGENT INSTRUCTIONS:
DO NOT USE THIS TOOL if you already know what tool you need - try to call the tool directly first.
ONLY use this tool if:
1. You tried to call a tool and got an error that it doesn't exist or isn't enabled
2. You genuinely don't know what tools are available for a specific task
3. You need to discover new tools for an unfamiliar use case

If you find one or more tools you want to enable, call enable_tools with all the tool names.
Once you have enabled a tool, you MUST invoke the tool to accomplish the user's original request - DO NOT USE A DIFFERENT TOOL OR THE COMMAND LINE.
Once a tool has been enabled, you do not need to call list_tools again - instead, invoke the desired tool directly.
```

### 2. enable_tools (`lib/tools/enable_tools.js`)
title: "Enable Salesforce MCP tools"

description (дословно):
```
Enable one or more of the tools the Salesforce MCP server provides.

AGENT INSTRUCTIONS:
Use list_tools first to learn what tools are available for enabling.
Once you have enabled the tool, you MUST invoke that tool to accomplish the user's original request - DO NOT USE A DIFFERENT TOOL OR THE COMMAND LINE.
```

### Маркер-скан (по всему lib/ + bin/)
Совпадения по steering-регексам:
- `enable_tools`: «you MUST invoke that tool to accomplish the user's original request - DO NOT USE A DIFFERENT TOOL OR THE COMMAND LINE.»
- `list_tools`: «you MUST invoke the tool to accomplish the user's original request - DO NOT USE A DIFFERENT TOOL OR THE COMMAND LINE.»

Характер стиринга: мягко-агрессивная фиксация агента внутри экосистемы сервера — после enable агенту капсом запрещают использовать другой инструмент или CLI. Классический lock-in паттерн «MUST invoke / DO NOT USE A DIFFERENT TOOL», но без анти-памяти («don't answer from memory»), без клеветы на встроенные инструменты и без precedence-claims.

## NOTES
- Код НЕ минифицирован: чистый tsc-выхлоп с sourceMappingURL, комментарии и JSDoc сохранены. Просмотрено 16 JS-файлов (lib/*.js, lib/tools/*.js, lib/utils/*.js, bin/*.js), ~1451 строка + package.json, README.md.
- Динамической сборки строк описаний нет: описания двух локальных инструментов — статические template-литералы. Но основная масса описаний инструментов (dx-core: query_org, deploy_metadata и т.д.; code-analyzer; lwc/aura experts; devops...) подтягивается в рантайме из 8 внешних npm-пакетов `@salesforce/mcp-provider-*` — для полного покрытия волны эти пакеты надо анализировать как отдельные юниты.
- `registerTool` в `SfMcpServer` оборачивает все инструменты телеметрией (@salesforce/telemetry, PDP-события) и рейт-лимитером; описания при регистрации не модифицируются (`lib/utils/tools.js` лишь читает `toolInfo.tool.description`).
- Режим `--dynamic-tools`: регистрируются только list_tools/enable_tools, остальные включаются агентом на лету через enable_tools + sendToolListChanged — сам механизм прогрессивного раскрытия инструментов.
