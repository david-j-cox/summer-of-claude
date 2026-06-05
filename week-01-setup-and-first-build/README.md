# Week 1 - Setup and First Build

Goal for the week: get the tool installed, talk to it, pull down the course
files with git, and make it do one tiny useful thing. That's it. You are
learning to drive, not to build yet.

## 1. Install a tool (pick one)

Most of us will use Claude Code, but either is fine. Install one to start.

- Claude Code: https://docs.claude.com/en/docs/claude-code
- Codex CLI: https://developers.openai.com/codex/cli

You also need git (the tool we use to share files). Check if you have it:
`git --version`. If not, install from https://git-scm.com or, on Mac, run
`xcode-select --install`.

## 2. Sign in

Launch the tool in your terminal and follow the login prompt.

- Claude Code: run `claude`
- Codex: run `codex`

If it greets you and waits for input, you are connected.

## 3. Get the course files

Pick a folder for your work, then clone the course repo:

```
git clone https://github.com/david-j-cox/summer-of-claude.git
cd summer-of-claude
```

You now have every week's materials on your machine. Each week lives in its
own folder. We will learn what git is really doing in Week 4 - for now, "clone"
just means "download a copy you can update later with `git pull`."

## 4. Start the tool inside the folder, and turn on learning mode

From inside `summer-of-claude`, start the tool so it can see the files.

If you have never coded: turn on a teaching mode so the tool explains itself.

- Claude Code: run `/config`, set Output style to Explanatory.
- Codex (or either tool): just ask in plain English, e.g. "Explain everything
  you do as you go, and don't make me write code yet."

## 5. Your first build

Ask the tool, in your own words, to do something small and real. For example:

> "Make a CSV with 10 rows of fake survey data, then write a short script that
> reads it and prints the average of each numeric column. Explain each step."

Watch what it does. Read its explanation. Ask it "why?" at least once.

## The trust habit (starts now)

When it says "done" or "this works," ask yourself: how would I actually know?
Run it. Look at the output. We build this reflex every week.

## Words you met this week
agent, model, prompt, context, clone
