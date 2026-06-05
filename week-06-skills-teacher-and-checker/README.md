# Week 6 - Skills: Teacher and Checker

Status: outline only - to be built out.

## Objectives
- Write CLAUDE.md / AGENTS.md instruction files and custom skills.
- Encode the questions students shouldn't have to memorize into skills.

## Skills built this week (collected in /skills)
- `/explain` - turns the agent into a tutor for the current repo: explain any
  file/function/architecture at a chosen depth, trace data flow, quiz the student.
- `/check-assumptions` - before reporting any statistical result, state the test's
  assumptions, check each against the data, flag violations, note better methods.

## The transferable idea
`/explain` makes the agent teach the student; `/check-assumptions` makes the agent
check itself. Both are just "questions encoded as a skill."

## To build later
- Reference implementations of both skills (downloadable)
- AGENTS.md / CLAUDE.md template
- "Write your own skill" exercise
