# Week 5 - First Domain Project
Goal for the week: take a dataset from a raw file to a result you trust, working
with the system the whole way. This is a first end-to-end demo of a real project. 
The skills are breaking a goal into steps, building each step with the system, 
and checking the result instead of assuming it is right.

## The dataset
This week uses `resources/datasets/behavior_sessions.csv`. Read
`resources/datasets/DATA_DICTIONARY.md` first. Each row is one session for one
participant. The structure is nested: sessions repeat within participants, and
participants sit within clinics. That nesting is important for the analysis, 
analytically and mathematically. 

There is also a finer-grained file, `resources/datasets/behavior_intervals.csv`,
with one row per minute within each session. It adds a fourth level (minute within
session within participant within clinic) and a within-session time series: the
per-minute counts are related from one minute to the next. Start with the
session-level file. If you want a harder version, or once you reach Week 8, switch to
the interval file, where the extra level and the within-minute relationship give more
to model and more assumptions to check.

Point the system at the file and have it describe what is there before doing
anything else (i.e., ask it to conduct exploratory data analysis):

> "Load resources/datasets/behavior_sessions.csv, show me the first rows, the column
> types, how many participants and clinics there are, and anything that looks off.
> Do not analyze it in depth yet. We are simply interested in what is here and exploratory 
> data analysis."

## Break the project into steps
Do not ask for the whole analysis in one prompt. A vague "analyze this data" gives a
vague result that is hard to check. Work in steps you can review one at a time:
1. Load and inspect the data.
2. Clean and validate it: types, missing values, impossible values, duplicates.
3. Explore it with summaries and plots.
4. Choose and fit a model.
5. Interpret the result and check it.

Run one step, read what came back, then move to the next. You can also ask the
system to propose the steps, then you decide the order.

## When to let it run, and when to step in
Let the system handle the mechanical parts: loading, reshaping, making plots,
writing boilerplate. Step in for the decisions: what counts as an impossible value,
which model is appropriate, what the result means. The system can suggest these, but
you own them. When it makes a choice for you, have it say so and explain why.

The systems can also hallucinate results and findings. How will you know if it 
has done that with your results?

## Choosing a model that fits the structure
The data are nested, so a model that treats every row as independent would be wrong:
the 12 sessions from one participant are not 12 independent observations. A
mixed-effects model (also called a multilevel or hierarchical model) handles this. It
separates effects that apply to everyone (fixed effects, such as the average
intervention effect) from variation that differs by group (random effects, such as
each participant and clinic having their own level).

You do not need to know how to write the code to build a hierarchical model. Ask the 
system to do it for you, and have it explain what it does and why:

> "These data are nested: sessions within participants within clinics. Recommend an
> appropriate model, explain why it fits this structure better than a simple
> regression, and write the code to fit it. Use R with lme4 or Python with
> statsmodels, whichever you prefer, and explain the formula."

## Make the result reproducible
A result you cannot reproduce is not a result. Have the system put the analysis in a
script rather than running loose commands, and set a seed anywhere randomness is
involved, so the analysis returns the same numbers every run. This is the
deterministic-software point from Week 3. The script runs the same each time, even
though the system that wrote it does not.

## Check the result
Before you believe the output, check it. This week, start with the basics:
- Does the direction make sense? Here the intervention should lower the rate.
- Do the numbers match what a plot of the data shows?
- Ask the system: "What did you assume in this analysis, and where could it be
  wrong?"

Because this dataset was generated from a known model (see the data dictionary), you
can go further and ask whether the analysis recovers the values that produced the
data. Week 8 is devoted to this kind of checking, including the assumptions behind
the model. For now the habit is simple: produce a result, then try to find out if it
is wrong.

## Words you met this week
- nested (multilevel / hierarchical) data: observations grouped within larger units,
  such as sessions within participants within clinics.
- mixed-effects model (multilevel model): a model for nested data that includes both
  fixed effects and random effects.
- fixed effect: an effect estimated as the same across the sample, such as the
  average intervention effect.
- random effect: variation allowed to differ by group, such as each participant
  having their own level or trend.
- seed: a fixed starting value for random number generation, so a procedure gives
  the same result every run.

Full running glossary: ../resources/glossary.md
