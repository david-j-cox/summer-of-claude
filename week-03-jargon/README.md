# Week 3 - Jargon

Goal for the week: put names to the things you have already been using. You have
cloned a repo, watched tool calls, read diffs, and switched output styles. Now we
slow down and build a mental model of how the pieces fit, so you can read docs and
online discussion without drowning. Knowing the vocabulary is also how you stay in
control of the system instead of being mystified by it.

## 1. The one mental model that makes the rest click

Almost every term fits into one picture: a probabilistic part wrapped in
deterministic software.

- The model is the probabilistic part. It guesses likely next words. It is
  flexible and creative, but on its own it is not reliable - run it twice and you
  can get two different answers.
- The tools are deterministic software - read a file, run a command, search.
  These behave the same way every time. This is the reliable part.
- The harness is the program that wraps the model and the tools together (Claude
  Code and Codex are harnesses). It feeds the model context, lets it call tools,
  shows you diffs, and runs the loop. The harness is ordinary software too.
- The agent is all of that working together in the ask -> act -> review loop.

The payoff, and the theme of the whole course: the more of your work you push into
deterministic software (have the system write you a script, a test, a skill), the
more your results stop being probabilistic guesses and start being reproducible
and trustworthy. The model is the assistant; software is what you actually rely on.

## 2. The rest of the vocabulary, grouped

Things the model works within:
- context: everything the system is currently aware of (your prompts, files it
  read, its replies).
- context window: the size limit on that awareness. When it fills, older material
  gets dropped or summarized - which is why long sessions start to "forget."

Ways you extend or customize the harness:
- skill: a saved set of instructions (sometimes with code) that teaches the system
  to do a specific job the same way every time.
- slash command: a shortcut starting with "/" that triggers a skill or built-in
  action (like `/config`).
- MCP (Model Context Protocol): a standard way to plug outside tools and data (a
  database, a web service, your files) into the harness.
- hook: a command set to run automatically at certain moments (before or after an
  edit, say), so something happens without you asking each time.
- subagent: a separate helper agent the main one can spin up for a focused task,
  with its own context.
- output style: how the system talks to you (Explanatory, Learning).

## 3. Exercise: match the word to what you already did

For each term above, write one line: where did you already run into this in Weeks
1 and 2? ("I switched output style when I turned on Explanatory." "I watched tool
calls when it read my CSV.") Anything you cannot place is exactly what to ask the
system about next.

## 4. Exercise: read something real and survive it

Open the official docs for your tool, or a forum thread about it, and read a few
paragraphs. Mark every term you are unsure of. Then paste them to the system:
"Explain each of these in plain language, using this repo as the example." Reading
past jargon is a skill, and it is one you will need well beyond this course.

## 5. Embed the learning

Do not just collect definitions - make the system check that they stuck. Try:
"Quiz me on this week's vocabulary one term at a time, tell me if I am right or
wrong, and correct me." Building the habit of learning while you work is how you
avoid deskilling (losing skills you had) and neverskilling (never building them in
the first place).

## Words you met this week

- harness: the software that wraps the model and tools and runs the loop; Claude
  Code and Codex are harnesses.
- context window: the size limit on what the system can hold in mind at once.
- MCP (Model Context Protocol): a standard for plugging outside tools and data
  into the harness.
- skill: a saved, repeatable job you teach the system to do the same way each time.
- slash command: a "/"-shortcut that triggers a skill or built-in action.
- subagent: a helper agent spun up for a focused task, with its own context.
- hook: a command that runs automatically at a set moment.

Full running glossary: ../resources/glossary.md
