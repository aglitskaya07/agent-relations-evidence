# UNIT: expo-mcp | npm v0.2.4 (published 2026-02-12T15:15:26.248Z) | рамки: npm-top | captured 2026-07-29 (static, tarball)

Издатель: 650 Industries, Inc. (Expo). «Local MCP capabilities provider for Expo» — stdio MCP-сервер (или composite-прокси через MCP-туннель) для локальной разработки Expo/React Native: логи, devtools, автоматизация симулятора/эмулятора.

Архитектура: `bin/expo-mcp.mjs` → `dist/cli.js` создаёт `StdioMcpServerProxy` или `CompositeMcpServerProxy` из внешней зависимости `@expo/mcp-tunnel` (в тарболле НЕ содержится), затем `addMcpCapabilities(server, projectRoot)` регистрирует инструменты и один prompt (`expo_router_sitemap`, только для expo-router-проектов).

## CHANNEL: instructions, npm (static)
(не обнаружены статически)

Конструктору прокси в `dist/cli.js` передаются только `tunnelServerUrl / devServerUrl / projectRoot / mcpServerName / mcpServerVersion` — поля `instructions` нет; grep по `instructions` во всём `dist/` — ноль совпадений. Оговорка: фактический вызов `new McpServer(...)` находится внутри невключённой зависимости `@expo/mcp-tunnel` (~0.2.3), там теоретически может добавляться своя instructions-строка — вне охвата этого тарболла.

## CHANNEL: tool descriptions, npm (static, coverage=full)

6 инструментов (1 условный), все описания дословно:

1. **expo_router_sitemap** (регистрируется только если проект использует expo-router)
   - title: `Query the sitemap of the current expo-router project`
   - description: `Query the all routes of the current expo-router project. This is useful if you were using expo-router and want to know all the routes of the app`

2. **open_devtools**
   - title: `Open devtools`
   - description: `Open the React Native DevTools`

3. **collect_app_logs**
   - title: `Collect app logs`
   - description: `Collect logs from native device (logcat/syslog) or JavaScript console`
   - параметры с описаниями: sources — `Log sources: logcat, syslog, or console.log`; filter — `Regex or string pattern to filter logs. Only logs matching this pattern will be returned`; logLevel — `Log level filter (e.g., error, warn, info, debug). Only logs with this level will be returned`

4. **automation_tap**
   - title: `Tap on device`
   - description: `Tap on the device at the given coordinates (x, y) or by react-native testID. Provide either (x AND y) or testID.`

5. **automation_take_screenshot**
   - title: `Take screenshot of the app`
   - description: `Take screenshot of the full app or a specific view by react-native testID. Optionally provide testID to screenshot a specific view.`

6. **automation_find_view**
   - title: `Find view properties`
   - description: `Find view and dump its properties. This is useful to verify the view is rendered correctly`

Prompt (не tool): **expo_router_sitemap** — description: `Query the all routes of the current expo-router project using \`expo-router-sitemap\`.`

Стиринг-маркеры: ноль. Описания нейтральные, функциональные, без «primary/prefer/instead of/MUST»-риторики. Единственные мягкие обороты — «This is useful if/to …» (x2), это обычная контекстная подсказка, не вытеснение конкурентов.

## NOTES
- Код НЕ минифицирован: чистый tsc-выход с сорсмапами и .d.ts, читается полностью.
- Все описания — статические строковые литералы; риск динамической сборки строк описаний — нулевой в пределах тарболла.
- Остаточный риск: server-level instructions могли бы жить в `@expo/mcp-tunnel` (внешняя зависимость, не в тарболле).
- Побочное наблюдение (не steering, но supply-chain-заметка): tool и prompt `expo_router_sitemap` при вызове исполняют `npx -y expo-router-sitemap@latest` — подтягивание свежего пакета из npm в рантайме.
- Просмотрено: все 5 JS-файлов серверной логики (index.js, cli.js, mcp/tools.js, mcp/prompts.js, mcp/tools/automation.js) полностью + package.json + grep по всему dist/ (~30 js/d.ts файлов); assets/ — бинарные iOS-драйверы автоматизации, текстовых описаний не содержат.
