# Example hook: block commits to main

A hook is a command Claude Code runs automatically at a set point. Unlike a skill,
which is an instruction the system may or may not follow, a hook runs every time and
can stop an action before it happens. This makes hooks the right tool for a guardrail
that must always hold.

`block-commit-to-main.sh` is a `PreToolUse` hook. Before any shell command runs, it
checks whether the command is a `git commit` on the `main` or `master` branch, and if
so it denies it and tells the system to use a development or feature branch. This is
the enforced version of the branch rule from Week 4: the `git-workflow` skill asks for
it, this hook requires it.

## Install (Claude Code)

1. Copy `block-commit-to-main.sh` into your project at
   `.claude/hooks/block-commit-to-main.sh` and make it executable:
   `chmod +x .claude/hooks/block-commit-to-main.sh`.
2. Add this to your project's `.claude/settings.json` (create the file if it does not
   exist):

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "command",
            "command": "${CLAUDE_PROJECT_DIR}/.claude/hooks/block-commit-to-main.sh"
          }
        ]
      }
    ]
  }
}
```

3. It needs `jq` installed (a small command-line JSON tool). Check with `jq --version`;
   install with `brew install jq` on Mac or your package manager on Linux/Windows.
4. Start a new session and try to commit on `main`. The commit should be denied.

Codex does not use this hook format. For Codex, keep the rule in `AGENTS.md` as an
instruction, which is followed but not enforced.

## A note on what hooks can do

This is one small example. Hooks can also run a linter (a tool that automatically
checks code for errors and style problems) or your tests after each edit, log every
command, or warn before risky actions. The pattern is the same: pick the
event, match the tool, and run a command. Use hooks for the few things that must
happen every time, and keep everything else as skills and instructions.
