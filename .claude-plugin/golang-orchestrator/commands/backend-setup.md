---
name: backend-setup
description: Initiate collaborative backend configuration with Golang and Echo Router orchestration
---

# Backend Setup Command

You are orchestrating a collaborative backend configuration process using two specialized agents:

**Agent 1: Golang Expert** - Uses the Golang skill and knowledge to architect production-ready Go applications
**Agent 2: Echo Router Expert** - Uses the Echo Router skill and knowledge to implement HTTP routing and middleware

## Your Task

Based on the user's backend requirements, you must:

1. **Parse Requirements** from the user's input
2. **Spawn Two Subagents in Parallel** using the Task tool:
   - Golang Expert Agent (subagent_type: "general-purpose", skill: "effective-go")
   - Echo Router Expert Agent (subagent_type: "general-purpose", skill: "echo-router-skill")
3. **Coordinate Their Work**:
   - Golang agent focuses on: project structure, interfaces, concurrency, error handling, dependency management
   - Echo agent focuses on: routing configuration, middleware chains, HTTP handlers, request validation
4. **Synthesize Results** into a cohesive, integrated backend design

## Example User Input

"Configure a production-ready REST API for a user management system with JWT authentication, PostgreSQL database, role-based access control, and Docker support."

## What You Should Do

1. **Understand the Requirements**:
   - Project scope (REST API, microservice, real-time system, etc.)
   - Key features (authentication, databases, external integrations)
   - Infrastructure (Docker, cloud deployment, scaling needs)
   - Code style preferences (layered, hexagonal, DDD, etc.)

2. **Brief Each Subagent Clearly**:
   - Give Golang agent architecture requirements
   - Give Echo agent routing and middleware requirements
   - Share project context so both understand the overall system

3. **Spawn in Parallel**:
   ```
   Task("Design Golang Backend Architecture",
        "You are a Golang expert. Use the effective-go skill to architect...",
        "general-purpose")
   Task("Implement Echo Routing Layer",
        "You are an Echo framework expert. Use the echo-router-skill skill to implement...",
        "general-purpose")
   ```

4. **Wait for Results** and synthesize them into a unified backend design

## Integration Points to Clarify

Ensure the agents coordinate on:
- **Request/Response Types**: Shared DTOs and API contracts
- **Error Handling**: Consistent error response format
- **Middleware Stack**: Agreement on middleware ordering
- **Configuration Management**: Environment variables and config structure
- **Testing Patterns**: Unit test conventions across layers
- **Logging**: Structured logging strategy

## Invoking the Agents

When spawning agents, use this pattern:

**Golang Expert Agent:**
```
Task("Design Golang Backend Architecture",
     "You are a Golang expert. Use the effective-go skill to architect a production-ready backend for: [requirements]\n\nFocus on: project structure, database layer, business logic, error handling, configuration, testing, build setup.\n\nYour peer agent will handle HTTP routing with Echo framework. Define clear interfaces for them to depend on.",
     "general-purpose")
```

**Echo Router Expert Agent:**
```
Task("Implement Echo Routing Layer",
     "You are an Echo framework expert. Use the echo-router-skill skill to implement HTTP routing and middleware for: [requirements]\n\nFocus on: Echo setup, routes, middleware stack, request validation, authentication, error handling, response formatting.\n\nYour peer agent designed the core architecture. Build handlers that call their service layer interfaces.",
     "general-purpose")
```

**Important:** Both agents should be spawned in parallel (single message, multiple Task calls).

## Example Brief to Golang Agent

```
You are a Golang expert. Using your Golang skill knowledge, architect the backend for:
[requirements]

Focus on:
- Project structure and package organization
- Database abstraction layer and models
- Error handling with custom error types
- Configuration management (environment-based)
- Dependency injection patterns
- Testing structure
- Build and deployment setup

Your peer agent is an Echo Router expert who will handle the HTTP routing and middleware.
Define clear interfaces that the routing layer will depend on.
```

## Example Brief to Echo Agent

```
You are an Echo Router expert. Using your Echo Router skill knowledge, implement the HTTP routing and middleware layer for:
[requirements]

Focus on:
- Echo server setup and configuration
- Route definitions and grouped routes
- Middleware chains and ordering
- Request validation and binding
- Authentication/authorization middleware
- CORS and security headers
- Static file serving (if needed)
- Error handling and recovery

Your peer agent is a Golang expert who designed the core business logic layer.
Build handlers that depend on the interfaces they defined.
```

## Success Criteria

Both agents complete and you deliver:
- ✅ Complete project structure diagram
- ✅ Architecture overview showing components and relationships
- ✅ Go package structure with clear responsibilities
- ✅ Echo router configuration with all routes and middleware
- ✅ Type definitions for requests/responses
- ✅ Example handlers and business logic patterns
- ✅ Testing strategy and examples
- ✅ Docker configuration (if requested)
- ✅ Documentation and quick start guide
