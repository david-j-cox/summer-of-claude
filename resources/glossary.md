# Glossary

A running list of the jargon, in plain language. It grows every week. Terms are
grouped by the week they first show up, so you can always find where one was
introduced. Week 3 is a dedicated pass back over all of it.

## Week 1 - Setup and First Build

- terminal (or PowerShell): the text window where you type commands to your
  computer; where these tools run.
- agent: an AI tool that can take actions for you, such as reading and writing
  files or running commands, not just replying with text.
- model: the generative AI system (such as Claude or GPT) that produces the
  responses and chooses which tools to call. The agent is the software built around
  the model.
- prompt: the instruction or question you type to the agent.
- context: the information currently loaded for the system to use in this session
  (your prompts, the files it has read, its earlier replies). The space is limited,
  so older material eventually drops out.
- clone: making your own local copy of a shared project so you can use it and
  pull updates later.
- repository (repo): a folder of project files tracked by git so changes can be
  shared and updated.

## Week 2 - Driving the Loop

- tool: a specific action the agent is allowed to take, such as reading a file,
  editing a file, running a command, or searching the web. The model selects which
  to use.
- tool call: one use of a tool. When you watch the agent work, the steps scroll-
  ing by ("Read", "Edit", "Bash") are its tool calls.
- diff: a before-and-after view of a file showing exactly what changed, with lines
  added and removed. How you review an edit before accepting it.
- output style: a setting that changes how the agent talks to you. Explanatory
  narrates its reasoning; Learning leaves pieces for you to write.
- iterate / iteration: one round of the back-and-forth: you ask, it acts, you
  review and correct, then repeat. Most real work is many iterations, not one prompt.
- session: one continuous conversation with the agent, from launch until you
  close it or clear it. Its context lives inside the session.
- steering: redirecting the system while it works, telling it to change course,
  stop, or try something different mid-task, rather than only at the start.

## Week 3 - Jargon

How these fit together: a probabilistic generative AI model wrapped in
deterministic software. The model predicts likely text; the software (tools,
harness, the scripts you have it write) does the same thing every run and can be
relied on. ("Probabilistic" describes generative AI models specifically, not models
in general.)

- harness: the program that wraps the model and the tools together and runs the
  ask -> act -> review loop. Claude Code and Codex are harnesses. It is ordinary,
  deterministic software.
- context window: the limit on how much can be loaded at once. When it fills, older
  material is dropped or summarized, so a long session loses access to earlier parts.
- MCP (Model Context Protocol): a standard way to plug outside tools and data
  sources (a database, a web service, your files) into the harness.
- skill: a saved set of instructions (sometimes with code) that teaches the system
  to do a specific job the same way every time, on demand.
- slash command: a shortcut starting with "/" that triggers a skill or a built-in
  action (such as `/config`).
- subagent: a separate helper agent the main agent can spin up for a focused task,
  with its own context.
- hook: a command set to run automatically at a certain moment (for example before
  or after an edit), so behavior happens without you asking each time.

## Week 4 - Version Control

Git is deterministic software (the Week 3 theme again): a commit is a fixed
checkpoint that behaves the same forever. The system proposes changes; git gives
you reliable control over which ones you keep.

- commit: a saved checkpoint of your project at a moment in time, with a short
  note about what changed.
- branch: a parallel line of work, so you can try something risky without touching
  your known-good version.
- revert / undo: going back to an earlier checkpoint when a change was wrong.
- push: sending your commits up to the shared repo (like the course repo).
- pull: bringing down commits others have added.
- merge: combining the work from one branch into another.
- main branch: the stable version of the project that always works. You do not edit
  it directly; changes are made on another branch and merged in once they work.
- development / feature branch: a branch where you make and test changes before
  merging them into main. Use `development` for general work or `feature/<name>` for
  one specific change.

## Week 5 - First Domain Project

- nested (multilevel / hierarchical) data: observations grouped within larger units,
  such as sessions within participants within clinics. The grouping means the rows
  are not all independent of each other.
- mixed-effects model (multilevel model): a model for nested data that includes both
  fixed effects and random effects, so it respects the grouping.
- fixed effect: an effect estimated as the same across the whole sample, such as the
  average intervention effect.
- random effect: variation allowed to differ by group, such as each participant or
  clinic having its own level or trend.
- seed: a fixed starting value for random number generation, so a procedure that
  uses randomness gives the same result every run.
- reproducible: an analysis gives the same result when run again, because it is
  written down as a script and any randomness is pinned with a seed.
- time series: measurements taken in order over time, such as per-minute response
  counts within a session.
- autocorrelation: when values in a series are related to nearby values (one minute
  predicts the next). It breaks the assumption that observations are independent.

## Week 6 - Skills: Teacher and Checker

- instruction file (`CLAUDE.md`, `AGENTS.md`): a file of standing rules the system
  loads every session. Claude Code reads `CLAUDE.md`; Codex reads `AGENTS.md`. A
  `CLAUDE.md` can import an `AGENTS.md` (with `@AGENTS.md`) so both tools share one
  set of rules.
- always-on vs on-demand: instruction files apply every session (always in context,
  so keep them short); skills load only when used. Short rules go in the instruction
  file, multi-step procedures go in a skill.
