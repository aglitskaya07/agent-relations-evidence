# UNIT: @salesforce/mcp-provider-aura-experts | npm v0.3.7 (published 2026-03-26T19:54:06.868Z) | рамки: npm-top | captured 2026-07-29 (static, tarball)

## Тип пакета
Это НЕ standalone MCP-сервер, но и не клиент/SDK: это provider-плагин для Salesforce DX MCP Server (`@salesforce/mcp`). Экспортирует `AuraExpertsMcpProvider extends McpProvider` (из `@salesforce/mcp-provider-api`), который через `getTools()` отдаёт 4 MCP-инструмента хост-серверу. Серверный код MCP (Server/McpServer) в бандле не конструируется — вкод забандлен SDK-схемы (`z.object({... instructions: t.optional(t.string())})`), но вызовов `new Server(...)` нет. Классифицирую как server-side tool provider — досье по каналам применимо.

## CHANNEL: instructions, npm (static)
(не обнаружены статически) — пакет не создаёт сервер и не передаёт `instructions`; это делает хост `@salesforce/mcp`.

## CHANNEL: tool descriptions, npm (static, coverage=full)
4 инструмента (имена — из минифицированных констант qO/zO/VO + литерал):

1. **create_aura_blueprint_draft** — title: "Aura Create Blueprint Draft"
   > Use this tool to generate a Product Requirements Document (PRD) from a Salesforce Aura component. The PRD outlines the component's structure, functionality, and requirements for migrating or converting it into a Lightning Web Component (LWC), as part of the Aura to LWC migration workflow orchestrator.

2. **enhance_aura_blueprint_draft** — title: "Aura Enhance Blueprint Draft"
   > Use this tool to enhance a draft Product Requirements Document (PRD) as part of the Aura to LWC migration workflow orchestrator.

3. **transition_prd_to_lwc** — title: "Aura Transition from PRD to LWC Component Creation"
   > Use this tool to provide next-step migration instructions from a Product Requirements Document (PRD) to a Lightning Web Component (LWC), as part of the Aura to LWC migration workflow orchestrator. The PRD is generated from a Salesforce Aura component.

4. **orchestrate_aura_migration** — title: "Aura Orchestrate Migration"
   > Use this tool to orchestrate a workflow to convert or migrate a Salesforce Aura component into its Lightning Web Component (LWC) equivalent. The input can be either an Aura component bundle file (e.g., .cmp, .controller.js, .helper.js, etc.) or a directory containing Aura component bundle files.

Маркер-скан по регексам steering-паттернов: совпадений в описаниях НЕТ (нет "instead of built-in", "takes precedence", "MUST use", superlatives и т.п.). Описания нейтральные, стиль "Use this tool to ...".

## Steering через tool OUTPUT (наблюдение вне обязательных каналов)
Существенная часть steering-поверхности пакета — не описания, а тексты, которые инструменты ВОЗВРАЩАЮТ агенту в runtime: развёрнутые императивные инструкции ("# Component Analysis Instructions...", "**Your Task**: Follow the instructions...", "**Run each tool in order, using the output of one to inform the next step.**", "**⚡ Expert-Powered**: These instructions are automatically synchronized with our experts. When the experts get smarter, so do these instructions!"). Оркестратор выстраивает цепочку из всех 4 инструментов и предписывает переход к инструменту `create_lwc_component_from_prd` другого провайдера (LWC).

## Notes
- Код: единый rollup-бандл `index.bundle.js` (~1.04 MB, 64 строки, минифицирован, имена констант mangled). Смотрел 4 файла: package.json, index.bundle.d.ts, index.bundle.js, README.md (по списку).
- Динамическая сборка строк: описания инструментов — статические литералы (риск низкий); runtime-инструкции в выводах собираются шаблонными строками из "expert grounding" — контент частично динамический.
- package.json: "(For Interal Use Only)"; зависимости включают express/cors/eventsource (забандлен транспортный код SDK), но сервер не инстанцируется.
