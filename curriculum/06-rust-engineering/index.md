---
title: Rust Engineering
description: A practical learning path for builders who want to design, ship, and operate reliable Rust systems.
image: /img/og/rust-engineering/card.jpg
sidebar_position: 0
---

# Rust Engineering

Rust Engineering is a practical learning path for builders who want to use Rust to design, ship, and operate reliable systems: backend APIs, protocol services, async workers, CLI tools, data pipelines, infrastructure utilities, application foundations, WebAssembly modules, embedded programs, and performance-sensitive libraries.

This path does not replace [The Rust Programming Language](https://doc.rust-lang.org/book/). The official Rust materials teach the language. This path teaches the engineering judgment around Rust: how to model systems, choose boundaries, avoid over-abstraction, use AI responsibly, and ship code other people can review, extend, and operate.

> AI can make Rust code easier to produce, but humans still need to steer the architecture, ownership model, error boundaries, abstractions, security posture, and product taste.

## Who This Path Is For

- Builders coming from Python, JavaScript, TypeScript, Go, Solidity, or general backend engineering.
- Engineers who want to understand Rust beyond syntax and compiler errors.
- Developers building backend services, CLIs, workers, protocol tooling, data pipelines, agent infrastructure, or open-source infrastructure.
- Learners who can use AI to generate code but want the senior judgment to know what code should exist.

## What You Will Learn

By the end of the path, you should be able to:

- Read Rust compiler errors without panic.
- Read common Rust syntax: `let`, `mut`, `fn`, structs, enums, `impl`, `match`, `Option`, `Result`, references, and modules.
- Use ownership, borrowing, and lifetimes as design tools.
- Model product concepts with structs, enums, newtypes, and state machines.
- Build reusable code without copying inheritance-heavy OOP patterns.
- Design clean Axum APIs with typed extractors, state, responses, and middleware.
- Use SQLx with explicit SQL and practical repository/service boundaries.
- Build reusable CRUD without hiding important behavior behind generic magic.
- Use async Rust and Tokio for services, workers, queues, timeouts, cancellation, and graceful shutdown.
- Review AI-generated Rust for architectural mistakes.
- Structure Rust projects so humans and coding agents can navigate them consistently.
- Ship tested, observable, documented, and deployable Rust software.

## How To Use This Path

You can move through the lessons in order, or jump to the topic that matches the system you are building. The lessons are cohesive because they reuse the same engineering vocabulary: ownership, boundaries, explicit errors, typed data, small abstractions, reviewable behavior, and production feedback loops.

Backend engineers will see Axum, SQLx, services, authentication, and observability. CLI, data, infrastructure, protocol, WASM, and embedded engineers should still use the early lessons on ownership, modeling, modules, traits, concurrency, testing, performance, and review culture. The web stack is the default applied example, not the only destination.

## Default Stack And Tools

```text
Language: current stable Rust; examples assume Rust 2024 where practical
Tooling: rustup, cargo, rustfmt, clippy, rust-analyzer
Task runner: just or make, used lightly
Web/API default: Axum
Async runtime default: Tokio
Middleware/services default: Tower and tower-http
Database default: PostgreSQL
DB access default: SQLx
Serialization: Serde
Errors: thiserror for typed errors, anyhow for application-level context
Observability: tracing and tracing-subscriber
API docs: OpenAPI with utoipa or equivalent
Testing: cargo test, integration tests, HTTP tests, DB-backed tests
Architecture: domain, application, infrastructure, interfaces, workers
Deployment: Docker, CI, dependency audit, release checklist
Optional lab: predictable explicit-code CLI scaffolding for repeatable resource slices
```

These defaults give the path a concrete through-line. When your goal is not a web service, translate the same ideas into your domain: a CLI has commands instead of routes, a protocol node has message handlers instead of HTTP handlers, a data tool has parsing and transformation boundaries, and an embedded program has stricter runtime and allocation constraints.

## Modules

1. [Rust Mindset, Toolchain, and Engineering Loop](01-rust-mindset-toolchain-engineering-loop.md) — setup, compiler feedback, documentation, and a first CLI artifact.
2. [Rust Syntax Fast Start](02-rust-syntax-fast-start.md) — the syntax bridge for programmers who are new to Rust.
3. [Ownership, Borrowing, Lifetimes, and Memory Thinking](03-ownership-borrowing-lifetimes-memory-thinking.md) — ownership as a design model, not a syntax puzzle.
4. [Data Modeling, Errors, and Control Flow](04-data-modeling-errors-control-flow.md) — structs, enums, pattern matching, `Option`, `Result`, typed errors, and boundary validation.
5. [Reuse Without OOP](05-reuse-without-oop.md) — traits, generics, newtypes, conversion traits, composition, and restrained abstraction.
6. [Modules, Crates, Workspaces, and Project Shape](06-modules-crates-workspaces-project-shape.md) — project organization, visibility, configuration, features, and ADRs.
7. [Smart Pointers, Shared State, and Concurrency Basics](07-smart-pointers-shared-state-concurrency.md) — `Box`, `Rc`, `Arc`, locks, atomics, threads, channels, `Send`, and `Sync`.
8. [Async Rust and Tokio](08-async-rust-and-tokio.md) — futures, runtime setup, tasks, channels, timeouts, cancellation, graceful shutdown, and backpressure.
9. [Axum-First Web Engineering](09-axum-first-web-engineering.md) — routers, handlers, extractors, state, middleware, responses, and OpenAPI.
10. [Persistence and Reusable CRUD With SQLx](10-persistence-reusable-crud-sqlx.md) — migrations, pools, DTOs, explicit SQL, transactions, pagination, and reusable CRUD without generic magic.
11. [Service-Layer Architecture and Domain Boundaries](11-service-layer-architecture-domain-boundaries.md) — keeping HTTP, persistence, domain logic, and workers from tangling.
12. [Application Framework and Scaffolding Lab](12-application-framework-scaffolding-lab.md) — compare manual Axum + SQLx structure with predictable explicit-code scaffolding.
13. [Testing, Fixtures, and Code Review Culture](13-testing-fixtures-code-review-culture.md) — domain, HTTP, database, integration, doctest, benchmark, and review workflows.
14. [Security, Authentication, and API Safety](14-security-authentication-api-safety.md) — identity, auth, authorization, secrets, safe responses, and supply-chain checks.
15. [Observability, Performance, and Deployment](15-observability-performance-deployment.md) — tracing, health, metrics, performance measurement, Docker, and CI/CD.
16. [Beyond Backend](16-beyond-backend-cli-data-protocols-wasm-embedded.md) — CLI, parsing, data processing, protocol tooling, WASM, embedded, and FFI awareness.
17. [Macros, Unsafe Rust, and Advanced Escape Hatches](17-macros-unsafe-advanced-escape-hatches.md) — macros, generated behavior, unsafe invariants, and review discipline.
18. [AI-Assisted Rust Engineering](18-ai-assisted-rust-engineering.md) — spec-first prompting, compiler-guided iteration, code smell review, and human simplification.
19. [Production Service Capstone](19-production-service-capstone.md) — build, test, document, deploy, and review a portfolio-grade Rust service.

## Core Message

Rust is not only a backend language and it is not only a systems language. It is a language for making important constraints visible: who owns data, who may mutate it, which states are valid, which failures are recoverable, which operations need synchronization, and which abstractions are worth keeping.

The best Rust code is usually explicit before it is clever. Use types to express meaning, modules to shape responsibility, traits and generics to remove real duplication, tests to protect behavior, observability to understand production, and AI as an accelerator that still needs human architectural judgment.
