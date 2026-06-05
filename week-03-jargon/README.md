# Week 3 - Jargon

Goal for the week: learn the names of the things you have been using, and a few you
will use later. You have already cloned a repo, watched tool calls, read diffs, and
switched output styles. This week we slow down and describe how those pieces fit
together, so you can read documentation and online discussion without getting lost.
The vocabulary is also part of staying in control of the system and improving the
accuracy of its output.

## How the pieces fit together

Most of the terms describe one arrangement: a probabilistic part wrapped in
deterministic software.

- Model: the probabilistic part. It produces likely next words from patterns in its
  training. It is flexible, but on its own it is not reliable. Run the same prompt
  twice and you can get two different answers.
- Tools: deterministic software the model can call, such as read a file, run a
  command, or search. A tool does the same thing every time. This is the reliable
  part.
- Harness: the program that connects the model to the tools. Claude Code and Codex
  are harnesses. It supplies the model with context, runs the tools the model
  requests, shows you the diffs, and manages the loop. The harness is ordinary
  software.
- Agent: all of the above working together in the ask, act, review loop.

This is the central idea of the course. The more of your work you move into
deterministic software, such as a script, a test, or a skill the system writes for
you, the less your results depend on a probabilistic guess and the more they become
reproducible. The model proposes; the software is what you rely on.

## The rest of the vocabulary

What the model operates within:

- context: the information currently loaded for the system to use, including your
  prompts, the files it has read, and its earlier replies.
- context window: the limit on how much can be loaded at once. When it fills, older
  material is dropped or summarized, so a long session loses access to its earlier
  parts.

Ways to extend or customize the harness:

- skill: a saved set of instructions, sometimes with code, that has the system do a
  specific job the same way each time.
- slash command: a shortcut starting with "/" that runs a skill or a built-in
  action, such as `/config`.
- MCP (Model Context Protocol): a standard for connecting outside tools and data,
  such as a database, a web service, or your files, to the harness.
- hook: a command that runs automatically at a set point, such as before or after
  an edit, without you asking each time.
- subagent: a separate helper agent the main agent starts for a focused task, with
  its own context.
- output style: the format the system uses to respond, such as Explanatory or
  Learning.

You will not use all of these yet. MCP, hooks, and subagents return in Week 9. They
are listed here so the full landscape is visible.

## Exercise: match each term to something you did

For each term above, write one line naming where you already encountered it in Weeks
1 and 2, for example "output style, when I turned on Explanatory" or "tool call,
when it read my CSV." Any term you cannot place is one to ask the system about.

## Exercise: read real documentation

Open the official documentation for your tool, or a forum thread about it, and read
a few paragraphs. Mark the terms you are unsure of, then ask the system: "Explain
each of these in plain language, using this repo as the example."

## Practice and self-check

Have the system test your recall instead of only reading definitions: "Quiz me on
this week's vocabulary one term at a time, tell me whether I am right, and correct
me." Learning while you work is how you avoid deskilling, losing skills you had, and
neverskilling, never building them in the first place.

## Words you met this week

- harness: the software that connects the model to its tools and runs the loop;
  Claude Code and Codex are harnesses.
- context window: the limit on how much information can be loaded at once.
- MCP (Model Context Protocol): a standard for connecting outside tools and data to
  the harness.
- skill: a saved, repeatable job the system runs the same way each time.
- slash command: a "/" shortcut that runs a skill or a built-in action.
- subagent: a helper agent started for a focused task, with its own context.
- hook: a command that runs automatically at a set point.

Full running glossary: ../resources/glossary.md
