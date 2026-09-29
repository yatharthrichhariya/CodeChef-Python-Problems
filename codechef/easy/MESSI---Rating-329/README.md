# MESSI - Rating 329

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Football Training

As a football trainer, you have several players training under you. Each of these players are fans of either  *Leo*  or  *Ronald*,  **but not both**.

- $X$ of the players are fans of Leo, and want a free kick session to be carried out.
- $Y$ of the players are fans of Ronald, and want a penalty session to be carried out.

Note that each player is a fan of exactly one of Leo or Ronald, so there are $X+Y$ players in total.

It'd be nice if players are actually interested in their training, so you decide to hold whichever type of training has more people interested in it.

Given $X$ and $Y$, which type of training session will you hold?
It is guaranteed that $X \neq Y$.

### Input Format

The first and only line of input contains two space-separated integers $X$ and $Y$ — which denote the number of Leo's fans and the number of Ronald's fans, respectively.

### Output Format

For each test case, output on a new line which session will be carried out: `"FREEKICK"` if it'll be a free kick session, and `"PENALTY"` if it'll be a penalty session (without quotes).

Each character of the output may be printed in either uppercase or lowercase, i.e, if the answer is `PENALTY`, the strings `penalty`, `PENALTY`, `pEnALty`, and so on will all be accepted.

### Constraints
- $0 \leq X \leq 100$
- $0 \leq Y \leq 100$
- $X \neq Y$
### Sample 1:
Input
Output

```
10 7

```

```
FREEKICK

```

### Explanation:

$10$ players want a free kick session, while $7$ of them want a penalty session.
$10\gt 7$, so a free kick session will be carried out.

### Sample 2:
Input
Output

```
1 15
```

```
PENALTY
```

### Explanation:

$1$ player wants a free kick session, while $15$ of them want a penalty session.
So, a penalty session will be carried out.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-29T10:36:49.342Z  

```py
X,Y=map(int,input().split())
if X>Y:
    print("FREEKICK")
else:
    print("PENALTY")
```

---

[View on CodeChef](https://www.codechef.com/problems/MESSI)