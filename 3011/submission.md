# Problem Solving Submission

This file must be written by the student in their own words.

Use this template only for OJ problems that are marked as learning-log required.

Do not ask AI to write this file for you. AI may help check grammar, formatting, or clarity after you have written your own content.

If AI was used for this learning-log-required problem, also complete `ai_reflection.md`.

---

## 1. OJ Information

OJ problem number/title:

```text
3011
```

OJ submission ID, if submitted:

```text
546826
```

OJ status:

```text
Pass
```

Independent time spent on this problem:

```text
0-15 minutes
```

Choose one:

```text
0-15 minutes
15-30 minutes
30-60 minutes
1-3 hours
3-6 hours
6-24 hours
1-3 days
4-7 days
1-4 weeks
More than 4 weeks
```

How to count this time:

- Count only the time you actively worked on this problem independently.
- Start counting from when you first read the problem.
- Do not include breaks, meals, classes, sleep, time spent on other problems, or time when you were not working on this problem.
- If you used AI, count only the independent time before your first AI prompt.
- If you asked a friend, TA, or instructor for help, count only the independent time before your first help request.
- If you used both AI and human help, count only the independent time before the first outside help of any kind.
- If you did not use AI or human help, count the time before writing this `submission.md`.
- An estimate is acceptable, but it must be honest.

---

## 2. My Understanding

Write the problem in your own words.

Also explain the input, output, and important constraints.

If you do not fully understand the problem yet, write what you currently understand. Your understanding may be incomplete or incorrect, but you must make a genuine attempt.

```text
input 2 primary colors and output the result of mixing the colors is. output Error if one of the input isnt a primary color

```

---

## 3. My First Plan

Write your first plan before getting help from AI, a friend, a TA, an instructor, or before finalizing your code.

If you used AI, write the plan you had before your first AI prompt.

If you asked a friend, TA, or instructor for help, write the plan you had before asking for help.

If you did not use AI or human help, write the plan you had before or while you started coding.

This can be rough. It may be incomplete or different from your final solution.

You may write pseudocode, a flowchart idea, or step-by-step thinking.

```text
input 2 colors

use if else as in. if color 1 is blue and color 2 is red it outputs violet. and do that for every case


```

---

## 4. My Final Approach

Briefly explain the final algorithm or method you actually used in your submitted code.

This section is different from Section 3:

- Section 3 is your first plan before AI, human help, or before the final code.
- Section 4 is the final method used in your actual solution.
- If your final approach is the same as your first plan, write that it is the same and briefly explain why.

Do not copy AI's explanation.

Do not copy another person's explanation.

```text
input 2 colors

check every case. for example. if color 1 is red and color 2 is yellow. output orange.

and for reverse too. if color 1 is yellow and color 2 is red then output orange.

and for same color cases i check for col1 == col2. and if it is a primary color by checking if its in a list of primary colors. then print color1. because col1 and col2 are the same anyways

and else prints Error
```

---

## 5. My Tests

Write at least 3 test cases that you tried or designed by yourself.

Try to choose test cases that are different from each other.

For each test case, explain why you chose it.

If the input or output has many lines, write them inside the text blocks.

### Test Case 1

Why I chose this case:

```text
check if the program works in the first place
```

Input:

```text
Red
Blue
```

Expected output:

```text
Violet
```

Actual output:

```text
Violet
```

Result:

```text
Pass
```

### Test Case 2

Why I chose this case:

```text
see if the reverse works
```

Input:

```text
Blue
Red
```

Expected output:

```text
Violet
```

Actual output:

```text
Violet
```

Result:

```text
Pass
```

### Test Case 3

Why I chose this case:

```text
sgsgssgg isnt a primary color
```

Input:

```text
Red
sgsgssgg
```

Expected output:

```text
Error
```

Actual output:

```text
Error
```

Result:

```text
Pass
```

---

## 6. AI Use

Did you use AI for this problem?

```text
No
```

If yes, also complete:

```text
ai_reflection.md
```

If you only asked a friend, TA, or instructor and did not use AI, you do not need to complete `ai_reflection.md`.

---

## 7. Human Help / Collaboration

Did you ask a friend, TA, instructor, or another person for help on this problem?

```text
Yes
```

If yes, briefly explain what kind of help you received.

Allowed examples:

- explanation of the problem statement
- explanation of a programming concept
- hint about the approach
- debugging discussion
- test-case discussion
- help understanding an error message

Not allowed:

- copying another person's code
- submitting another person's solution
- asking another person to write the solution for you
- using another person's OJ submission
- asking another person to submit to the OJ for you

Who helped you?

```text
someone sitting next to me during PSCP lab.
```

What did they help with?

```text
discussed about what testcases i havent thought about. and it is same color inputs should output the same color. 
```

What did you still do by yourself?

```text
implement the code by writing col1 == col2 and col1 in ["Red","Yellow", "Blue"]. to check if it is also a primary color. so cases like. adsd == adsd doesnt happen
```

Did you copy any code from another person?

```text
No
```

---

## 8. Student Declaration

Write `Yes` for each statement.

| Statement | Yes/No |
|---|---|
| I wrote this submission in my own words. | yes |
| I understand my final code. | yes |
| I recorded the real OJ status. | yes |
| I did not copy AI-generated text directly into this file. | yes |
| I did not copy code from another person. | yes |
| If I received human help, I disclosed it in this file. | yes |
| I submitted the final code to the OJ by myself. | yes |