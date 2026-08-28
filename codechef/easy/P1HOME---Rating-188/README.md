# P1HOME - Rating 188

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Dice Play

Chef is playing with two standard six-sided dice. After rolling both dice once, Chef observes the numbers appearing on them.

You are given two integers $A$ and $B$ — the numbers shown on the first and second die, respectively.
Your task is to determine whether both dice show the same number. If they are equal, output `YES`; otherwise, output `NO`.

### Input Format

The first and only line of input contains two space-separated integers $A$ and $B$ — the numbers shown on the first and second die, respectively.

### Output Format

Output a single string on a new line:

Print `YES` if both dice show the same number. Otherwise, print `NO`.
You may print each character of the output in either uppercase or lowercase.

### Constraints
- $1 \leq A \leq 6$
- $1 \leq B \leq 6$
### Sample 1:
Input
Output

```
1 1
```

```
Yes
```

### Explanation:

Since $A$ is equal to $B$, print `Yes`.

### Sample 2:
Input
Output

```
1 3
```

```
No
```

### Explanation:

Since $A$ is not equal to $B$, print `No`.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-08-28T17:23:22.941Z  

```py
A,B=map(int,input().split())
if A==B:
    print("Yes")
else:
    print("No")
```

---

[View on CodeChef](https://www.codechef.com/problems/P1HOME)