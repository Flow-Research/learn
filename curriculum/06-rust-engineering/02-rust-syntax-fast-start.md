---
id: rust-syntax-fast-start
title: Rust Syntax Fast Start
track: rust-engineering
level: foundation
version: 1.0
---

# Rust Syntax Fast Start

## Watch First

<div style={{position: 'relative', paddingBottom: '56.25%', height: 0, overflow: 'hidden', maxWidth: '100%', marginBottom: '1.5rem'}}>
  <iframe
    src="https://www.youtube.com/embed/zF34dRivLOw"
    title="Rust Crash Course | Rustlang"
    style={{position: 'absolute', top: 0, left: 0, width: '100%', height: '100%', border: 0}}
    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
    referrerPolicy="strict-origin-when-cross-origin"
    allowFullScreen
  />
</div>

## Why This Matters

This path assumes you can already program, but not that you know Rust. This lesson gives you enough syntax to read the rest of the path without pausing every line.

Rust syntax looks familiar if you know JavaScript, TypeScript, Go, C, Java, Python, or Solidity, but the meaning is stricter. Variables are immutable by default. Types are checked at compile time. Errors are values. `match` is normal control flow. Ownership affects whether a value is moved, borrowed, cloned, or mutated.

## What You Will Build

Create a small `task_summary` program that defines task data, validates input, formats a response, and returns errors without panicking.

## The Shape Of A Rust Program

A Rust binary starts in `main`. Functions use `fn`, blocks use braces, and most statements end with semicolons.

```rust
fn main() {
    let name = "Rust";
    println!("Hello, {name}");
}
```

`println!` has an exclamation mark because it is a macro. You do not need to understand macros yet. For now, read `println!` as "print formatted text."

Variables are immutable unless you write `mut`:

```rust
let count = 1;
// count = 2; // does not compile

let mut retries = 0;
retries += 1;
```

Use `let` again when you want to transform a value into a new value. This is called shadowing:

```rust
let input = "  Ship release notes  ";
let input = input.trim();
let input = input.to_lowercase();
```

Shadowing is useful when each step produces a better version of the value. `mut` is useful when the same variable truly changes over time.

## Types And Functions

Rust can infer many types, but function signatures should be explicit:

```rust
fn normalize_title(title: &str) -> String {
    title.trim().to_lowercase()
}
```

Read `&str` as "borrowed string slice." The function can read the text, but it does not own it. Read `String` as "owned, growable string." The function returns a new owned value.

Numbers and booleans look direct:

```rust
let limit: usize = 50;
let is_ready: bool = limit > 0;
```

Use `usize` for collection indexes and lengths. Use explicit integer types such as `i64`, `u64`, or `i32` when data crosses a database, API, or file boundary.

## Structs, Enums, And Methods

Use a `struct` when a thing has named fields:

```rust
#[derive(Debug, Clone)]
struct Task {
    id: u64,
    title: String,
    status: TaskStatus,
}
```

Use an `enum` when a value can be one of a known set of choices:

```rust
#[derive(Debug, Clone, PartialEq, Eq)]
enum TaskStatus {
    Draft,
    Ready,
    Blocked(String),
    Done,
}
```

An enum variant can carry data. `Blocked(String)` means a blocked task also stores the reason.

Use `impl` to add methods:

```rust
impl Task {
    fn is_finished(&self) -> bool {
        matches!(self.status, TaskStatus::Done)
    }
}
```

Read `&self` as "this method borrows the task." It can inspect the task without taking ownership of it.

## Match, Option, And Result

`match` forces you to handle every case:

```rust
fn status_label(status: &TaskStatus) -> &str {
    match status {
        TaskStatus::Draft => "draft",
        TaskStatus::Ready => "ready",
        TaskStatus::Blocked(_) => "blocked",
        TaskStatus::Done => "done",
    }
}
```

Rust does not use `null` for normal optional values. It uses `Option<T>`:

```rust
fn first_tag(tags: &[String]) -> Option<&str> {
    tags.first().map(|tag| tag.as_str())
}
```

An `Option<T>` is either `Some(value)` or `None`. You must handle both before using the value.

Recoverable errors use `Result<T, E>`:

```rust
fn parse_limit(input: &str) -> Result<usize, String> {
    let limit = input
        .parse::<usize>()
        .map_err(|_| "limit must be a positive number".to_string())?;

    if limit == 0 {
        return Err("limit must be greater than zero".to_string());
    }

    Ok(limit)
}
```

The `?` operator means: if this is `Ok(value)`, unwrap the value and continue; if this is `Err(error)`, return the error from the current function.

## Borrow, Move, Clone

Rust cares about who owns a value. These three choices appear constantly:

```rust
fn read_title(task: &Task) {
    println!("{}", task.title);
}

fn take_task(task: Task) {
    println!("owned task: {}", task.title);
}

fn copy_title(task: &Task) -> String {
    task.title.clone()
}
```

`&Task` borrows a task. `Task` moves ownership into the function. `.clone()` creates a new owned copy. Cloning is sometimes correct, but it should be intentional because it can hide poor ownership design.

## Modules And Cargo

Cargo is Rust's project tool. You will use it constantly:

```bash
cargo new task-summary
cd task-summary
cargo check
cargo test
cargo run
```

Inside a project, modules split code into namespaced files:

```rust
mod domain;
mod parser;

use domain::Task;
```

Start simple. A beginner-friendly project can keep `main.rs`, `domain.rs`, and `parser.rs` before introducing workspaces or many crates.

## Practice

Build `task_summary` with one `Task` struct, one `TaskStatus` enum, a `normalize_title` function, and a `parse_limit` function that returns `Result<usize, String>`.

Then add three tests:

- a title with spaces becomes trimmed and lowercase,
- `parse_limit("20")` returns `Ok(20)`,
- `parse_limit("0")` returns an error.

You are ready to continue when you can explain the difference between `String` and `&str`, `Option` and `Result`, `match` and `if`, `&T` and `T`, and `mut` and shadowing.

## Curated Resources

- [Rust Book: Common Programming Concepts](https://doc.rust-lang.org/book/ch03-00-common-programming-concepts.html) — variables, data types, functions, comments, and control flow.
- [Rust Book: Structs](https://doc.rust-lang.org/book/ch05-00-structs.html) — named data types and methods.
- [Rust Book: Enums and Pattern Matching](https://doc.rust-lang.org/book/ch06-00-enums.html) — enums, `Option`, and `match`.
- [Rust Book: Error Handling](https://doc.rust-lang.org/book/ch09-00-error-handling.html) — `Result`, `panic!`, and recoverable errors.

## Next Step

Continue to [Ownership, Borrowing, Lifetimes, and Memory Thinking](03-ownership-borrowing-lifetimes-memory-thinking.md).
