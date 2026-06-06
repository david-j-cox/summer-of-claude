# Week 7 - Testing
Goal for the week: learn to test code, especially code you did not write. A test is
how you check, automatically and repeatedly, that code does what you think it does.

## What a test is
A test is code that runs your code on a known input and checks that the output is what
it should be. It either passes or fails. Like git, a test is deterministic. It runs
the same way every time and gives you a yes-no answer, which is what you want
for a system whose output can vary probabilistically.

For example, in words, a test might be something like: "given a column of values 
`[2, 4, 6]`, the mean function should return `4`." A test states that expectation in code and checks it.

## What to test
The same idea applies whether you are analyzing data or building an experiment. 
Test the pieces whose correct behavior you can state in advance. 

If you are analyzing data, useful targets might be:
- Cleaning and transformation functions: a known input should give a known output.
- Edge cases: missing values, empty groups, a participant with one session, an
  impossible value, duplicates. 
- Properties you can state: for this course's dataset, the data were generated from
  known values (see the data dictionary), so you can test that an analysis recovers
  the intervention effect within a tolerable error window. 

If you are building an experiment, useful targets might be:
- The contingency logic: reinforcement is delivered as scheduled. For example, an
  FR-5 should reinforce exactly every fifth response, not the fourth or sixth, and
  an interval schedule should time correctly.
- Trial and session flow: trials advance in the right order, the session starts and
  ends on the right conditions, and the inter-trial interval is presented as specified.
- Data recording: every response and its timestamp is logged, in the right format,
  with nothing dropped or double-counted. A study is only as good as the data it saves.
- Edge cases: very fast or double responses, a response right at a schedule boundary,
  a participant who does nothing, and a session interrupted partway through.

## The trap: plausible code and plausible tests
One known problem with LLMs and AI-coding systems (and humans, too) is that they can write code that looks right and write tests that also look right and pass, even though both share the same mistake. The test does not catch the bug because the test was written to match the code, not to match what the code should do. The result is a green checkmark on top of a wrong answer.

Two things to do to avoid this:
- Decide the expected behavior yourself, first. Tell the system what the correct output is before any code exists. That way the test measures the code against the expected output expectation, not against itself.
- Make tests fail on purpose. A test that can't fail proves nothing. Break the code
  briefly, or feed a wrong expected value, and confirm the test actually goes red. If
  it does not, the test is not testing anything.

## Test-first, with the system
The reliable order is to write the test before the code. There is a skill for this:
`skills/test-first/`. It has the system state the expected behavior, get your
confirmation, write a test, run it and show it failing for the right reason, then write
the code until it passes, including an edge case.

Install this skill by copying the `test-first` folder into `.claude/skills/` (or
`~/.claude/skills/`), then run `/test-first`. Codex users: paste the steps from
`skills/test-first/SKILL.md` into a session. Here's a prompt to start:

> "Using a test-first approach: I want a function that takes the session data and
> returns the mean target rate per condition. State the expected output for a small
> example first, write the test, show it failing, then implement it."

Or, for an experiment:
> "Using a test-first approach: I am building an FR-5 reinforcement schedule. State
> the expected behavior (reinforce on exactly every fifth response), write a test with
> a normal case and an edge case, show it failing, then implement it."

## Reading code you did not write
It;s difficult to judge a test you cannot read. This is the week to slow down and read the code and its tests. Use `/explain` from Week 6 on anything unclear: "Explain what
this test checks, and what would make it fail." If you cannot say what a test would
catch, it is not yet doing its job for you.

NB: The reality is that knowledge work is increasingly being done in code and code is
increasingly knowledge work. Learning how to read and investigate code will be an
important skill giving advantage to people who can do it. 

## Exercise: plant a bug
This shows whether your tests are real.
1. Have the system write a small function and the tests for that function using a 
   test-first approach. Use a data summary if you are analyzing data, or a piece of your 
   experiment such as a schedule if you are building one.
2. Confirm the tests pass.
3. Now change the function so it is wrong on purpose (for example, drop the last row,
   or divide by the wrong count).
4. Run the tests. Did they catch it? If yes, your tests have value. If no, the tests
   were checking the wrong thing, so fix them and try again.

## Words you met this week
- test: code that runs your code on a known input and checks the output is correct.
- unit test: a test of one small piece, such as a single function.
- assertion: the line in a test that states what must be true (for example, the result
  equals 4); the test fails if it is not.
- edge case: an unusual or boundary input where errors often hide, such as missing
  values or an empty group.
- test-driven development (TDD): writing the test before the code, so the code is built
  to meet a stated expectation.
- regression test: a test kept around to confirm a thing that once worked still works
  after later changes.

Full running glossary: ../resources/glossary.md
