# SELLCOIN - Rating 218

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Selling Coins

Chef has $A$ silver coins and $B$ gold coins.

He can avail the following $2$ deals (multiple times):

- Sell $1$ silver coin for Rs. $1$.
- Trade $1$ gold coin for $2$ silver coins.

Chef is trying to sell all his coins and earn money now. How much money will Chef be able to earn?

### Input Format
- The first and only line of each test case contains $2$ integers - $A$ and $B$.
### Output Format

For each test case, output on a new line the amount of money Chef can earn.

### Constraints
- $1 \le A, B \le 10$
### Sample 1:
Input
Output

```
2 1

```

```
4

```

### Explanation:

Chef can first trade his gold coin for $2$ silver coins. Now he has $4$ silver coins in total, and he sells all of them for Rs. $4$.

### Sample 2:
Input
Output

```
10 10

```

```
30

```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-03T10:01:33.473Z  

```py
A,B=map(int,input().split())
C=A*1
D=B*2
print(C+D)
```

---

[View on CodeChef](https://www.codechef.com/problems/SELLCOIN)