# Project instructions

Standing instructions for any AI coding tool working in this project. Codex reads
this file (`AGENTS.md`) automatically. For Claude Code, see the companion
`CLAUDE.md`, which imports this file. Keep this short; long instruction files are
followed less reliably.

## How to work

- Explain what you are doing as you go, and say why you made each choice.
- When you make a decision for me (a default, a method, a cleaning rule), say so and
  explain it. I own those decisions.
- Prefer writing a script over running loose one-off commands, so the work can be
  rerun and checked.

## Data and analysis

- Treat the data structure seriously. This project uses nested data (for example,
  repeated measures within participants within groups). Do not treat rows as
  independent unless that is justified.
- Before reporting any statistical result, follow the `check-assumptions` skill:
  state the method's assumptions, check each against the data, flag violations, and
  say whether a better method exists.
- Do not report a statistic, p-value, or effect size you did not actually compute.
  Show the code and the output that produced each number.
- Set a seed anywhere randomness is involved, so results are reproducible.

## Version control

- Keep `main` stable. Work on a development or feature branch.
- Show me the diff and explain it before committing. Do not commit a diff I have not
  seen.
- See the `git-workflow` skill for the full workflow.

## Asking first

- Ask before deleting files, overwriting data, or anything hard to undo.
