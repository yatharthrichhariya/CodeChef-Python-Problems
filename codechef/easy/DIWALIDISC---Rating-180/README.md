# DIWALIDISC - Rating 180

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Diwali Discount

Chef is trying to buy a Diwali gift for Rs. $A$, and he has a voucher for Rs. $B$. Chef will have to pay the remaining amount after applying the voucher. If the voucher's value exceeds the gift's value, Chef will not have to pay anything.

Find the amount that Chef will pay for buying the gift.

### Input Format
- The first and only line of input contains $2$ integers - $A$ and $B$.
### Output Format

For each test case, output on a new line the amount paid by Chef.

### Constraints
- $1 \le A, B \le 5000$
### Sample 1:
Input
Output

```
3000 1000

```

```
2000
```

### Explanation:

Chef is trying to buy a gift of Rs. $3000$, and his voucher is of Rs. $1000$. Thus, he still has to pay $3000 - 1000 =$ Rs. $2000$.

### Sample 2:
Input
Output

```
1000 5000

```

```
0
```

### Explanation:

Chef's voucher value exceeds the gift value, so he has to pay nothing.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-08-26T18:28:35.133Z  

```py
A,B=map(int,input().split())
if A>B:
    print(A-B)
else:
    print("0")

```

---

[View on CodeChef](https://www.codechef.com/problems/DIWALIDISC)