# Go TDD Plugin

TDD workflow for Go using stretchr/testify and testcontainers-go. Orchestrates parallel subagents to write unit tests, integration tests, and execute the red-green-refactor cycle.

## Features

- **Parallel agent execution** for faster test writing
- **Unit tests** with testify assertions, mocks, and table-driven patterns
- **Integration tests** with testcontainers-go for real services
- **TDD workflow** support with test execution and iteration

## Usage

```
/go-tdd [description of what to test]
```

### Examples

```bash
# Unit tests for a function
/go-tdd write tests for the CalculateDiscount function

# Integration tests for a repository
/go-tdd test the UserRepository with PostgreSQL

# Mixed scope (dispatches both agents in parallel)
/go-tdd implement TDD for the OrderService

# Run and fix tests
/go-tdd run the tests and fix any failures
```

## Components

### Skill: testify-tdd

Comprehensive knowledge base for stretchr/testify:
- `assert` vs `require` usage patterns
- Interface mocking with `testify/mock`
- Test suite organization with `testify/suite`
- Table-driven test patterns
- TDD workflow guidance

### Command: /go-tdd

Entry point that analyzes your request and dispatches appropriate agents:

| Request Type | Agent(s) Dispatched |
|--------------|---------------------|
| Pure functions, utilities | unit-test-agent |
| Database, cache, external services | integration-test-agent |
| Services, handlers (mixed) | Both agents in parallel |
| Run/fix tests | test-runner-agent |

### Agents

#### unit-test-agent (green)
- Writes unit tests for pure Go code
- Creates mocks for interface dependencies
- Uses table-driven tests for multiple scenarios
- Same-package testing style

#### integration-test-agent (blue)
- Writes integration tests with testcontainers-go
- Spins up real PostgreSQL, Redis, Kafka, etc.
- Black-box testing style (`_test` package)
- Proper cleanup and wait strategies

#### test-runner-agent (orange)
- Executes `go test` commands
- Analyzes test failures
- Implements minimal fixes (TDD Green phase)
- Suggests refactoring opportunities

## Prerequisites

- Go 1.21+
- Docker (for integration tests with testcontainers)
- stretchr/testify: `go get github.com/stretchr/testify`
- testcontainers-go: `go get github.com/testcontainers/testcontainers-go`

## Integration with testcontainers-go Plugin

The `integration-test-agent` references the `testcontainers-go` skill for comprehensive container patterns. Ensure you have the testcontainers-go plugin installed for best results.

## Test Patterns Supported

### Unit Tests
- Table-driven tests
- Interface mocking
- Test suites with setup/teardown
- Error case testing

### Integration Tests
- Database repository tests
- Cache layer tests
- Message queue tests
- Multi-container networking

## TDD Workflow

1. **Red**: Write failing tests first
2. **Green**: Implement minimal code to pass
3. **Refactor**: Improve code while keeping tests green

The plugin supports this full cycle:
```bash
# Write tests (Red)
/go-tdd write tests for ShippingCalculator

# After tests are written, run them
/go-tdd run the tests

# Fix failures (Green) and refactor
/go-tdd fix the failing tests
```
