# Glossary

A running list of the jargon, in plain language. It grows every week - terms are
grouped by the week they first show up, so you can always find where one was
introduced. Week 3 is a dedicated pass back over all of it.

## Week 1 - Setup and First Build

- terminal (or PowerShell): the text window where you type commands to your
  computer; where these tools run.
- agent: an AI tool that can take actions for you - read and write files, run
  commands - not just reply with text.
- model: the underlying AI "brain" (such as Claude or GPT) that does the
  thinking. The agent is the tool built around the model.
- prompt: what you type to the agent - your instruction or question.
- context: everything the agent is currently aware of in this session (your
  prompts, files it has read, its earlier replies). It has limited room, so it
  cannot remember everything forever.
- clone: making your own local copy of a shared project so you can use it and
  pull updates later.
- repository (repo): a folder of project files tracked by git so changes can be
  shared and updated.

## Week 2 - Driving the Loop

- tool: a specific action the agent is allowed to take - reading a file, editing
  a file, running a command, searching the web. The model decides which to use.
- tool call: one use of a tool. When you watch the agent work, the steps scroll-
  ing by ("Read", "Edit", "Bash") are its tool calls.
- diff: a before-and-after view of a file showing exactly what changed - lines
  added and removed. How you review an edit before accepting it.
- output style: a setting that changes how the agent talks to you. Explanatory
  narrates its reasoning; Learning leaves pieces for you to write.
- iterate / iteration: one round of the back-and-forth - you ask, it acts, you
  review and correct, repeat. Most real work is many iterations, not one prompt.
- session: one continuous conversation with the agent, from launch until you
  close it or clear it. Its context lives inside the session.

## Week 3 - Jargon

The mental model that ties these together: a probabilistic model wrapped in
deterministic software. The model guesses; the software (tools, harness, the
scripts you have it write) is what behaves the same every time and can be trusted.

- harness: the program that wraps the model and the tools together and runs the
  ask -> act -> review loop. Claude Code and Codex are harnesses. It is ordinary,
  deterministic software.
- context window: the size limit on what the model can hold in mind at once. When
  it fills up, older material is dropped or summarized - why long sessions "forget."
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
