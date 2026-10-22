# BETWEEN - Rating 213

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Exun Leaderboard

The Exun quiz leaderboard has no ties. Your team is ranked $X$-th in the leaderboard, and your rival team is ranked $Y$-th.

Find how many teams are ranked strictly between you and your rival.

### Input Format
- The first and only line of input contains $2$ integers - $X$ and $Y$.
### Output Format

Output the number of teams that are ranked strictly between you and your rival.

### Constraints
- $1 \le X, Y \le 10$
- $X \ne Y$
### Sample 1:
Input
Output

```
1 5

```

```
3

```

### Explanation:

Your team is ranked $1$, and your rival's team is ranked $5$. There are $3$ teams ($2$nd, $3$rd and $4$th) between you.

### Sample 2:
Input
Output

```
2 1

```

```
0

```

### Explanation:

Your rival team is $1$st, and you are $2$nd, no teams between you.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-22T18:02:30.425Z  

```py
X,Y=map(int,input().split())
A=abs(Y-X)
print(A-1)
```

---

[View on CodeChef](https://www.codechef.com/problems/BETWEEN)