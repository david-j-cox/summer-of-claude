# Week 8 - Validating Analysis

Goal for the week: check whether an analysis can be trusted before you report it. The
system can produce an analysis that looks complete and is written clearly but is still
wrong. The work this week is to test it. You have the system question its own analysis,
and you check the parts you can check yourself. If you are building an experiment
rather than analyzing data, there is a section for that near the end.

## Three questions to answer first

Before reporting an analysis, get answers to three questions:

1. What are the method's assumptions, and does the data meet each one?
2. Is there a more appropriate method, and why was this one used instead?
3. Where could the result be wrong: in the data, the code, or the analytic choices?

The `/check-assumptions` skill from Week 6 covers the first two. For the third, this
week adds `/challenge-result`.

## Validate the Week 5 analysis

Open the mixed-effects analysis from Week 5 and run `/check-assumptions` on it. For
this model and dataset, the checks that matter most are:

- Independence. The rows are not independent. Sessions repeat within participants, and
  participants sit within clinics. At the minute grain, the per-minute counts are
  autocorrelated by construction (see the data dictionary). Check whether the model
  accounts for this rather than assuming an independence it does not have.
- Distribution. At the interval grain the outcome is a count, not a continuous
  measure, so a model that assumes normal residuals is using the wrong distribution.
  Ask whether a count model is more appropriate.
- Random-effects structure. Check that the grouping levels are actually in the model
  and not collapsed away.
- Homogeneity and linearity, where the model assumes them.

Have the system run each check against the data and show the diagnostic, not just
assert that everything is fine.

## Recover the known values

This dataset was generated from known values, listed in the data dictionary. That
lets you check whether the analysis recovers them. Have the system compare its
estimates against the true intervention effect, session trend, severity effect, and
the clinic and participant variation. Real data will not give you this; synthetic data
does, so use it while you can. If an analysis cannot recover values you already know,
there is little reason to trust it on data where the values are unknown.

## Common problems to check for

Ask the system about each of these by name, since it will not always raise them on its
own:

- Hallucinated methods or citations: a named test or reference that does not exist, or
  does not say what is claimed. Verify it.
- Data leakage: information used in the analysis that would not be available in
  practice, which inflates the result.
- Silent type coercion: a numeric column read as text, a category treated as a number,
  dates parsed incorrectly. These change results with no error message.
- Wrong defaults: a function default that does not match your design, left unchanged.
- Multiple comparisons: many tests run, only the significant one reported, no
  correction applied.

## Challenge the result

`/check-assumptions` works through a checklist. `/challenge-result`, added this week,
does the opposite. It tries to show the result is wrong: it lists the ways the finding
could be false, checks the ones that can be checked, and reports which problems remain.

Install it by copying the `challenge-result` folder into `.claude/skills/` (or
`~/.claude/skills/`), then run `/challenge-result`. Codex users: paste the steps from
`skills/challenge-result/SKILL.md` into a session.

## Reproducibility

Confirm the analysis runs from a script, that any randomness is seeded, and that
someone else could run it and get the same numbers. A result that worked once in a
live session, through steps you cannot repeat, has not been validated.

## If you are building an experiment

Validating an experiment is about whether it does what it claims and records what it
should, not about statistical assumptions. The targets are:

- Contingencies: feed the app a scripted sequence of responses and check the log to
  confirm reinforcement was delivered exactly as the schedule specifies, rather than
  judging it by eye.
- Recording: confirm every response and timestamp is saved, in the right format, with
  nothing dropped or double-counted.
- Stress conditions: very fast responses, responses at schedule boundaries, and a
  session interrupted partway through. Pilot it on yourself and on a simulated
  responder before running a participant.

## A peer-review check

As a last step, ask the system, and ask yourself, what a careful reviewer would
object to first. Address that before reporting. Most of this is work the system can do
once you tell it to.

## Words you met this week

- statistical assumption: a condition a method requires to give valid results, such as
  independence or a particular distribution.
- independence: the assumption that observations do not depend on each other. Broken by
  repeated measures, nesting, and autocorrelation.
- multiple comparisons: running many tests at once, which raises the chance of a false
  positive unless it is corrected for.
- p-hacking: trying many analyses and reporting the one that reached significance,
  whether on purpose or by accident.
- data leakage: letting information into an analysis that would not be available in
  real use, which makes the result look better than it is.
- confound: an alternative cause that could explain a result instead of the one being
  claimed.
- overfitting: a result fit so closely to one sample that it does not hold on new data.

Full running glossary: ../resources/glossary.md
