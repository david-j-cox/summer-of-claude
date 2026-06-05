# Week 7 - Testing

Goal for the week: learn to test code, especially code you did not write. A test is
how you check, automatically and repeatedly, that code does what you think it does.
When the system writes the code, testing is most of how you earn the right to trust
it.

## What a test is

A test is code that runs your code on a known input and checks that the output is what
it should be. It either passes or fails. Like git, a test is deterministic: it runs
the same way every time and gives you a clear answer, which is exactly what you want
sitting underneath a system whose output varies.

A small example in words: "given a column of values `[2, 4, 6]`, the mean function
should return `4`." A test states that expectation in code and checks it.

## What to test in data work

You are not testing a web app. You are testing analysis code. The useful targets:

- Cleaning and transformation functions: a known input should give a known output.
- Edge cases: missing values, empty groups, a participant with one session, an
  impossible value, duplicates. These are where quiet errors hide.
- Properties you can state: for this course's dataset, the data were generated from
  known values (see the data dictionary), so you can test that an analysis recovers
  the intervention effect within a tolerance. That is a real, meaningful test of an
  analysis, not just of a helper function.

## The trap: plausible code and plausible tests

Here is the problem unique to working this way. The system can write code that looks
right, and then write tests that also look right and pass, while both share the same
mistake. The test does not catch the bug because the test was written to match the
code, not to match what the code should do. The result is a green checkmark on top of
a wrong answer.

Two habits avoid this:

- Decide the expected behavior yourself, first. Say what the correct output is before
  any code exists, so the test measures the code against your expectation, not against
  itself.
- Make tests fail on purpose. A test that cannot fail proves nothing. Break the code
  briefly, or feed a wrong expected value, and confirm the test actually goes red. If
  it does not, the test is not testing anything.

## Test-first, with the system

The reliable order is to write the test before the code. There is a skill for this:
`skills/test-first/`. It has the system state the expected behavior, get your
confirmation, write a test, run it and show it failing for the right reason, then write
the code until it passes, including an edge case.

Install it by copying the `test-first` folder into `.claude/skills/` (or
`~/.claude/skills/`), then run `/test-first`. Codex users: paste the steps from
`skills/test-first/SKILL.md` into a session. A prompt to start:

> "Using a test-first approach: I want a function that takes the session data and
> returns the mean target rate per condition. State the expected output for a small
> example first, write the test, show it failing, then implement it."

## Reading code you did not write

You cannot judge a test you cannot read. This is the week to slow down and read both
the code and its tests. Use `/explain` from Week 6 on anything unclear: "Explain what
this test checks, and what would make it fail." If you cannot say what a test would
catch, it is not yet doing its job for you.

## Exercise: plant a bug

This shows whether your tests are real.

1. Have the system write a cleaning or summary function and tests for it, test-first.
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
