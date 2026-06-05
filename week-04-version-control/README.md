# Week 4 - Version Control

Goal for the week: learn git well enough to use it as a safety net. When the
system edits your files, git is what lets you see exactly what changed, keep what
works, and throw away what does not. This is the thing that makes it safe to let
an agent touch your project at all.

## 1. Why this matters more once an agent is involved

An agent can change many files in seconds. Without version control you cannot
tell what it changed, and you cannot get back to the version that worked. With it,
every change is visible and reversible. Git turns "I hope it did not break
anything" into "let me look at exactly what it did, then decide."

Git is also deterministic software - the same theme from Week 3. A commit is a
fixed checkpoint that behaves the same way forever. The probabilistic system
proposes changes; git gives you reliable, reproducible control over which ones you
actually keep.

## 2. The core ideas (concepts first, commands later)

You do not need every git command. You need five ideas:

- commit: a saved checkpoint of your project at a moment in time, with a short
  note about what changed.
- diff: what changed between two points - lines added and removed. You already
  met this in Week 2; now you save and compare those changes over time.
- branch: a parallel line of work, so you can try something risky without
  touching your known-good version.
- revert / undo: going back to an earlier checkpoint when a change was wrong.
- push / pull: sending your commits up to the shared repo (like the course repo),
  or pulling down updates others made.

## 3. Let the system run git and teach you

You learn git fastest by having the system do it while explaining. From inside a
project, try prompts like:

> "Show me the current git status and explain what it means. Then commit the
> current state with a clear message, and tell me what that commit did."

> "I am about to make a change. Commit first so we have a checkpoint, then make
> the change, then show me the diff so I can decide whether to keep it."

Ask it to write good commit messages and explain why they are written that way.
You are learning the concepts through real use, not memorizing commands.

## 4. Read the diff critically - this is the actual skill

Reviewing the diff before you commit is how you supervise an agent. Every time,
ask:

- Did it change only what I asked, or did it also touch things I did not mention?
- Did anything get deleted that I wanted to keep?
- Do I actually understand each change? If not, ask: "Explain this part of the
  diff and why you made it."

Accepting a diff you have not read is the same as trusting the system blindly -
the exact habit this course is built to replace.

## 5. Exercise: break it on purpose, then recover

This is the lesson that makes git stick.

1. Ask the system to commit your working project ("a known-good checkpoint").
2. Ask it to make a change that breaks something, on purpose.
3. Confirm it is broken - run it, see the failure.
4. Use git to revert to the checkpoint, and confirm it works again.

Once you have rescued yourself once, letting an agent make bold changes stops
being scary - you know you can always get back.

## A note for the experienced

If you are already comfortable here, this is a good week to move into Learning
mode (from Week 2) as your default, and to start writing your own commit messages
and resolving small conflicts yourself. Keep embedding the learning so the tool
makes you sharper, not rustier.

## Words you met this week

- commit: a saved checkpoint of the project, with a short note on what changed.
- branch: a parallel line of work you can experiment on safely.
- revert / undo: returning to an earlier checkpoint.
- push: sending your commits up to the shared repo.
- pull: bringing down commits others have added.
- merge: combining work from one branch into another.

Full running glossary: ../resources/glossary.md
