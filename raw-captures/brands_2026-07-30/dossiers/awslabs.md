# UNIT: awslabs | AWS (core) | github awslabs/mcp/src/core-mcp-server | тип автора: официальный | captured 2026-07-29 (static source)

## PATH MISSING

Целевая директория юнита `src/core-mcp-server` в снапшоте репозитория отсутствует.

Проверено:
- Корень снапшота существует: `scratch/brands/src/awslabs/mcp-HEAD` (есть `src/` с ~60 другими серверами: aws-api-mcp-server, cloudwatch-mcp-server, dynamodb-mcp-server и т.д.).
- `src/core-mcp-server` — не существует (`find` возвращает ошибку "No such file or directory").
- Грep по всему снапшоту на `core-mcp-server` даёт только упоминания: `README.md` (примеры JSON-конфигов, оставшиеся от старой версии), `docs/migration-core.md`, `.github/CODEOWNERS`, шаблоны issue, `docusaurus/sidebars.ts`, `.secrets.baseline`. Ни одного файла исходников сервера.
- Грep по `prompt_understanding` (единственный собственный инструмент этого сервера) даёт единственное совпадение — `docs/migration-core.md`, то есть текст описания, а не код.

Причина, зафиксированная в самом репозитории (`docs/migration-core.md`, дословно):

> This guide helps you migrate from `awslabs.core-mcp-server` to configuring individual MCP servers directly in your client.

> The `core-mcp-server` was designed as a proxy that bundles 45+ MCP servers behind role-based environment variables. While useful early on, it has several issues:
>
> - **Modern MCP clients handle multi-server configs natively** — Kiro, Cursor, and VS Code all support configuring multiple MCP servers directly, making the proxy pattern unnecessary
> - **Massive dependency footprint** — Installing core-mcp-server pulls in every bundled server, causing slow installs and build failures (e.g., cassandra-driver compilation issues)
> - **Tool name overflow** — Proxied tool names with prefixes can exceed the 64-character API limit in some clients
> - **Bundles deprecated servers** — Several servers included in the core bundle have been deprecated

> The core server's only unique tool, `prompt_understanding`, returns a static Markdown document with AWS architecture guidance. This content can be included directly in your project's CLAUDE.md, `.cursorrules`, or equivalent AI assistant configuration file instead.

Дополнительно (важно для классификации, если юнит будет заменён): по описанию самого репозитория core-mcp-server был прокси/бандлером над другими MCP-серверами с единственным собственным инструментом `prompt_understanding`, то есть по типу это ближе к прокси, чем к содержательному серверу. Но исходников для статической проверки в снапшоте нет, поэтому вердикт — PATH MISSING, а не NOT-A-SERVER.

## CHANNEL: instructions
(не обнаружены статически — исходников сервера нет в снапшоте)

## CHANNEL: tool descriptions (coverage=none)
(не обнаружены статически — исходников сервера нет в снапшоте)
