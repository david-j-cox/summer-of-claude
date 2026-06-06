#!/bin/bash
# PreToolUse hook for Claude Code.
# Blocks any git commit made directly on the main or master branch, and tells the
# system to use a development or feature branch instead. Unlike a skill, this runs
# automatically and cannot be skipped: the commit is denied before it happens.
#
# Claude Code passes the tool-call details to this script as JSON on standard input.

command=$(jq -r '.tool_input.command // ""')

case "$command" in
  *"git commit"*)
    branch=$(git rev-parse --abbrev-ref HEAD 2>/dev/null)
    if [ "$branch" = "main" ] || [ "$branch" = "master" ]; then
      jq -n --arg b "$branch" '{
        hookSpecificOutput: {
          hookEventName: "PreToolUse",
          permissionDecision: "deny",
          permissionDecisionReason: ("Direct commits to \($b) are blocked. Create or switch to a development or feature branch, then commit there.")
        }
      }'
      exit 0
    fi
    ;;
esac

exit 0
