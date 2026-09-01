# CHEFSOCKS - Rating 212

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Chef and Socks

Chef needs $A$ dollars to buy himself a new pair of socks for Christmas.
If he has $X$ dollars saved up and his parents give him an additional $Y$ dollars, will Chef be able to buy new socks?

### Input Format
- The first and only line of input will contain $3$ space-separated integers $A, X,$ and $Y$ — the cost of the socks, the amount of money Chef has saved up, and the additional money he received from his parents.
### Output Format

Output a single string denoting the answer: `"YES"` if Chef can afford the socks, and `"NO"` otherwise (without quotes).

Each character of the output may be printed in either uppercase or lowercase, i.e., the strings `NO`, `No`, `nO`, and `no` will all be treated as equivalent.

### Constraints
- $1 \leq A,X,Y \leq 100$
### Sample 1:
Input
Output

```
58 40 88
```

```
YES
```

### Explanation:

Chef has $40$ dollars and his parents gave him $88$ dollars. Now he has $40+88=128$ dollars which allows him to buy socks which cost only $58$ dollars.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-01T17:36:21.938Z  

```py
A,X,Y=map(int,input().split())
if X+Y>=A:
    print("YES")
else:
    print("NO")
```

---

[View on CodeChef](https://www.codechef.com/problems/CHEFSOCKS)