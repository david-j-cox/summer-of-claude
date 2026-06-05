# Week 6 - Skills: Teacher and Checker

Goal for the week: stop relying on your memory for good practice. Write down the
questions and steps you want followed every time, and have the system follow them.
You do not need to know everything. You need to make sure the system is doing the
right things, and you can encode that.

This week you set up project instruction files and two skills: one that has the
system teach you the project, and one that has the system check its own statistics
before reporting them.

## Two ways to give standing instructions

You met skills in Week 3 and used one in Week 4 (`git-workflow`). There are two
related tools:

- Instruction files (`CLAUDE.md`, `AGENTS.md`): always-on standing rules. The system
  loads them at the start of every session, so they apply to everything. Use them for
  facts and "always do X" rules. Keep them short, since they are always in context.
- Skills: on-demand procedures. They load only when you run them or when the system
  detects the task matches. Use them for multi-step jobs.

A rough split: a short rule goes in the instruction file; a procedure goes in a skill.

### Setting up the instruction files

Copy the templates from `resources/templates/` into your project:

- `AGENTS.md` holds the shared rules. Codex reads it automatically.
- `CLAUDE.md` imports `AGENTS.md` (with the line `@AGENTS.md`) so Claude Code reads
  the same rules. Claude Code does not read `AGENTS.md` on its own, which is why the
  small `CLAUDE.md` exists.

Edit them to fit your project, then start a new session and confirm the system is
following them.

## Skill 1: /explain (teacher mode)

`skills/explain/` is a skill that turns the system into a tutor for whatever project
you are in. It explains any file, function, or the overall structure at the depth you
ask for, traces how data flows through the project, and quizzes you to check that it
stuck. It is read-only, so it will not change your files.

Install it by copying the `explain` folder into `.claude/skills/` (or
`~/.claude/skills/`), then run `/explain` or `/explain <file or topic>`. Codex users:
paste the steps from `skills/explain/SKILL.md` into a session.

Use it on this very repo, or on the analysis you built in Week 5.

## Skill 2: /check-assumptions (self-policing)

`skills/check-assumptions/` is the spine skill of the course. Before the system
reports a statistical result, this skill makes it state the method's assumptions,
check each one against the actual data, flag violations with evidence, name a better
method when one is violated, and separate numbers it actually computed from anything
it merely asserted. That last part matters: the system can produce a confident result
it never actually ran (you raised this in Week 5). This skill makes it show the code
and output behind every number.

Install it the same way and run `/check-assumptions` when you are about to report or
interpret an analysis. You will lean on it heavily in Week 8.

## Exercise: write your own skill

Pick one check or task you keep repeating and turn it into a skill. A skill is a
folder with a `SKILL.md` file: a short description of when to use it, and the steps to
follow. Copy `skills/check-assumptions/SKILL.md` as a starting shape, change the steps
to your task, and try it. Ask the system to help you write it, then read what it wrote
and make sure the steps are actually what you want.

## The idea to take with you

`/explain` has the system teach you; `/check-assumptions` has the system check itself.
Both are the same move: a question or procedure you care about, written down once so it
happens every time instead of only when you remember. This is how you work with tools
you do not fully understand yet and still trust the output. You are not memorizing
everything. You are making sure the right questions get asked.

## Words you met this week

- instruction file (`CLAUDE.md`, `AGENTS.md`): a file of standing rules the system
  loads every session. `CLAUDE.md` is read by Claude Code; `AGENTS.md` is read by
  Codex; a `CLAUDE.md` can import `AGENTS.md` so both share one set of rules.
- always-on vs on-demand: instruction files apply every session; skills load only
  when used. Short rules go in the instruction file, procedures go in a skill.

Full running glossary: ../resources/glossary.md
