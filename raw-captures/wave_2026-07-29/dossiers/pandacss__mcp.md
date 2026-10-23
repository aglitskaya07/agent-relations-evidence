# UNIT: @pandacss/mcp | npm v1.12.0 (published 2026-07-29T04:27:43.890Z) | рамки: npm-top,smithery-top20 | captured 2026-07-29 (static, tarball)

## VERDICT: MCP-сервер
Да, полноценный stdio MCP-сервер: `new McpServer({ name: "@pandacss/mcp", version: "1.0.0" })` из `@modelcontextprotocol/sdk/server/mcp.js` + `StdioServerTransport` (dist/index.js:55-58, 184). CLI (`panda-mcp`, bin.js → dist/cli.js) — запуск сервера + `init`-команда, вписывающая конфиг в .mcp.json/.cursor/.vscode/.windsurf/.codex. Официальный пакет Panda CSS (repo chakra-ui/panda, packages/mcp).

## CHANNEL: instructions, npm (static)
(не обнаружены статически)

Конструктор McpServer получает только `{ name, version }` — поля `instructions` нет ни в одном бандле; grep по слову `instructions` во всём пакете — 0 совпадений.

## CHANNEL: tool descriptions, npm (static, coverage=full)
12 инструментов (registerTool), описания дословно; идентичны во всех трёх бандлах (dist/index.js, dist/cli.js, dist/chunk-IBM3OGUU.mjs):

1. `get_tokens` — "Get all design tokens with their values, CSS variables, and usage examples"
2. `get_semantic_tokens` — "Get semantic tokens with their conditional values (responsive, color modes)"
3. `get_recipes` — "Get component recipes with their variants, default values, and usage examples"
4. `get_patterns` — "Get layout patterns with their properties and usage examples"
5. `get_conditions` — "Get all conditions (breakpoints, pseudo-classes, color modes) and their CSS values"
6. `get_keyframes` — "Get keyframe animations defined in the theme"
7. `get_text_styles` — "Get text style compositions for typography"
8. `get_layer_styles` — "Get layer style compositions for visual styling"
9. `get_animation_styles` — "Get animation style compositions"
10. `get_color_palette` — "Get the color palette with all color values"
11. `get_config` — "Get the resolved Panda CSS configuration including paths, JSX settings, and output options"
12. `get_usage_report` — "Get a usage report of design tokens and recipes across the codebase. Shows which tokens/recipes are used, unused, or missing. Useful for auditing, cleanup, and identifying dead code."

Параметры-описания (schema .describe): "Filter by token category", "Filter by recipe name", "Filter by pattern name", "Analysis scope: token, recipe, or all (default)".

## STEERING-МАРКЕРЫ
Не обнаружены. Ни одного совпадения по маркер-регексам (primary/precedence/MUST use/prefer/instead of built-in и т.д.). Описания сухие, фактологические, без давления на выбор инструмента. Единственная мягко-рекламная фраза — "Useful for auditing, cleanup, and identifying dead code" в get_usage_report; в outro init-команды: "MCP setup complete! Your AI assistants can now use Panda CSS tools." (это вывод в терминал пользователю, не канал к модели).

## NOTES
- Код не минифицирован — читаемый tsup-бандл, имена и строки сохранены.
- Риск динамической сборки строк описаний: низкий. Все description — статические литералы. Единственная динамика — enum-схемы recipeNameSchema/patternNameSchema строятся из проектного panda.config (ctx.recipes.keys / ctx.patterns.keys), но describe-тексты фиксированы.
- Файлов в пакете 9; просмотрено: package.json, bin.js, README.md (заголовок), dist/index.js (полностью), grep-сверка dist/cli.js, dist/chunk-IBM3OGUU.mjs, dist/index.mjs, dist/cli.mjs. index.mjs/cli.mjs — тонкие ре-экспорты chunk-файла.
- Код пакета не исполнялся (только текстовый анализ).
