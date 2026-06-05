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
