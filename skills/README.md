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

## Planned

- `/explain`: repo tutor that explains any file, function, or the architecture at a
  chosen depth, traces data flow, and quizzes the student. (Week 6)
- `/check-assumptions`: before reporting any statistical result, states the test's
  assumptions, checks each against the data, flags violations, and suggests better
  methods. (Week 6)
- More added in Weeks 7-9.

## How to use

Each skill ships as a folder you drop into your own project (Claude Code) or adapt
as a prompt or `AGENTS.md` snippet (Codex). Install instructions live with each
skill above.
