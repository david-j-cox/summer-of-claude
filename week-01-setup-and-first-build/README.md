# Week 1 - Setup and First Build

Goal for the week: get a tool installed, talk to it, pull down the course files,
and make it do one tiny useful thing. Explore as much as you want past that.

## Open a terminal

The terminal is just a text window where you type commands to your computer. It
is also where these AI tools run. Open it once and leave it open.

- Mac: press Cmd+Space, type `Terminal`, press Enter.
- Windows: click Start, type `PowerShell`, press Enter.
- Linux: open your Terminal app (often Ctrl+Alt+T).

Everything below is typed into this window.

## Install a tool

I will be using Claude Code, but either is fine. Install one to get started, and
feel free to try the other too.

- Claude Code: https://docs.claude.com/en/docs/claude-code
- Codex CLI: https://developers.openai.com/codex/cli

You also need git (the tool used to share these files). Check whether you already
have it by typing `git --version`. If you see a version number, you are set. If
not:

- Mac: run `xcode-select --install`
- Windows: install from https://git-scm.com/download/win
- Linux: `sudo apt install git` (or your distro's package manager)

## Sign in

Launch the tool and follow the login prompt.

- Claude Code: run `claude`
- Codex: run `codex`

If it greets you and waits for your input, you are connected.

## See what it does and have it explain

You learn the most when you can see what the tool is doing and why. Do both of
these:

- Ask it directly, in plain English: "As you work, show me every command you run
  and its full output, explain each step, and tell me why you made each choice."
- Claude Code extras: run `/config` and set Output style to Explanatory (it adds
  the reasoning behind its choices). Press Ctrl+O at any time to open the full
  transcript and see every command and its complete output. (Codex: the plain-
  English request above works; run `codex --help` to see its output options.)

You can turn this up or down whenever you like.

## Get the course files

You could type git commands yourself, but a more useful first exercise is to let
the tool do it and teach you as it goes. Try something like:

> "Clone the course repo at https://github.com/david-j-cox/summer-of-claude.git
> into a folder for my coursework. Then walk me through what 'clone' just did,
> what git is, and the best practices I should follow while working in this
> folder."

Then keep poking: ask where the files went, how to get updates later, and what a
"commit" is. We go deeper on git in Week 4. Here you are just getting a feel for
asking the tool to do real things and explain them.

## Your first task

Ask the tool, in your own words, to do something small and real. For example:

> "Make a CSV with 10 rows of fake behavior analysis data, then write a short
> script that reads it and prints the average of each numeric column. Explain
> each step."

Watch what it does. Read its explanation. Ask it "why?" at least once.

## Checking the output

When it says "done" or "this works," ask yourself: how would I actually know?
Run it. Look at the output. Ask it about the assumptions it made. Ask where it
might have gotten things wrong, or how different assumptions would have changed
the results. Ask it to test and validate its work and to show you those steps.

This is the critical thinking skill set that will define future work.

## Words you met this week

- terminal (or PowerShell): the text window where you type commands to your
  computer; where these tools run.
- agent: an AI tool that can take actions for you, such as reading and writing
  files or running commands, not just replying with text.
- model: the generative AI system (such as Claude or GPT) that produces the
  responses and chooses which tools to call. The agent is the software built
  around the model.
- prompt: the instruction or question you type to the agent.
- context: the information currently loaded for the system to use in this session
  (your prompts, the files it has read, its earlier replies). The space is
  limited, so older material eventually drops out.
- clone: making your own local copy of a shared project so you can use it and
  pull updates later.
- repository (repo): a folder of project files tracked by git so changes can be
  shared and updated.

Full running glossary: ../resources/glossary.md
