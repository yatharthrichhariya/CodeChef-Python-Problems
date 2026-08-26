# VACCLOTH - Rating 177

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Vacation Clothes

Chef is going on a vacation for $N$ days. Each day, he must wear a fresh set of clothes.

Whenever a set is worn on day $d$, it is sent for cleaning and becomes available again only on day $d + 7$. A set that returns from cleaning on some day may be worn again that same day.

What is the minimum number of sets of clothes Chef must carry so that he always has something to wear for all $N$ days?

### Input Format
- The first and only line contains a single integer $N$.
### Output Format

Output the minimum number of sets of clothes Chef needs to carry.

### Constraints
- $1 \le N \le 10$
### Sample 1:
Input
Output

```
3

```

```
3

```

### Explanation:

Chef needs to carry $3$ sets of clothes for each of the $3$ days.

### Sample 2:
Input
Output

```
10

```

```
7

```

### Explanation:

Chef only needs to carry $7$ sets, because he can wear the first set again on day $8$, the second set again on day $9$ and the third set again on day $10$.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-08-26T18:21:57.082Z  

```py
N=int(input())
if N<7:
    print(N)
else:
    print("7")
```

---

[View on CodeChef](https://www.codechef.com/problems/VACCLOTH)