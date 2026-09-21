# TESTTGT - Rating 286

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Test Match Target

A cricket Test match between Australia and India is played over $4$ innings. Australia bat in the $1^\text{st}$ and $3^\text{rd}$ innings, while India bat in the $2^\text{nd}$ and $4^\text{th}$ innings.

Australia scored $X$ runs in the $1^\text{st}$ innings.

India scored $Y$ runs in the $2^\text{nd}$ innings.

Australia scored $Z$ runs in the $3^\text{rd}$ innings.

After $3$ innings, Australia have a combined total from both their innings. India have batted once so far. The difference between Australia's combined total and India's score is called the  *lead*.

In cricket, a team wins by  *strictly exceeding*  the opponent's total. So, India must score  **at least one more**  than the lead to win.

Given $X$, $Y$ and $Z$, find the minimum number of runs India must score in the $4^\text{th}$ innings to win the match.

If India's first innings score already exceeds Australia's combined total, India have already won before the $4^\text{th}$ innings — print $0$ in this case.

### Input Format
- The first and only line of input contains $3$ space-separated integers $X$, $Y$ and $Z$.
### Output Format

Print a single integer — the minimum number of runs India must score in the $4^\text{th}$ innings to win the match.

### Constraints
- $1 \le X, Y, Z \le 1000$
### Sample 1:
Input
Output

```
100 200 300

```

```
201

```

### Explanation:

Australia scored a total of $100 + 300 = 400$ runs across both innings.
India have scored $200$ runs so far, so they trail by $400 - 200 = 200$ runs.
India must score strictly more than Australia's total, so they need $200 + 1 = 201$ runs in the fourth innings.

### Sample 2:
Input
Output

```
100 500 200

```

```
0

```

### Explanation:

Australia scored a total of $100 + 200 = 300$ runs. India have already scored $500$ runs, which exceeds Australia's total. Hence, the answer is $0$.

### Sample 3:
Input
Output

```
200 500 300

```

```
1

```

### Explanation:

Australia scored a total of $200 + 300 = 500$ runs. India have also scored $500$ runs so far. Since a tie is not enough to win, India need $1$ more run in the fourth innings.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-21T12:22:55.537Z  

```py
X,Y,Z=map(int,input().split())
A=X+Z
B=(A-Y)+1
if A>=Y:
    print(B)
else:
    print("0")
```

---

[View on CodeChef](https://www.codechef.com/problems/TESTTGT)