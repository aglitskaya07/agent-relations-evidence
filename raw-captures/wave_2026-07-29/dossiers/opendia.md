# UNIT: opendia | npm v1.1.1 (published 2026-07-03T00:48:00.032Z) | рамки: pulsemcp | captured 2026-07-29 (static, tarball)

## VERDICT
Это настоящий MCP-сервер. `server.js` реализует ручной JSON-RPC-роутер (`handleMCPRequest`), который обрабатывает методы `initialize`, `tools/list`, `tools/call`, `resources/list`, `prompts/list`, `prompts/get`. SDK `@modelcontextprotocol/*` не используется — протокол реализован вручную поверх Express + `ws`. Сервер выступает мостом MCP ↔ браузерное расширение (Chrome/Firefox) через WebSocket. Фактический набор инструментов приходит динамически от расширения (`availableTools`); при отсутствии расширения возвращается статический fallback-набор (`getFallbackTools`).

## CHANNEL: instructions, npm (static, 143 chars)
Строка `instructions`, возвращаемая в ответе на `initialize` (server.js:192–193):

"🎯 Enhanced browser automation with anti-detection bypass for Twitter/X, LinkedIn, Facebook. Extension may take a moment to connect."

serverInfo.name = "browser-mcp-server", version "2.0.0" (несмотря на npm-версию пакета 1.1.1).

Дополнительно: при вызове `tools/call` без подключённого расширения возвращается текст ошибки с setup-инструкциями (server.js:241) — это content ответа, не канал instructions.

## CHANNEL: tool descriptions, npm (static, coverage=full)

ВАЖНО: реальный список инструментов формируется расширением в рантайме (`availableTools.map(...)`, server.js:216) и в тарболл НЕ входит — расширение поставляется отдельно. Ниже — 18 статических fallback-инструментов из `getFallbackTools()` (server.js), которые сервер отдаёт, пока расширение не подключилось. Их <= 40 → включены ВСЕ, дословно.

1. **page_analyze** — "🔍 BACKGROUND TAB READY: Analyze any tab without switching! Two-phase intelligent page analysis with token efficiency optimization. Use tab_id parameter to analyze background tabs while staying on current page. (Extension required)"

2. **page_extract_content** — "📄 BACKGROUND TAB READY: Extract content from any tab without switching! Perfect for analyzing multiple research tabs, articles, or pages simultaneously. Use tab_id to target specific background tabs. (Extension required)"

3. **element_click** — "🖱️ BACKGROUND TAB READY: Click elements in any tab without switching! Perform actions on background tabs while staying on current page. Use tab_id to target specific tabs. (Extension required)"

4. **element_fill** — "✏️ BACKGROUND TAB READY: Fill forms in any tab without switching! Enhanced focus and event simulation for modern web apps with anti-detection bypass for Twitter/X, LinkedIn, Facebook. Use tab_id to fill forms in background tabs. (Extension required)"

5. **page_navigate** — "🧭 Navigate to URLs with wait conditions (Extension required)"

6. **page_wait_for** — "⏳ Wait for elements or conditions (Extension required)"

7. **tab_create** — "Creates tabs. CRITICAL: For multiple identical tabs, ALWAYS use 'count' parameter! Examples: {url: 'https://x.com', count: 5} creates 5 Twitter tabs. {url: 'https://github.com', count: 10} creates 10 GitHub tabs. Single tab: {url: 'https://example.com'}. Multiple different URLs: {urls: ['url1', 'url2']}."

8. **tab_close** — "❌ Close specific tab(s) by ID or close current tab (Extension required)"

9. **tab_list** — "📋 TAB DISCOVERY: Get list of all open tabs with IDs for background tab targeting! Shows content script readiness status and tab details. Essential for multi-tab workflows - use tab IDs with other tools to work on background tabs. (Extension required)"

10. **tab_switch** — "🔄 Switch to a specific tab by ID (Extension required)"

11. **element_get_state** — "🔍 Get detailed state information for a specific element (disabled, clickable, etc.) (Extension required)"

12. **get_bookmarks** — "Get all bookmarks or search for specific bookmarks (Extension required)"

13. **add_bookmark** — "Add a new bookmark (Extension required)"

14. **get_history** — "🕒 Search browser history with comprehensive filters for finding previous work (Extension required)"

15. **get_selected_text** — "📝 BACKGROUND TAB READY: Get selected text from any tab without switching! Perfect for collecting quotes, citations, or highlighted content from multiple research tabs simultaneously. (Extension required)"

16. **page_scroll** — "📜 BACKGROUND TAB READY: Scroll any tab without switching! Critical for long pages. Navigate through content in background tabs while staying on current page. Use tab_id to target specific tabs. (Extension required)"

17. **get_page_links** — "🔗 Get all hyperlinks on the current page with smart filtering (Extension required)"

18. **page_style** — "🎨 Transform page appearance with themes, colors, fonts, and fun effects! Apply preset themes like 'dark_hacker', 'retro_80s', or create custom styles. Perfect for making boring pages fun or improving readability."

## MARKER-ANALYSIS (справочно)
Прогон по стир-маркерам. Явных precedence/override/"instead of built-in"/refund-паттернов не найдено. Мягкие императивы-маркеры:
- **tab_create**: "CRITICAL: ... ALWAYS use 'count' parameter!", "DO NOT make 5 separate calls!" (в inputSchema-описаниях полей) — настойчивая инструкция агенту генерировать пакетное открытие множества вкладок (потенциальный вектор массового автопостинга/спама вкупе с anti-detection).
- Сквозной мотив в instructions и в description'ах element_fill: **"anti-detection bypass for Twitter/X, LinkedIn, Facebook"** — сервер прямо позиционирует обход античит/антибот-детекции соцсетей как фичу.
- Множественные "BACKGROUND TAB READY ... without switching" — подталкивают к скрытым от пользователя действиям в фоновых вкладках.

## PROMPTS (prompts/list, static)
Сервер также отдаёт 6 workflow-промптов (не инструменты): post_to_social ("Post content to social media platforms with anti-detection bypass"), post_selected_quote, research_workflow, analyze_browsing_session, organize_tabs, fill_form_assistant.

## NOTES
- Код НЕ минифицирован (2555 строк, читабельный), исполнялся только текстовый анализ, код пакета не запускался.
- Риск динамической сборки строк инструментов: ВЫСОКИЙ по составу, но не по тексту в тарболле — реальные name/description инструментов приходят от браузерного расширения в рантайме (`availableTools`), которого в npm-пакете нет. Статически зафиксирован только 143-символьный `instructions` и 18 fallback-описаний.
- Просмотрено файлов: 3 (package.json, server.js, README.md — последний бегло). Извлечение fallback-описаний — регексом поверх текста server.js.
