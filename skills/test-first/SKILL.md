---
name: Test-first implementation
description: When implementing or changing a function, write a test for the expected behavior first, run it and show it failing for the right reason, then write the code until it passes. Cover at least one normal case and one edge case. Use when adding or changing code whose output can be checked.
argument-hint: [function or behavior to build]
---

# Test-first implementation

Use this when building or changing a function whose output can be checked. The order
matters: the expectation comes first, then the code. Do not write the implementation
and then a test that simply matches whatever it does.

## Steps

1. State the expectation. In one or two lines, say what the function should do for a
   specific input, and what the correct output is. Base this on what the code should
   do, not on what any existing code already does.
2. Show the user the expectation and ask them to confirm it is right before you rely
   on it.
3. Write a test that encodes the expectation. Include at least one normal case and one
   edge case, such as a missing value, an empty input, or a boundary value.
4. Run the test and show it failing. Confirm it fails for the right reason (the
   function is not implemented yet, or is wrong), not because the test itself is
   broken.
5. Write the implementation.
6. Run the test again and show it passing.

## Rules

- A test that cannot fail is worthless. If a test passes before the code exists, the
  test is wrong.
- Do not change the test just to make it pass. If the test is right and the code
  fails, fix the code.
- Keep each test checking one clear thing, so a failure points to one cause.
