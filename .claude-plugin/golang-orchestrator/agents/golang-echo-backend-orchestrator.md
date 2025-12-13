---
name: golang-echo-backend-orchestrator
description: Orchestrates two specialized subagents - one with Golang expertise and one with Echo Router expertise - to collaboratively design, implement, and configure a production-ready Go backend with Echo routing framework
---

# Golang Echo Backend Orchestrator

## Overview

This skill orchestrates two specialized subagents to collaboratively configure a production-ready Golang backend with Echo routing framework.

## Agents Involved

1. **Golang Expert Agent** - Applies best practices for Go development, code structure, and idioms
2. **Echo Router Agent** - Specializes in Echo framework patterns, routing, middleware, and HTTP handler design

## Orchestration Process

When triggered, this skill:

1. **Analyzes Requirements** - Gathers project specifications and constraints
2. **Spawns Subagents in Parallel** - Initializes both specialists simultaneously with coordinated context
3. **Facilitates Collaboration** - Manages communication between agents through shared memory
4. **Synthesizes Results** - Combines outputs into a cohesive, production-ready backend configuration

## How It Works

The orchestrator spawns two subagents with these instructions:

### Subagent 1: Golang Expert
- Uses your Golang skill to architect the backend
- Focuses on: project structure, error handling, interfaces, concurrency patterns
- Ensures idiomatic Go code following effective-go principles
- Sets up: dependency management, build configuration, environment safety

### Subagent 2: Echo Router Expert
- Uses your Echo Router skill to implement routing and middleware
- Focuses on: HTTP handlers, middleware chains, request/response binding
- Implements: routing patterns, authentication middleware, static file serving
- Configures: error handling, validation, CORS, rate limiting

## Collaboration Pattern

Both agents work with:
- **Shared Context**: Project requirements stored in memory
- **Coordination**: Updates about completed components
- **Integration Points**: Agreement on interfaces between routing and business logic
- **Testing Strategy**: Coordinated test coverage across layers

## Usage

Ask the plugin to configure a backend with specific requirements:

```
Configure a production-ready REST API backend for a user management system using Golang and Echo Router
```

Or use the `/backend-setup` command:

```
/backend-setup Configure a user management system with authentication and role-based access control
```

The orchestrator will:
1. Parse your requirements
2. Spawn both specialist agents
3. Coordinate their efforts
4. Generate production-ready code structure and configuration

## Expected Outputs

- Go project structure with proper organization
- Echo router configuration with optimized middleware chain
- Type-safe request/response handlers
- Environment-based configuration setup
- Database abstraction layer design
- Error handling patterns
- Test structure and examples
- Docker configuration (if applicable)
- API documentation structure

## Customization

Provide specific requirements in your prompt:

- **Architecture Style**: Layered, hexagonal, MVC, clean architecture
- **Database**: PostgreSQL, MySQL, MongoDB, etc.
- **Authentication**: JWT, OAuth2, session-based
- **Middleware Stack**: CORS, logging, rate limiting, etc.
- **Features**: User management, business logic, integrations
- **Deployment**: Docker, Kubernetes, cloud-native patterns

The agents will adapt their collaboration to match your exact needs.
