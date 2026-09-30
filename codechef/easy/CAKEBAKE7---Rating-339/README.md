# CAKEBAKE7 - Rating 339

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Cake Baking

Chef knows $N$ customers will come to his bakery today, and so he has baked $M$ cakes ($M \ge N$).

Every customer needs at least one cake, otherwise they will for sure be unhappy. Further, if a customer is able to buy  **two**  or more cakes, then they will be happy.

Chef wants to maximize the number of happy customers while not having any unhappy customers. What is the maximum possible happy customers?

### Input Format
- The first and only line of each test case contains $2$ integers - $N$ and $M$.
### Output Format

Output the maximum number of happy customers.

### Constraints
- $1 \le N \le M \le 10$
### Sample 1:
Input
Output

```
3 7

```

```
3

```

### Explanation:

Chef can make all the customers happy by letting each buy $2$ cakes, and having $1$ cake leftover.

### Sample 2:
Input
Output

```
4 6

```

```
2

```

### Explanation:

Chef can let customers $1$ and $2$ buy $2$ cakes, and customers $3$ and $4$ buy $1$ cake each.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-30T11:41:41.779Z  

```py
N,M=map(int,input().split())
B=M//N
if (B>=2):
    print(N)
else:
    print(M%N)
```

---

[View on CodeChef](https://www.codechef.com/problems/CAKEBAKE7)