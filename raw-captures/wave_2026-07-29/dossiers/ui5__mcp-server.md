# UNIT: @ui5/mcp-server | npm v0.2.17 (published 2026-07-27T11:08:36.651Z) | рамки: npm-top | captured 2026-07-29 (static, tarball)

Тип: полноценный MCP-сервер (`McpServer` из `@modelcontextprotocol/sdk`, stdio-транспорт, `lib/server.js`). Официальный сервер SAP UI5 tooling.

## CHANNEL: instructions, npm (static)
(не обнаружены статически)

Конструктор `new McpServer({name: "UI5", version: PKG_VERSION}, {capabilities: {tools: {}}})` — параметр `instructions` не передаётся. Grep по `instructions` в lib/ даёт только фрагмент описания инструмента get_typescript_conversion_guidelines.

## CHANNEL: tool descriptions, npm (static, coverage=full)

10 инструментов, регистрация через обёртку `registerTool` → `server.registerTool` (`lib/registerTools.js`). Порядок регистрации намеренный: комментарий в коде — "The guidelines tool should be registered first to ensure it is displayed first in MCP clients."

1. **get_guidelines** — "This tool MUST be called once to retrieve UI5 guidelines before working on any UI5 (SAPUI5/OpenUI5) related task or project or creating a UI5 project. The guidelines provided by this tool MUST be followed to ensure best practices and avoid common pitfalls in UI5 development."

2. **run_ui5_linter** — "Run UI5 linter on a UI5 project to find and optionally fix UI5 related problems like the usage of deprecated API. After making changes, you should always run the linter again to verify that no new problems have been introduced."

3. **get_api_reference** — "Search the UI5 API reference for module names and symbols"

4. **get_project_info** — "Get general information about a local UI5 project."

5. **create_ui5_app** — "Create a new basic SAPUI5 application implemented in TypeScript or JavaScript"

6. **get_version_info** — "Get version information for UI5 (OpenUI5 or SAPUI5)"

7. **get_integration_cards_guidelines** — "This tool MUST be called once to retrieve Integration Cards guidelines before working on any Integration Card related task or creating an Integration Card. The guidelines provided by this tool MUST be followed to ensure best practices and avoid common pitfalls in Integration Cards development.Integration Cards are also called 'UI Integration Cards' or 'UI5 Integration Cards'."

8. **create_integration_card** — "Create a new Integration Card, UI Integration Card, or UI5 Integration Card"

9. **run_manifest_validation** — "Validates UI5 manifest file. After making changes, you should always run the validation again to verify that no new problems have been introduced."

10. **get_typescript_conversion_guidelines** — "This tool MUST be called once before converting a UI5 (SAPUI5/OpenUI5) project from JavaScript to TypeScript. The instructions provided by this tool MUST be followed to ensure that the project setup and code is correctly converted."

### Steering-маркеры
- "MUST be called once … MUST be followed" — в трёх guidelines-инструментах (get_guidelines, get_integration_cards_guidelines, get_typescript_conversion_guidelines). Императив, но scoped: только для UI5-задач, не претендует на приоритет над другими серверами/встроенными инструментами.
- "you should always run the … again" — run_ui5_linter, run_manifest_validation (петля самопроверки).
- Маркеров вытеснения конкурентов ("instead of built-in", "takes precedence", "LAST resort", "primary", "faster and cheaper" и т.п.) — нет.

## NOTES
- Код НЕ минифицирован: транспилированный TypeScript (ESM) с sourcemaps и .d.ts, читается свободно.
- Все description — статические литералы/конкатенации строковых литералов; риска динамической сборки описаний нет. Динамика есть только в содержимом ответов guidelines-инструментов (текст подтягивается из lib/resources и tools/*/guidelines.js на рантайме — не влияет на канал descriptions).
- Просмотрено: lib/server.js, lib/registerTools.js, все 10 tools/*/index.js полностью; grep по "instructions" по всему lib/ (77 JS-файлов без sourcemaps в пакете).
