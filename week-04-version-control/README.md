# Week 4 - Version Control

Goal for the week: learn git well enough to use it as a safety net. When the system
edits your files, git is what lets you see exactly what changed, keep what works,
and discard what does not. It is what makes it reasonable to let an agent change
your project at all.

## Why version control matters with an agent

An agent can change many files in seconds. Without version control you cannot tell
what it changed, and you cannot return to the version that worked. With it, every
change is visible and reversible. Git replaces "I hope it did not break anything"
with "here is exactly what it did, and I decide what to keep."

Git is deterministic software, the same theme as Week 3. A commit is a fixed
checkpoint that behaves the same way every time. The GenAI model proposes changes;
git gives you reliable control over which of those changes you actually keep.

## The core ideas

You do not need every git command. Five ideas cover most of the work:

- commit: a saved checkpoint of your project at a point in time, with a short note
  about what changed.
- diff: what changed between two points, shown as lines added and removed. You met
  this in Week 2; now you save those changes and compare them over time.
- branch: a parallel line of work, so you can try something risky without changing
  your known-good version.
- revert / undo: returning to an earlier checkpoint when a change was wrong.
- push / pull: sending your commits up to the shared repo, or bringing down updates
  others made.

## Let the system run git and explain it

You learn git fastest by having the system run it and explain each step. From inside
a project, try prompts like:

> "Show me the current git status and explain what it means. Then commit the current
> state with a clear message, and tell me what that commit did."

> "I am about to make a change. Commit first so we have a checkpoint, then make the
> change, then show me the diff so I can decide whether to keep it."

Ask it to write the commit messages and explain why they are written the way they
are. You are learning the concepts through use, not memorizing commands.

## Reviewing a diff

Reading the diff before you commit is how you supervise an agent. Each time, ask:

- Did it change only what I asked, or did it also touch things I did not mention?
- Did anything get deleted that I wanted to keep?
- Do I understand each change? If not, ask: "Explain this part of the diff and why
  you made it."

Accepting a diff you have not read is the same as accepting the output without
checking it, which is the habit this course works to replace.

## Recovering from a bad change

A short exercise that shows why git is worth the effort:

1. Ask the system to commit your working project as a known-good checkpoint.
2. Ask it to make a change that breaks something on purpose.
3. Confirm it is broken by running it and seeing the failure.
4. Use git to revert to the checkpoint, and confirm it works again.

Once you have recovered from a broken state yourself, letting an agent make larger
changes carries less risk, because you can always return to a working version.

## If you are already comfortable with git

Use this week to move into Learning mode (from Week 2) as your default, write your
own commit messages, and resolve small merge conflicts yourself. Keep embedding the
learning so the tools make you sharper rather than rustier.

## Words you met this week

- commit: a saved checkpoint of the project, with a short note on what changed.
- branch: a parallel line of work you can experiment on without risk to the main
  version.
- revert / undo: returning to an earlier checkpoint.
- push: sending your commits up to the shared repo.
- pull: bringing down commits others have added.
- merge: combining work from one branch into another.

Full running glossary: ../resources/glossary.md
