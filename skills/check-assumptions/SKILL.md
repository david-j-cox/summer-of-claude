---
name: Check statistical assumptions
description: Before reporting or interpreting any statistical result, state the test or model's assumptions, check each one against the actual data, flag violations with evidence, and say whether a more appropriate method exists. Also separate numbers that were actually computed from anything asserted. Use whenever about to report a statistical analysis.
allowed-tools: Read Grep Glob
argument-hint: [analysis or result to check]
---

# Check statistical assumptions

Run this before presenting any statistical result as if it can be trusted. Work
through the steps and show the user each one. Do not skip to the conclusion.

## 1. Name the analysis and its assumptions

State plainly what test or model is being used and list its assumptions. Examples of
assumptions to consider, depending on the method:

- independence of observations (often violated by repeated measures, nesting, or
  time-series autocorrelation)
- the distribution the method assumes (for example, normal residuals for ordinary
  regression, or a count distribution for counts)
- equal variance / homogeneity across groups
- linearity, where assumed
- enough data per group or per parameter
- for multilevel models: whether the grouping structure is modeled correctly
- for multiple tests: whether correction for multiple comparisons is needed

## 2. Check each assumption against the actual data

For every assumption, do not just assert it. Check it:

- describe how it can be checked,
- run that check on the data (a plot, a diagnostic, a test), and
- show the output.

If running a check needs code, write it, run it, and show the result.

## 3. Report what holds and what does not

For each assumption, say clearly: holds, questionable, or violated, with the evidence
you just produced. Do not bury a violation.

## 4. If an assumption is violated, name a better method

When something is violated, say what a more appropriate method would be and why (for
example, a mixed-effects model for nested data, a count model for counts, or a method
that allows autocorrelation). Recommend it; do not quietly keep the wrong method.

## 5. Separate computed from asserted

Guard against reporting results that were never actually produced:

- For every number you report, show the code and the output that produced it.
- Do not state a statistic, p-value, or effect size you did not compute.
- If you are estimating or recalling rather than computing, say so explicitly.

## 6. Verdict

End with a short, honest summary: can this result be trusted as reported, does it
need a different method first, or does it need more checking. If it cannot be trusted
yet, say that plainly.
