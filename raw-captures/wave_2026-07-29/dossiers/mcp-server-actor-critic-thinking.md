# UNIT: mcp-server-actor-critic-thinking | npm v1.0.0 (published 2025-05-26T07:26:45.192Z) | рамки: pulsemcp | captured 2026-07-29 (static, tarball)

## VERDICT: MCP-сервер

Да, это MCP-сервер: `dist/index.js` создаёт `new Server({name: "actor-critic-thinking-server", version: "0.2.0"}, {capabilities: {tools: {}}})` из `@modelcontextprotocol/sdk` 0.5.0, подключает `StdioServerTransport`, регистрирует хендлеры `ListToolsRequestSchema` / `CallToolRequestSchema`. Один инструмент. Bin-энтрипоинт: `dist/index.js`.

## CHANNEL: instructions, npm (static)
(не обнаружены статически)

Конструктору `Server` передаются только `name` и `version` — поля `instructions` нет ни в конструкторе, ни где-либо ещё в коде (SDK 0.5.0 это поле и не поддерживал в текущем виде).

## CHANNEL: tool descriptions, npm (static, coverage=full)

Инструментов: 1 (<= 40, включён полностью).

### 1. `actor-critic-thinking`

Description (дословно):

```
A sophisticated tool for dual-perspective performance analysis through actor-critic methodology.
This tool enables comprehensive evaluation of performances, creative works, or decisions by embodying both the performer's mindset and the critic's analytical perspective.
Each thought alternates between actor (creative/experiential) and critic (analytical/evaluative) viewpoints, creating a balanced assessment.

When to use this tool:
- Evaluating artistic performances, creative works, or strategic decisions
- Analyzing the gap between intention and execution
- Providing constructive feedback that considers both creative vision and technical execution
- Reviewing complex scenarios that require both empathy and objectivity
- Situations requiring balanced assessment of subjective and objective criteria
- Performance reviews that need both self-reflection and external evaluation
- Creative processes that benefit from iterative refinement

Key features:
- Alternates between actor (performer) and critic (evaluator) perspectives
- Tracks rounds of dual-perspective analysis
- Allows for multiple rounds of actor-critic dialogue
- Balances empathetic understanding with objective analysis
- Generates nuanced, multi-dimensional assessments
- Provides actionable feedback for improvement

Parameters explained:
- content: Your current analysis content from the specified role perspective
- role: Either "actor" (empathetic/creative viewpoint) or "critic" (analytical/evaluative viewpoint)
- nextRoundNeeded: True if another round of actor-critic dialogue is needed
- thoughtNumber: Current thought number in the sequence (increments with each thought)
- totalThoughts: Total number of thoughts planned (must be odd and >= 3)

Actor perspective should include:
* Understanding intentions, creative choices, emotional context, challenges faced
* Self-reflection on performance and decision-making process
* Explanation of creative vision and goals

Critic perspective should include:
* Technical execution analysis, effectiveness evaluation
* Audience impact assessment, comparative analysis
* Objective feedback and improvement suggestions

You should:
1. Start with either actor or critic perspective
2. Alternate between perspectives to maintain balance
3. Continue rounds until comprehensive analysis is achieved
4. Focus on relevant performance aspects
5. Generate balanced assessments that honor both perspectives
6. Provide constructive, actionable feedback
7. Only set nextRoundNeeded to false when analysis is complete
```

Параметры (описания из inputSchema, дословно):
- `content` (string, required): "Your current analysis content from the specified role perspective"
- `role` (string enum actor|critic, required): "The perspective role: 'actor' for empathetic/creative viewpoint, 'critic' for analytical/evaluative viewpoint"
- `nextRoundNeeded` (boolean, required): "Whether another round of actor-critic dialogue is needed"
- `thoughtNumber` (integer >=1, required): "Current thought number in the sequence"
- `totalThoughts` (integer >=3, required): "Total number of thoughts planned (must be odd and >= 3)"

## MARKER SIGNALS

Из стирингового регекс-списка совпадений нет (нет "instead of built-in", "takes precedence", "MUST use", "primary tool" и т.п.). Тон описания — рекламно-инструктивный ("A sophisticated tool", императивный блок "You should: 1…7", "Only set nextRoundNeeded to false when analysis is complete"), но это self-scoped guidance по использованию самого инструмента, не вытеснение других инструментов и не steering против built-ins.

## NOTES (static analysis)

- Код НЕ минифицирован: tsc-выхлоп с sourcemap и .d.ts, читается полностью.
- Риск динамической сборки строк: нулевой — description задан одним литеральным template string, конструктор Server получает объектный литерал.
- Никакой сети/файловой системы/exec: единственный side effect — pretty-print мысли в stderr через chalk. Состояние (thoughtHistory) держится в памяти процесса.
- Просмотрено файлов: 4 из 6 (package.json, dist/index.js целиком, README.md и карты/декларации по списку; index.js.map и index.d.ts — генерируемые артефакты того же кода).
- Клон паттерна sequential-thinking от Anthropic (структура кода почти идентична reference-серверу), автор Aquarius Wing. Версия в package.json 1.0.0, но в конструкторе Server — "0.2.0" (расхождение метаданных).
