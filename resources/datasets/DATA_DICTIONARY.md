# Data dictionary: behavior_sessions.csv

A synthetic dataset for the course. The numbers are made up, but the structure is
realistic: repeated sessions are nested within participants, and participants are
nested within clinics. That nesting is why a mixed-effects (multilevel) model fits
this data better than a single-level model that treats every row as independent.

Used in Weeks 5, 8, and 10. Regenerate any time with
`python3 generate_behavior_sessions.py` (standard library only, fixed seed, so the
file is identical each run).

## One row

One row is one session for one participant: 32 participants x 12 sessions = 384 rows.

## Columns

| column | type | description |
|--------|------|-------------|
| `clinic_id` | text | The clinic (C1 to C4). The highest grouping level. |
| `participant_id` | text | The participant (P01 to P32). Nested within a clinic. |
| `age` | integer | Participant age in years. A participant-level value (same across that participant's rows). |
| `baseline_severity` | integer | Rated severity at intake, 1 (low) to 10 (high). Participant-level. |
| `session` | integer | Session number, 1 to 12. The repeated-measures index. |
| `condition` | text | `baseline` for sessions 1 to 6, `intervention` for sessions 7 to 12. |
| `target_rate` | number | The outcome: target behavior rate in responses per minute. |

## How it was generated (the ground truth)

The outcome was built from a known model, so an analysis can be checked against
what actually produced the data. See `generate_behavior_sessions.py` for exact
values. In words:

- A baseline rate, plus a clinic-level offset, plus a participant-level offset.
- The intervention lowers the rate.
- A small decline across sessions, with each participant having their own slope.
- Higher baseline severity raises the rate; age has a very small effect.
- Observation-level noise on top.

Because the generating values are known, you can ask whether an analysis recovers
them: the intervention effect, the session trend, the severity effect, and the
clinic and participant variation. Weeks 8 returns to this in depth.
