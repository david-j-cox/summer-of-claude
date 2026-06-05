# Week 2 - Driving the Loop

Goal for the week: get comfortable with the back-and-forth. You ask, the tool
acts, you look at what it did, you correct it, and you repeat. That loop is the
whole job. One-shot prompts rarely work. This week is about steering it well 
and starting to check the work.

## Give instructions the system can follow
A vague ask gets a vague result. The more you say, the better it does. A good
instruction usually has three parts:
- What you want: "write a script that..."
- Any context it needs: "...the data is in `data/survey.csv`, one row per
  participant..."
- What "done" looks like: "...it should print the mean of each numeric column
  and save a cleaned copy."

Try the same request once vague, once specific, and compare what you get. Describe
the contrast. 

## Watch what it does
The tool does not just generate text. The system takes actions (reading files, editing them,
running commands). Each of those is a tool call, and you can watch them happen.
Do not look away while it works. 
- Read the steps as they scroll by: which file did it open, what command did it
  run, what changed.
- Claude Code: press Ctrl+O to open the full transcript and see every command
  and its complete output.
- When it changes a file, it shows a diff - the before-and-after, with lines
  added and removed. Read the diff before you accept it.

Tool calls are deterministic software. Once you realize this, it's easier to see
that the LLM does little work and is not that skilled. 

Software is doing the work. And, you can have Claude build you the software so 
your output is deterministic and accurate and not probabilistic and change
from run-to-run.  

## Correcting and steering
You are not stuck with the first try. Tell it what is wrong and it will adjust.
- "That is close, but the column is named `score`, not `Score`."
- "Undo that last change and try a simpler approach."
- "Stop - explain what you are about to do before you do it."

Steering mid-task is normal and expected. Each round is one iteration.

## Writing some of it yourself (Learning mode)
If you want to start writing a little code yourself, try Learning mode. Instead
of doing everything, the tool leaves a marked spot - `TODO(human)` - for you to
fill in, then continues.
- Claude Code: run `/config`, set Output style to Learning.
- Either tool, in plain English: "Leave one small piece for me to write, and
  tell me what it needs to do."

Switch back to Explanatory any time you get stopped and aren't sure what to do. 
You can also ask the system to help prompt you toward the solution. You can learn 
as much or as little as you'd like. 

Learning to embed learning in these interactions is the route to avoiding 
deskilling and neverskilling. 

## Checking the work
When the tool reports 
success, do not take its word for it.
- Run the thing yourself and read the actual output.
- Ask: "What did you assume here? Where could this be wrong?"
- Ask it to test its own work and show you the test and the result.

Catching the tool being confidently wrong is a win, not a failure. This is the
skill.

## Words you met this week
- tool: a specific action the agent can take (read a file, run a command).
- tool call: one use of a tool; the steps you see scrolling as it works.
- diff: a before-and-after view of a file showing exactly what changed.
- output style: a setting for how the agent talks to you (Explanatory, Learning).
- iterate / iteration: one round of ask -> act -> review -> correct.
- session: one continuous conversation with the agent.
- steering: redirecting the system while it works - telling it to change, stop, or
  try something different mid-task, not only at the start.

Full running glossary: ../resources/glossary.md
