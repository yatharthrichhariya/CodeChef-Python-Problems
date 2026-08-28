# REDBLUEGEM - Rating 185

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Red and Blue Gems

There are $R$ red gems and $B$ blue gems. Each red gem can be sold for $P$ coins, while a blue gem can be sold for $Q$ coins.

It is not allowed to take gems of both colours. You may either take all of the red gems, or take all of the blue gems.

Find the maximum number of coins you can obtain by taking some of the gems and then selling them.

### Input Format
- The first and only line of input contains $4$ integers - $R, B, P, Q$.
### Output Format

For each test case, output on a new line the maximum number of coins you can make.

### Constraints
- $1 \le R, B, P, Q \le 10$.
### Sample 1:
Input
Output

```
2 3 5 3

```

```
10

```

### Explanation:

Taking the red gems would get you $2 \cdot 5 = 10$ coins, while taking the blue gems would get you $3 \cdot 3 = 9$ coins. Hence you should take the red gems.

### Sample 2:
Input
Output

```
1 1 6 7

```

```
7

```

### Explanation:

There is only $1$ red gem and $1$ blue gem. The blue gem sells for more, so you should take it, and get $7$ coins.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-08-28T17:16:35.241Z  

```py
R,B,P,Q=map(int,input().split())
A=R*P
S=B*Q
if A>S:
    print(A)
else:
    print(S)
```

---

[View on CodeChef](https://www.codechef.com/problems/REDBLUEGEM)