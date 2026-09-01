# PAYSC - Rating 213

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Payment Scheme

Chef picked out several items in a shop, and now has to pay for them.

The shop offers Chef two payment schemes:

- Pay $100$ coins immediately, and then pay $X$ coins every week for the next four weeks.
- Pay $300$ coins immediately, with no future payments required.

Find the minimum possible number of coins Chef needs to pay if he chooses the payment scheme appropriately.

### Input Format
- The input contains a single integer $X$ — the required weekly payment for the first payment scheme.
### Output Format

Output a single integer: the minimum possible number of coins Chef needs to pay.

### Constraints
- $1 \le X \le 100$
### Sample 1:
Input
Output

```
8

```

```
132
```

### Explanation:

In this case, it's ideal to choose the first payment scheme: pay $100$ coins immediately, and then pay $X = 8$ coins each week for the next four weeks.
The total cost comes out to $100 + 4\cdot 8 = 132$, which is better than paying $300$ via the second option.

### Sample 2:
Input
Output

```
77

```

```
300
```

### Explanation:

In this case, since $X = 77$ it's better to choose the second scheme and pay $300$ coins immediately.
The first scheme would lead to a total of $100 + 4\cdot 77 = 408$ coins which is more expensive.

### Sample 3:
Input
Output

```
39
```

```
256
```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-01T17:43:22.481Z  

```py
X=int(input())
A=100+4*X
if A>=300:
    print("300")
else:
    print(A)
```

---

[View on CodeChef](https://www.codechef.com/problems/PAYSC)