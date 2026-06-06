# Shared Resources

Cross-week references, datasets, and supplemental reading.

## Available now
- `glossary.md`: plain-language definitions of all the jargon used across the course,
  in alphabetical order.
- `datasets/behavior_sessions.csv` and `datasets/behavior_intervals.csv`: synthetic
  multilevel behavioral data used in Weeks 5 and 8. The sessions file has one
  row per session; the intervals file has one row per minute and adds a within-
  session time series. See `datasets/DATA_DICTIONARY.md` for columns and structure,
  and `datasets/generate_behavior_sessions.py` to regenerate both (standard library
  only, fixed seed).

- `templates/AGENTS.md` and `templates/CLAUDE.md`: project instruction file templates
  (Week 6). `CLAUDE.md` imports `AGENTS.md` so both tools share one set of rules.
- `templates/hooks/`: a working example hook that blocks commits to `main` (Week 9),
  with install instructions.

## To collect
- Official docs links (Claude Code, Codex)
- Recommended reading on reproducibility and statistical assumptions
