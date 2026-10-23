# UNIT: @modelcontextprotocol/server-sequential-thinking | npm v2026.7.4 (published 2026-07-04T23:05:13.130Z) | рамки: npm-top | captured 2026-07-29 (static, tarball)

## VERDICT: MCP-сервер

Настоящий MCP-сервер на stdio-транспорте: `dist/index.js` создаёт `new McpServer({ name: "sequential-thinking-server", version: "0.2.0" })`, регистрирует один инструмент через `server.registerTool(...)` и подключает `StdioServerTransport`. Бизнес-логика в `dist/lib.js` (класс `SequentialThinkingServer`). Никакой сетевой активности, файловых операций или исполнения кода — чисто in-memory журнал «мыслей».

## CHANNEL: instructions, npm (static)
(не обнаружены статически)

Конструктор `McpServer` получает только `{ name, version }` — поля `instructions` нет ни в конструкторе, ни где-либо ещё в коде пакета.

## CHANNEL: tool descriptions, npm (static, coverage=full)

Инструментов: 1 (<= 40, включён полностью).

### Tool 1: `sequentialthinking` (title: "Sequential Thinking")

Description (дословно):

```
A detailed tool for dynamic and reflective problem-solving through thoughts.
This tool helps analyze problems through a flexible thinking process that can adapt and evolve.
Each thought can build on, question, or revise previous insights as understanding deepens.

When to use this tool:
- Breaking down complex problems into steps
- Planning and design with room for revision
- Analysis that might need course correction
- Problems where the full scope might not be clear initially
- Problems that require a multi-step solution
- Tasks that need to maintain context over multiple steps
- Situations where irrelevant information needs to be filtered out

Key features:
- You can adjust total_thoughts up or down as you progress
- You can question or revise previous thoughts
- You can add more thoughts even after reaching what seemed like the end
- You can express uncertainty and explore alternative approaches
- Not every thought needs to build linearly - you can branch or backtrack
- Generates a solution hypothesis
- Verifies the hypothesis based on the Chain of Thought steps
- Repeats the process until satisfied
- Provides a correct answer

Parameters explained:
- thought: Your current thinking step, which can include:
  * Regular analytical steps
  * Revisions of previous thoughts
  * Questions about previous decisions
  * Realizations about needing more analysis
  * Changes in approach
  * Hypothesis generation
  * Hypothesis verification
- nextThoughtNeeded: True if you need more thinking, even if at what seemed like the end
- thoughtNumber: Current number in sequence (can go beyond initial total if needed)
- totalThoughts: Current estimate of thoughts needed (can be adjusted up/down)
- isRevision: A boolean indicating if this thought revises previous thinking
- revisesThought: If is_revision is true, which thought number is being reconsidered
- branchFromThought: If branching, which thought number is the branching point
- branchId: Identifier for the current branch (if any)
- needsMoreThoughts: If reaching end but realizing more thoughts needed

You should:
1. Start with an initial estimate of needed thoughts, but be ready to adjust
2. Feel free to question or revise previous thoughts
3. Don't hesitate to add more thoughts if needed, even at the "end"
4. Express uncertainty when present
5. Mark thoughts that revise previous thinking or branch into new paths
6. Ignore information that is irrelevant to the current step
7. Generate a solution hypothesis when appropriate
8. Verify the hypothesis based on the Chain of Thought steps
9. Repeat the process until satisfied with the solution
10. Provide a single, ideally correct answer as the final output
11. Only set nextThoughtNeeded to false when truly done and a satisfactory answer is reached
```

Param descriptions (дословно, из zod `.describe()`):
- thought: "Your current thinking step"
- nextThoughtNeeded: "Whether another thought step is needed"
- thoughtNumber: "Current thought number (numeric value, e.g., 1, 2, 3)"
- totalThoughts: "Estimated total thoughts needed (numeric value, e.g., 5, 10)"
- isRevision: "Whether this revises previous thinking"
- revisesThought: "Which thought is being reconsidered"
- branchFromThought: "Branching point thought number"
- branchId: "Branch identifier"
- needsMoreThoughts: "If more thoughts are needed"

Annotations: readOnlyHint=true, destructiveHint=false, idempotentHint=true, openWorldHint=false.

## STEERING-МАРКЕРЫ

Маркер-скан по регексам исследования: 0 совпадений. Описание не содержит формулировок приоритета/вытеснения других инструментов ("instead of", "prefer", "precedence", "last resort", "must use" и т.п.). Тон директивный только внутри собственного протокола использования ("You should: ... Provide a single, ideally correct answer") — это инструкции по формату вызовов, а не steering против других инструментов.

## NOTES

- Код НЕ минифицирован — читаемый tsc-вывод с комментариями; описание инструмента — один статический template literal, риск динамической сборки строк отсутствует.
- Просмотрено 4 файла (все файлы пакета): package.json, README.md (наличие), dist/index.js (124 строки), dist/lib.js (79 строк). Покрытие исходников 100%.
- Расхождение версий: npm-пакет v2026.7.4, но серверу передаётся version "0.2.0" — косметика.
- yargs числится в dependencies, но в dist-коде не используется.
