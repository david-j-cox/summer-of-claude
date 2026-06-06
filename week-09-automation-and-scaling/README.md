# Week 9 - Automation and Scaling
Goal for the week: take the steps you now do by hand and have them run automatically,
so that they happen consistently and you can take on larger work. The catch is that
automation hides the steps it runs, so the more you automate, the more deliberately you
have to validate. This week covers the tools for automating, and where automating is
and is not a good idea.

## From instructions to enforcement
So far you have given the system standing instructions (the `CLAUDE.md` and `AGENTS.md`
files) and on-demand skills. Both tell the system what to do, and it usually does. A
hook is different. A hook is a command the tool runs automatically at a set point, and
it runs every time regardless of the model. Use a hook for the few things that must
always happen.

`resources/templates/hooks/` has a working example: a hook that blocks any git commit
made directly on `main`. The `git-workflow` skill from Week 4 asks for this; the hook
requires it. Install it by following the README there. Hooks can also run your tests or
a linter (a tool that automatically checks code for errors and style problems) after
every edit, log every command, or warn before risky actions. Pick the event, match the
tool, run a command.

## Subagents
A subagent is a separate helper the main session can start for a focused task, with its
own context. It is useful when a job would otherwise fill up the main session, or when
you want a fresh, independent pass.

How to launch a subagent: just ask, in plain language. Tell the system to use a subagent for the task, for example:

> "Use a subagent to run /challenge-result on this finding and report back only the
> verdict."

The subagent does the work in its own context and returns just its summary, so the
details never enter the main session. In Claude Code you can also save your own
subagent types as files in `.claude/agents/`; ask the system to set one up if you want
a reusable one.

## Workflows
A workflow is several steps chained into one run. Your analysis from Weeks 5 and 8 is
already a sequence: load, clean, model, check assumptions, challenge the result. Once
that sequence is stable, you can have the system run it end to end, or write it as a
skill that performs the steps in order. The value is consistency: the validation steps
run as part of the pipeline instead of only when you remember them.

## Scheduled and background tasks
Long jobs can run in the background while you do other things, and recurring jobs can
run on a schedule (for example, re-running an analysis when the data file changes, or
overnight). These are worth knowing about for large work. Start small and confirm the
job does what you expect before you leave it running on its own.

## More automation, more validation
This is the part to take seriously. Automating the work does not automate the trust.
When a pipeline runs ten steps without stopping, it is easy to stop reading any of
them, and a system that is confidently wrong is now wrong ten times without a pause.
The fix is to build the checks into the automation, not to drop them:
- Keep the validation steps (tests, `/check-assumptions`, `/challenge-result`) inside
  the pipeline, so scaling the work scales the checking too.
- Use hooks to enforce the steps you cannot afford to skip.
- Keep a human approving the things that matter, and have the automation report what it
  did so you can read it.
- Use deterministic software as much possible. Don't have the LLM do the work. Have it  
  write software that will do the same thing the same way, every time. 

## Where automation fits in research
A rough rule. Automate the mechanical and the checking. Do not automate the judgment.
- Good to automate: cleaning, plotting, running tests, running the validation skills,
  backing up data, rerunning an analysis when inputs change.
- Keep under review: what a result means and whether to trust it, anything sent outside
  your machine, anything that deletes or overwrites data.
- For experiments specifically: automate the build, the tests, and data backups. Do not
  automate running a participant, or anything with a real-world consequence, without a
  person in the loop.

## Words you met this week
- hook: a command the tool runs automatically at a set point, every time, regardless of
  the model. Used to enforce a rule rather than only request it.
- subagent: a separate helper the main session starts for a focused task, with its own
  context.
- workflow: several steps chained into one run, such as clean, model, then validate.
- background task: a job that runs while you continue doing other things.
- scheduled task: a job set to run on a timer or when something changes, such as a
  nightly rerun.

Full running glossary: ../resources/glossary.md
