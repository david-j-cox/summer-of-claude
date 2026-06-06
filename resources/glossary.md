# Glossary

Plain-language definitions of the jargon used across the course, in alphabetical
order. One idea ties much of it together: a probabilistic generative AI model wrapped
in deterministic software. The model predicts likely text; the software (tools, the
harness, and the scripts you have it write) does the same thing every run and can be
relied on.

- agent: an AI tool that can take actions for you, such as reading and writing files
  or running commands, not just replying with text.
- always-on vs on-demand: instruction files apply every session (always in context,
  so keep them short); skills load only when used. Short rules go in the instruction
  file, multi-step procedures go in a skill.
- assertion: the line in a test that states what must be true (for example, the result
  equals 4); the test fails if it is not.
- autocorrelation: when values in a series are related to nearby values (one minute
  predicts the next). It breaks the assumption that observations are independent.
- background task: a job that runs while you continue doing other things.
- branch: a parallel line of work, so you can try something risky without touching
  your known-good version.
- clone: making your own local copy of a shared project so you can use it and pull
  updates later.
- commit: a saved checkpoint of your project at a moment in time, with a short note
  about what changed.
- confound: an alternative cause that could explain a result instead of the one being
  claimed.
- context: the information currently loaded for the system to use in this session
  (your prompts, the files it has read, its earlier replies). The space is limited, so
  older material eventually drops out.
- context window: the limit on how much can be loaded at once. When it fills, older
  material is dropped or summarized, so a long session loses access to earlier parts.
- data leakage: letting information into an analysis that would not be available in
  real use, which makes the result look better than it really is.
- development / feature branch: a branch where you make and test changes before merging
  them into main. Use `development` for general work or `feature/<name>` for one
  specific change.
- diff: a before-and-after view of a file showing exactly what changed, with lines
  added and removed. How you review an edit before accepting it.
- edge case: an unusual or boundary input where errors often hide, such as missing
  values, an empty group, or a single observation.
- fixed effect: an effect estimated as the same across the whole sample, such as the
  average intervention effect.
- harness: the program that wraps the model and the tools together and runs the ask,
  act, review loop. Claude Code and Codex are harnesses. It is ordinary, deterministic
  software.
- hook: a command the tool runs automatically at a set point, every time, regardless
  of the model. Used to enforce a rule rather than only request it (a skill or
  instruction requests; a hook enforces).
- independence: the assumption that observations do not depend on each other. Broken by
  repeated measures, nesting, and autocorrelation.
- instruction file (`CLAUDE.md`, `AGENTS.md`): a file of standing rules the system loads
  every session. Claude Code reads `CLAUDE.md`; Codex reads `AGENTS.md`. A `CLAUDE.md`
  can import an `AGENTS.md` (with `@AGENTS.md`) so both tools share one set of rules.
- iterate / iteration: one round of the back-and-forth: you ask, it acts, you review and
  correct, then repeat. Most real work is many iterations, not one prompt.
- linter: a tool that automatically checks code for errors and style problems, so they
  are caught early rather than at run time.
- main branch: the stable version of the project that always works. You do not edit it
  directly; changes are made on another branch and merged in once they work.
- MCP (Model Context Protocol): a standard way to plug outside tools and data sources (a
  database, a web service, your files) into the harness.
- merge: combining the work from one branch into another.
- mixed-effects model (multilevel model): a model for nested data that includes both
  fixed effects and random effects, so it respects the grouping.
- model: the generative AI system (such as Claude or GPT) that produces the responses
  and chooses which tools to call. The agent is the software built around the model.
- multiple comparisons: running many tests at once, which inflates the chance of a false
  positive unless it is corrected for.
- nested (multilevel / hierarchical) data: observations grouped within larger units,
  such as sessions within participants within clinics. The grouping means the rows are
  not all independent of each other.
- output style: a setting that changes how the agent talks to you. Explanatory narrates
  its reasoning; Learning leaves pieces for you to write.
- overfitting: a result fit so closely to one sample that it does not hold on new data.
- p-hacking: trying many analyses and reporting the one that reached significance,
  whether on purpose or by accident.
- prompt: the instruction or question you type to the agent.
- pull: bringing down commits others have added.
- push: sending your commits up to the shared repo (like the course repo).
- random effect: variation allowed to differ by group, such as each participant or
  clinic having its own level or trend.
- regression test: a test kept around to confirm that something which once worked still
  works after later changes.
- repository (repo): a folder of project files tracked by git so changes can be shared
  and updated.
- reproducible: an analysis gives the same result when run again, because it is written
  down as a script and any randomness is pinned with a seed.
- residual: the difference between an observed value and the value the model predicts
  for it. Many methods make assumptions about the residuals (for example, that they are
  normally distributed).
- revert / undo: going back to an earlier checkpoint when a change was wrong.
- scheduled task: a job set to run on a timer or when something changes, such as a
  nightly rerun or a rerun when the data file is updated.
- seed: a fixed starting value for random number generation, so a procedure that uses
  randomness gives the same result every run.
- session: one continuous conversation with the agent, from launch until you close it or
  clear it. Its context lives inside the session.
- skill: a saved set of instructions (sometimes with code) that teaches the system to do
  a specific job the same way every time, on demand.
- slash command: a shortcut starting with "/" that triggers a skill or a built-in action
  (such as `/config`).
- statistical assumption: a condition a method requires to give valid results, such as
  independence of observations or a particular distribution.
- steering: redirecting the system while it works, telling it to change course, stop, or
  try something different mid-task, rather than only at the start.
- subagent: a separate helper agent the main agent can start for a focused task, with
  its own context.
- terminal (or PowerShell): the text window where you type commands to your computer;
  where these tools run.
- test: code that runs your code on a known input and checks the output is correct. It
  passes or fails, and runs the same way every time.
- test-driven development (TDD): writing the test before the code, so the code is built
  to meet a stated expectation rather than the test being fit to existing code.
- time series: measurements taken in order over time, such as per-minute response counts
  within a session.
- tool: a specific action the agent is allowed to take, such as reading a file, editing
  a file, running a command, or searching the web. The model selects which to use.
- tool call: one use of a tool. When you watch the agent work, the steps scrolling by
  ("Read", "Edit", "Bash") are its tool calls.
- unit test: a test of one small piece, such as a single function.
- workflow: several steps chained into one run, such as clean, model, then validate. The
  value is that the checks run as part of the pipeline, not only when remembered.
