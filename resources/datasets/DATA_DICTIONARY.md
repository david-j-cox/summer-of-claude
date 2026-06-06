# Data dictionary: behavior datasets

Two synthetic files for the course, both generated from the same model by
`generate_behavior_sessions.py` (standard library only, fixed seed, so the files
are identical each run). The numbers are made up, but the structure is realistic.

The data have four nested levels:

    minute  ->  session  ->  participant  ->  clinic

Responses are counted in one-minute intervals within a session, sessions repeat
within a participant, and participants sit within a clinic. This nesting is why a
mixed-effects (multilevel) model fits better than a single-level model that treats
every row as independent. Within a session the per-minute counts also form a short
time series with autocorrelation (one minute is related to the next), so successive
minutes are not independent either.

Used in Weeks 5 and 8. Regenerate any time with
`python3 generate_behavior_sessions.py`.

## behavior_intervals.csv (finest grain: one row per minute)

3,840 rows: 32 participants x 12 sessions x 10 minutes.

| column | type | description |
|--------|------|-------------|
| `clinic_id` | text | The clinic (C1 to C4). The highest grouping level. |
| `participant_id` | text | The participant (P01 to P32). Nested within a clinic. |
| `age` | integer | Participant age in years. Participant-level (constant per participant). |
| `baseline_severity` | integer | Rated severity at intake, 1 (low) to 10 (high). Participant-level. |
| `session` | integer | Session number, 1 to 12. |
| `condition` | text | `baseline` for sessions 1 to 6, `intervention` for sessions 7 to 12. |
| `minute` | integer | One-minute interval within the session, 1 to 10. The within-session time index. |
| `responses` | integer | Count of target responses in that minute (a count, not a rate). |

## behavior_sessions.csv (one row per session)

384 rows: the per-minute counts aggregated to a session. Same schema as the simpler
version used earlier in the course.

| column | type | description |
|--------|------|-------------|
| `clinic_id` | text | The clinic (C1 to C4). |
| `participant_id` | text | The participant (P01 to P32). |
| `age` | integer | Participant age in years. |
| `baseline_severity` | integer | Rated severity at intake, 1 to 10. |
| `session` | integer | Session number, 1 to 12. |
| `condition` | text | `baseline` or `intervention`. |
| `target_rate` | number | Mean responses per minute for the session (total responses divided by 10). |

## How it was generated (the ground truth)

See `generate_behavior_sessions.py` for exact values. In words:

- A baseline per-minute rate, plus a clinic-level offset, plus a participant-level
  offset.
- The intervention lowers the rate.
- A small decline across sessions, with each participant having their own slope.
- Higher baseline severity raises the rate; age has a very small effect.
- Within a session: under intervention the rate declines minute to minute (an
  extinction-like pattern); under baseline it stays roughly flat. Each participant
  has their own within-session slope.
- The minute-to-minute values carry AR(1) autocorrelation, so one minute is related
  to the previous one.
- Per-minute counts are drawn from a Poisson distribution around the expected rate.

Because the generating values are known, you can ask whether an analysis recovers
them: the intervention effect, the session trend, the within-session decline, the
severity effect, and the clinic and participant variation. Week 8 returns to this in
depth, including whether the model's assumptions (independence, the count
distribution, and so on) actually hold.
