---
name: Challenge a result
description: Take a finding or statistical result and actively try to show it is wrong before trusting it. List the most likely ways it could be wrong (assumption violations, data problems like leakage or type coercion, multiple comparisons, alternative explanations, code errors, overfitting), check the ones that can be checked against the data and code, and report which threats survive. Use after producing a result and before reporting it.
allowed-tools: Read Grep Glob
argument-hint: [the result or claim to challenge]
---

# Challenge a result

Your job here is to try to break the result, not to defend it. Default to skepticism.
A result that survives a real attempt to refute it is worth more than one that was
never challenged.

## 1. State the claim precisely

Write the claim in one or two lines: the effect, its direction, its size, and the
data it was computed on. Vague claims hide errors.

## 2. List the ways it could be wrong

Go through these categories and name the specific threats that apply:

- Assumptions: are the method's assumptions met? If in doubt, run the
  `check-assumptions` skill.
- Data problems: leakage (information that would not be available in practice),
  silent type coercion, how missing data were handled, outliers, a wrong join or
  merge.
- Analysis choices: multiple comparisons without correction, choices that could be
  fishing for significance, the wrong model for the design, a wrong default left
  unchanged.
- Alternative explanations: a confound or a simpler account that would produce the
  same result.
- Code errors: does the code actually compute what the claim says it does? Read it.
- Generalization: would this hold on new data, or is it fit to this particular sample?

## 3. Check what can be checked

For each threat that can be tested against the data or code, check it and show the
output. Do not just speculate. If the data were generated from known values (as in
this course), check whether the analysis recovers those values.

## 4. State what cannot be checked

List the threats you could not rule out here, as honest caveats.

## 5. Verdict

Say which threats are ruled out, which survive, and whether the claim can be reported
as it stands, reported with caveats, or not yet. If it cannot be trusted yet, say so
plainly.
