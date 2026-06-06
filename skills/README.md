# Take-Home Skills

Downloadable skills students collect across the series. Each is "a question (or a
job) encoded as a skill" so the agent does it every time without the student having
to remember.

## Available now

### git-workflow (introduced Week 4)

A guardrail that tells the system to keep `main` stable, work on a development or
feature branch, checkpoint before risky changes, and show and explain every diff
before committing.

Install (Claude Code):

- For one project: copy the `git-workflow/` folder into that project's
  `.claude/skills/` so the path is `.claude/skills/git-workflow/SKILL.md`.
- For all your projects: copy it into `~/.claude/skills/` instead.
- Start the system in that project and run `/git-workflow`, or just work normally
  and it will apply when you change code.

Use with Codex:

- Codex does not use this folder format. Open `git-workflow/SKILL.md`, copy the
  instruction steps into your project's `AGENTS.md` (or paste them at the start of a
  session) so Codex follows the same practices.

Caveat: a skill is an instruction the system follows, not a hard lock. Keep
reviewing the diffs. Week 9 covers hooks, which can enforce steps automatically.

### explain (introduced Week 6)

A read-only tutor for whatever project you are in. It explains any file, function, or
the overall structure at the depth you ask for, traces how data flows through the
project, and quizzes you to check understanding. Install by copying the `explain/`
folder into `.claude/skills/` (or `~/.claude/skills/`), then run `/explain` or
`/explain <file or topic>`. Codex users: paste the steps from `explain/SKILL.md` into
a session.

### check-assumptions (introduced Week 6)

The most important skill in the course, and the one you will use most often. Before
the system reports a statistical result, it
states the method's assumptions, checks each against the data, flags violations with
evidence, names a better method when one is violated, and separates numbers actually
computed from anything merely asserted (a guard against confident but un-run results).
Install the same way and run `/check-assumptions` when about to report or interpret an
analysis. Used heavily in Week 8.

### test-first (introduced Week 7)

Enforces test-before-code so the system cannot write a bug and a test that blesses it
in one go. It states the expected behavior, gets your confirmation, writes a test,
runs it and shows it failing for the right reason, then implements until it passes,
including an edge case. Install by copying the `test-first/` folder into
`.claude/skills/` (or `~/.claude/skills/`), then run `/test-first`. Codex users: paste
the steps from `test-first/SKILL.md` into a session.

### challenge-result (introduced Week 8)

Takes the opposite stance to `check-assumptions`: instead of a checklist, it tries to
prove a result wrong. It lists the most likely ways a finding could be false
(assumption violations, data leakage, type coercion, multiple comparisons, confounds,
code errors, overfitting), checks the ones that can be checked, and reports which
threats survive. Install by copying the `challenge-result/` folder into
`.claude/skills/` (or `~/.claude/skills/`), then run `/challenge-result`. Codex users:
paste the steps from `challenge-result/SKILL.md` into a session.

## Planned

- More added in Week 9.

## How to use

Each skill ships as a folder you drop into your own project (Claude Code) or adapt
as a prompt or `AGENTS.md` snippet (Codex). Install instructions live with each
skill above.
