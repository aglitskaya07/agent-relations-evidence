# UNIT: @21st-dev/magic | npm v0.2.1 (published 2026-07-24T23:30:24.384Z) | рамки: pulsemcp | captured 2026-07-29 (static, tarball)

## NOT-A-SERVER

Пакет НЕ содержит серверного кода MCP. Это compatibility-shim: тонкий stdio↔HTTP прокси (dist/index.js, ~6 KB, единственный JS-файл), который построчно читает JSON-RPC со stdin и пересылает каждое сообщение POST-запросом на удалённый эндпоинт `https://21st.dev/api/mcp` (переопределяется env `MCP_URL_21ST`), добавляя заголовки `x-api-key` и `mcp-session-id`. В коде нет ни импорта MCP SDK, ни Server/McpServer/FastMCP/createServer, ни обработки `initialize`, ни регистраций инструментов — единственный import это `node:readline`.

Комментарий в шапке файла подтверждает: «Since 0.2.0 it is a thin stdio<->HTTP proxy to the unified 21st MCP endpoint … kept alive because the old install command … is baked into countless agent configs and model memories».

Вся steering-поверхность (instructions, tool descriptions для инструментов `generate`, `get_inspiration`, `search_logo`, легаси-имена `21st_magic_component_builder` / `21st_magic_component_inspiration` / `21st_magic_component_refiner` / `logo_search`) живёт на удалённом сервере 21st.dev и статически из tarball недоступна. README прямо говорит: «Connect and call `tools/list` to see the full set».

## CHANNEL: instructions, npm (static)
(не обнаружены статически — сервер удалённый, в пакете конструктора сервера нет)

## CHANNEL: tool descriptions, npm (static, coverage=none)
(не обнаружены статически — регистраций инструментов в пакете нет; описания отдаёт удалённый эндпоинт https://21st.dev/api/mcp)

Косвенный steering-сигнал из README (не tool description): «The old `/ui`, `/21` trigger phrases were a convention of the legacy tools' descriptions, not the protocol» — то есть у легаси-версий описания инструментов содержали триггер-фразы, но в этой версии пакета их текст отсутствует.

## NOTES
- Код НЕ минифицирован (читаемый tsc-вывод с комментариями).
- Риск динамической сборки строк для описаний: не применим локально — все описания приходят с удалённого сервера в рантайме, статический анализ tarball их принципиально не видит. Это главный «динамический» риск юнита: содержимое tools/list может меняться на стороне 21st.dev в любой момент.
- Просмотрено файлов: 3 из 3 (package/dist/index.js, package/README.md, package/package.json) — полный обход пакета.
