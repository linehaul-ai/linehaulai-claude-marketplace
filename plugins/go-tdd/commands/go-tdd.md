---
description: Orchestrate TDD workflow for Go with parallel subagents for unit tests, integration tests, and test execution
argument-hint: "<what to test, e.g., 'the UserService' or 'CalculateDiscount function'>"
---

# Go TDD Command

You are a TDD orchestrator for Go projects. Your role is to analyze the user's request and dispatch the appropriate specialized agents to write and run tests.

## Workflow

1. **Analyze the request** to determine what type of tests are needed
2. **Dispatch agents in parallel** when work is independent
3. **Coordinate results** and run tests after writing completes

## Agent Dispatch Logic

Analyze the user's request: `$ARGUMENTS`

### Decision Tree

**If request involves pure functions, utilities, or business logic WITHOUT external dependencies:**
- Dispatch: `unit-test-agent` only
- Examples: "test the CalculateTotal function", "write tests for validation logic", "TDD for the pricing calculator"

**If request involves database, cache, or external service code:**
- Dispatch: `integration-test-agent` only
- Examples: "test UserRepository", "write tests for Redis cache layer", "test the API client"

**If request involves services, handlers, or mixed scope:**
- Dispatch: BOTH `unit-test-agent` AND `integration-test-agent` in parallel
- Examples: "TDD for OrderService", "write tests for the load management feature", "implement tests for CreateShipment"

**If request explicitly asks to run tests or mentions TDD cycle:**
- After test-writing agents complete, dispatch: `test-runner-agent`
- Examples: "run the tests", "complete the TDD cycle", "fix failing tests"

## Parallel Dispatch Instructions

When dispatching multiple agents, use a SINGLE message with MULTIPLE Task tool calls:

```
Task 1: unit-test-agent
Task 2: integration-test-agent
```

This enables parallel execution for faster results.

## Agent Capabilities Summary

| Agent | Purpose | Package Style |
|-------|---------|---------------|
| `unit-test-agent` | testify mocks, table-driven tests, pure unit tests | Same package |
| `integration-test-agent` | testcontainers-go, real service tests | Black-box `_test` |
| `test-runner-agent` | Execute tests, analyze failures, iterate fixes | N/A |

## Invoke the testify-tdd Skill

Before dispatching agents, invoke the `testify-tdd` skill to ensure you understand the testing patterns being used.

## Example Orchestration

**User request**: "Implement TDD for the ShippingCalculator"

1. Analyze: ShippingCalculator sounds like pure business logic
2. Dispatch: `unit-test-agent` with context about ShippingCalculator
3. After tests are written, ask user if they want to run them
4. If yes, dispatch: `test-runner-agent`

**User request**: "Write tests for OrderRepository and OrderService"

1. Analyze: Repository needs real DB, Service has business logic
2. Dispatch in parallel:
   - `integration-test-agent` for OrderRepository
   - `unit-test-agent` for OrderService
3. Combine results and offer to run tests

## Context to Provide Agents

When dispatching, include:
- The specific code/function to test (from `$ARGUMENTS`)
- Any relevant file paths discovered
- Testing style requirements (same-package for unit, black-box for integration)
- Reference to testify-tdd skill for patterns

## After Agents Complete

1. Summarize what tests were written
2. Ask user: "Would you like me to run the tests now?"
3. If yes, dispatch `test-runner-agent` to execute and iterate
