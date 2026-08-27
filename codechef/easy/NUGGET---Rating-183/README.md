# NUGGET - Rating 183

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Moneymaking

Chef has $X$  *nuggets*  and $Y$  *star pieces*  with him.

Each nugget sells for $5000$ coins, and each star piece sells for $9800$ coins.

How much money can Chef make by selling all of his items?

### Input Format
- The only line of input will contain two space-separated integers $X$ and $Y$ — the number of nuggets and star pieces Chef has.
### Output Format

Output a single integer: the amount of money Chef can earn by selling all his items.

### Constraints
- $0 \leq X, Y \leq 10$
### Sample 1:
Input
Output

```
2 3

```

```
39400
```

### Explanation:

There are two nuggets and three star pieces, so Chef will obtain $2\times 5000 + 3\times 9800 = 10000 + 29400 = 39400$ from selling them all.

### Sample 2:
Input
Output

```
4 0

```

```
20000
```

### Explanation:

There are four nuggets and no star pieces, Chef will obtain $4\times 5000 = 20000$ from selling them all.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-08-27T18:01:41.366Z  

```py
X,Y=map(int,input().split())
print((X*5000)+(Y*9800))

```

---

[View on CodeChef](https://www.codechef.com/problems/NUGGET)