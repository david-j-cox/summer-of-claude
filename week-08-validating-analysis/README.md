# Week 8 - Validating Analysis

Goal for the week: this is where producing a result and trusting a result come apart.
The system will hand you an analysis that looks finished and reads convincingly. This
week is about not believing it until it has earned it. Everything so far has been
building toward this.

The work is to make the system question its own analysis, and to check the parts you
can check yourself. If you are building an experiment instead of analyzing data, there
is a section for you near the end; the same skepticism applies to a different target.

## The three questions

For any analysis, make the system answer these before you report anything:

1. What are this method's assumptions, and does the data meet each one?
2. Is there a more appropriate method, and why was this one chosen over it?
3. Where could this result be wrong: the data, the code, the choices?

The `/check-assumptions` skill from Week 6 is built for the first two. This week you
use it in depth, and add `/challenge-result` for the third.

## Validate the Week 5 analysis

Go back to the mixed-effects analysis you built in Week 5 and run `/check-assumptions`
on it. For this data and model, the checks that matter include:

- Independence: the rows are not independent. Sessions repeat within participants,
  participants within clinics. At the minute grain, the per-minute counts are
  autocorrelated by construction (see the data dictionary), so even the within-session
  observations are related. Does the model account for this, or does it assume
  independence it does not have?
- Distribution: at the interval grain the outcome is a count, not a continuous value.
  A model assuming normal residuals is the wrong family. Should this be a count model?
- Random-effects structure: are the grouping levels modeled, or collapsed away?
- Homogeneity and linearity, where the model assumes them.

Make the system check each against the actual data and show the diagnostic, not just
assert that it is fine.

## Recover the known answer

This dataset has an advantage real data never will: it was generated from known
values (the data dictionary lists them). So you can ask the strongest question there
is. Does the analysis recover the truth? Have the system compare its estimates to the
true intervention effect, session trend, severity effect, and the clinic and
participant variation.

If an analysis cannot recover a known answer on data where the truth is given, you
have no reason to trust it on real data where the truth is unknown. This is one of the
most useful checks you can run, and it is only possible because the data are
synthetic.

## The usual suspects

Whatever the analysis, watch for these. Ask the system about each by name:

- Hallucinated methods or citations: a named test or reference that does not exist or
  does not say what is claimed. Verify it.
- Data leakage: information used in the analysis that would not be available in
  practice, inflating the result.
- Silent type coercion: a column read as text, a category treated as a number, dates
  parsed wrong. These change results quietly.
- Wrong defaults: a function's default that does not fit your design, left unchanged.
- Multiple comparisons and fishing: many tests run, only the significant one reported,
  no correction applied.

## Challenge the result

Run the new `/challenge-result` skill. Where `/check-assumptions` works through a
checklist, this one takes the opposite stance: it tries to prove the result wrong. It
lists the most likely ways the finding could be false, checks the ones that can be
checked, and reports which threats survive.

Install it by copying the `challenge-result` folder into `.claude/skills/` (or
`~/.claude/skills/`), then run `/challenge-result`. Codex users: paste the steps from
`skills/challenge-result/SKILL.md` into a session. A result that survives an honest
attempt to break it is one you can start to trust.

## Reproducibility is part of validation

A result you cannot reproduce has not been validated, only observed once. Confirm the
analysis runs from a script, that any randomness is seeded, and that someone else
could run it and get the same numbers. If it only worked once in a live session, it is
not yet a result.

## If you are building an experiment

Validating an experiment is not about statistical assumptions. It is about whether the
study does what it claims and records what it should. The same skepticism, a different
target:

- Deliver the contingencies: feed the app a scripted sequence of responses and confirm
  reinforcement was delivered exactly as the schedule specifies. Do not eyeball it,
  check the log against the known sequence.
- Record faithfully: confirm every response and timestamp is saved, in the right
  format, with nothing dropped or double-counted.
- Hold up under stress: very fast responses, responses at boundaries, a session
  interrupted partway. Pilot it on yourself and on a simulated responder before any
  real participant.

The question is the same as for an analysis: how would you know if it were wrong?

## Would this survive peer review?

A final pass. Ask the system, and ask yourself: if a reviewer who wanted to reject
this read it closely, what would they catch first? Fix that before you report it. The
goal of this week is to be your own toughest reviewer, with the system doing the parts
it can.

## Words you met this week

- statistical assumption: a condition a method requires to give valid results, such as
  independence or a particular distribution.
- independence: the assumption that observations do not depend on each other; broken by
  repeated measures, nesting, and autocorrelation.
- multiple comparisons: running many tests, which inflates the chance of a false
  positive unless corrected.
- p-hacking: trying many analyses and reporting the one that reached significance, on
  purpose or by accident.
- data leakage: letting information into the analysis that would not be available in
  real use, making the result look better than it is.
- confound: an alternative cause that could explain the result instead of the one
  claimed.
- overfitting: a result fit so closely to one sample that it does not hold on new data.

Full running glossary: ../resources/glossary.md
