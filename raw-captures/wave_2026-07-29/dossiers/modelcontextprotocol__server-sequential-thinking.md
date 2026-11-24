# UNIT: @modelcontextprotocol/server-sequential-thinking | npm v2026.7.4 (published 2026-07-04T23:05:13.130Z) | frames: npm-top | captured 2026-07-29 (static, tarball)

## VERDICT: MCP server

A real MCP server on stdio transport: `dist/index.js` creates `new McpServer({ name: "sequential-thinking-server", version: "0.2.0" })`, registers one tool via `server.registerTool(...)` and connects `StdioServerTransport`. Business logic is in `dist/lib.js` (class `SequentialThinkingServer`). No network activity, file operations, or code execution — purely an in-memory journal of "thoughts".

## CHANNEL: instructions, npm (static)
(not found statically)

The `McpServer` constructor receives only `{ name, version }` — there is no `instructions` field either in the constructor or anywhere else in the package code.

## CHANNEL: tool descriptions, npm (static, coverage=full)

Tools: 1 (<= 40, included in full).

### Tool 1: `sequentialthinking` (title: "Sequential Thinking")

Description (verbatim):

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

Param descriptions (verbatim, from zod `.describe()`):
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

## STEERING-MARKERS

Marker scan for research regexes: 0 matches. The description does not contain priority/displacement formulations for other tools ("instead of", "prefer", "precedence", "last resort", "must use", etc.). The tone is directive only within its own usage protocol ("You should: ... Provide a single, ideally correct answer") — these are call-format instructions, not steering against other tools.

## NOTES

- The code is NOT minified — readable tsc output with comments; the tool description is a single static template literal, and there is no risk of dynamic string assembly.
- Reviewed 4 files (all package files): package.json, README.md (presence), dist/index.js (124 lines), dist/lib.js (79 lines). Source coverage 100%.
- Version mismatch: npm package v2026.7.4, but version "0.2.0" is passed to the server — cosmetic.
- yargs is listed in dependencies, but is not used in the dist code.
