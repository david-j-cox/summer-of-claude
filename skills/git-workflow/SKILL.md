---
name: Git workflow guardrails
description: Safe git practices for changing code in a repository. Keep main stable and work on a development or feature branch, never commit directly to main, checkpoint before risky changes, show and explain the diff before every commit, and write clear commit messages. Use whenever you are about to modify files in a git repository.
allowed-tools: Bash(git status:*) Bash(git diff:*) Bash(git log:*) Bash(git branch:*)
---

# Git workflow guardrails

Follow these practices for any change to a git repository. Say what you are doing at
each step so the user can follow along.

## At the start

1. Run `git status` and report the current branch and whether the working tree is
   clean.
2. If the current branch is `main` (or `master`), do not make changes there.
   Propose a working branch and ask the user to confirm the name, then create and
   switch to it:
   - `development` for general ongoing work, or
   - `feature/<short-name>` for one specific change.

## Before a risky or non-trivial change

1. If there are uncommitted changes worth keeping, commit them first as a
   checkpoint so the earlier state can be restored.
2. State in one or two sentences what you are about to change and why.

## Before every commit

1. Run `git diff` and `git status` and show the user exactly what changed.
2. Explain the change in plain language. Call out anything you touched that was not
   requested, and anything you deleted.
3. Wait for the user to confirm before committing. Do not commit a diff the user has
   not seen.

## Commit messages

- Write a short, specific message saying what changed and why.
- Keep one logical change per commit. Do not bundle unrelated edits together.

## Merging back to main

- Merge a working branch into `main` only after the change has been reviewed and
  confirmed to work.
- Before merging, summarize what will land on `main`.

## Keep the user learning

- When you run a git command the user may not know, say in one line what it does.
- If the user asks why, explain the reasoning rather than only running the command.
