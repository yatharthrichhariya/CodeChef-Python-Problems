# SHARING - Rating 232

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Sharing Cookies

Alice received $A$ cookies and Bob received $B$ cookies individually, but being good friends, they want to share them equally. Alice received more cookies than Bob, i.e. $A > B$.

Is it possible for Alice and Bob to share such that they both have equal number of cookies? Find the number of cookies Alice has to give Bob in that case, and otherwise print $-1$ to denote it is impossible.

### Input Format
- The first and only line contains $2$ integers $A$ and $B$.
### Output Format

Output the number of cookies Alice needs to give Bob or $-1$ if impossible.

### Constraints
- $1 \le B \lt A \le 10$
### Sample 1:
Input
Output

```
6 2

```

```
2

```

### Explanation:

If Alice gives Bob $2$ cookies, he has $6 - 2 = 4$ cookies left, and Bob has $2 + 2 = 4$ cookies. Hence, both have equal number of cookies.

### Sample 2:
Input
Output

```
5 2

```

```
-1

```

### Explanation:

The total number of cookies is $7$, which is not dividable fairly between Alice and Bob.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-18T17:03:36.030Z  

```py
A,B=map(int,input().split())
C=A-B
if C%2==0:
    print(C//2)
else:
    print("-1")
```

---

[View on CodeChef](https://www.codechef.com/problems/SHARING)