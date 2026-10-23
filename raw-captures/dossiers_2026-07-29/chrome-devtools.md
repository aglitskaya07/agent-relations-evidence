# UNIT: chrome-devtools-mcp@1.6.0 | npm (Google) | captured 2026-07-29 (static, tarball)

## CHANNEL: instructions, npm (static)
(см. экстракцию ниже — если в коде нет, раздел будет помечен «не обнаружены»)

**Экстракция: инструкции НЕ обнаружены.** В `build/src/index.js` сервер создаётся как:

```js
const server = new McpServer({
    name: 'chrome_devtools',
    title: 'Chrome DevTools MCP server',
    version: VERSION,
}, { capabilities: { logging: {} } });
```

Поле `instructions` конструктору не передаётся; все прочие вхождения `instructions` в коде — внутренности бандла MCP SDK (`build/src/third_party/index.js`) и строки Lighthouse-локализации, не относящиеся к серверу.

**Дополнительный инструкционный канал (не MCP-handshake):** пакет включает каталог `skills/` с шестью агентскими скиллами (`chrome-devtools`, `chrome-devtools-cli`, `debug-optimize-lcp`, `memory-leak-debugging`, `a11y-debugging`, `troubleshooting`) — SKILL.md-файлы с инструкциями для агента. Они не передаются через MCP `initialize`, но попадают агенту, если клиент подхватывает skills из пакета.

## CHANNEL: tool descriptions, npm (static, coverage=marker-scan+sample)

Всего инструментов: **55** (каталог `build/src/tools/`: console, emulation, extensions, input, lighthouse, memory, network, pages, performance, screencast, screenshot, script, snapshot, thirdPartyDeveloper, webmcp + slim-профиль `slim/tools.js` с 3 упрощёнными инструментами screenshot/navigate/evaluate).

### Маркер-скан (регексы steering-маркеров по ВСЕМ 55 описаниям)

Совпадений: 2 (оба — маркер `prefer`, внутренняя self-preference между инструментами того же сервера, не вытеснение чужих инструментов).

1. **fill_form** (`input.js`), маркер `prefer`:
> Fill out multiple form elements (inputs, selects, checkboxes, radios) at once. ALWAYS prefer this tool over multiple individual 'fill' or 'click' calls when interacting with forms. It is significantly faster, more reliable, and reduces turn count. Example: Fill username, password, and check "Remember Me" in one call.

2. **take_snapshot** (`snapshot.js`), маркер `Prefer`:
> Take a text snapshot of the currently selected page based on the a11y tree. The snapshot lists page elements along with a unique
> identifier (uid). Always use the latest snapshot. Prefer taking a snapshot over taking a screenshot. The snapshot indicates the element selected
> in the DevTools Elements panel (if any).

Прочие маркеры (instead of built-in, most powerful, PRECEDENCE, LAST resort, primary, MUST use, whenever the user, refund/credit/reward и т.д.) — совпадений нет.

### 8 репрезентативных полных описаний (дословно)

**click** (`input.js`):
> Clicks on the provided element

**evaluate_script** (`script.js`):
> Evaluate a JavaScript function inside the currently selected page${cliArgs?.categoryExtensions ? ' or service worker' : ''}. Returns the response as JSON, so returned values have to be JSON-serializable.

**navigate_page** (`pages.js`):
> Go to a URL, or back, forward, or reload. Use project URL if not specified otherwise.

**take_screenshot** (`screenshot.js`):
> Take a screenshot of the page or element.

**performance_start_trace** (`performance.js`):
> Start a performance trace on the selected webpage. Use to find frontend performance issues, Core Web Vitals (LCP, INP, CLS), and improve page load speed.

**list_network_requests** (`network.js`):
> List all requests for the currently selected page since the last navigation.

**lighthouse_audit** (`lighthouse.js`):
> Get Lighthouse score and reports for accessibility, SEO, best practices, and agentic browsing. This excludes performance. For performance audits, run ${startTrace.name}

**execute_webmcp_tool** (`webmcp.js`):
> Executes a WebMCP tool exposed by the page.

### Динамическая сборка описаний

5 описаний — шаблонные литералы с интерполяцией (`list_console_messages`, `get_console_message`, `lighthouse_audit`, `list_pages`, `evaluate_script`). Интерполяции ограничены: условные добавки по CLI-флагу `categoryExtensions` и подстановка имён соседних инструментов. Внешних/сетевых источников текста описаний нет. Отдельный случай: `execute_webmcp_tool` / `execute_3p_developer_tool` исполняют инструменты, объявленные самой веб-страницей — их описания приходят из страницы в рантайме и статически не фиксируются (потенциальный runtime-канал стороннего текста).

## NOTES
- Код НЕ минифицирован: читаемый скомпилированный TypeScript (ES modules, комментарии лицензий сохранены). Исключение — `build/src/third_party/*` (бандлы MCP SDK и Lighthouse, конкатенированные, но тоже не однострочно минифицированные).
- Риск динамической сборки строк: низкий для собственных описаний (только CLI-флаги и cross-ссылки на имена инструментов); отдельно отмечен runtime-канал webmcp/3p-developer tools, где описания приходят из открытой страницы.
- Просмотрено: 366 файлов в пакете, из них текстово проанализированы все 19 файлов `build/src/tools/**` (grep+regex по всем), `build/src/index.js` полностью, grep по всему `build/` (348 файлов) на `instructions`/`new McpServer`/`registerTool`; каталог `skills/` (6 SKILL.md) учтён как побочный канал.
