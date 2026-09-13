# IED - Rating 271

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### International Education Day!

On the occasion of International Education Day, a fair is held in Chefland.

Both Chef and Chefina have set up their stalls.
Chef sells each item at his stall for $A$ rupees and Chefina sells each item at her store for $B$ rupees.

If both of them sell exactly $C$ items, find the maximum amount in sales amongst Chef and Chefina.

### Input Format

The input consists of three space-separated integers $A, B,$ and $C$ denoting the cost of each item at Chef's and Chefina's stall and the number of items they sell respectively.

### Output Format

Output the the maximum amount in sales amongst Chef and Chefina.

### Constraints
- $1 \leq A, B, C \leq 10$
- $A \neq B$
### Sample 1:
Input
Output

```
4 2 5

```

```
20

```

### Explanation:

Chef's total sale value is $4\cdot 5 = 20$ while Chefina's total sale value is $2\cdot 5 = 10$.
Thus, the maximum amongst these is $20$.

### Sample 2:
Input
Output

```
1 10 7
```

```
70
```

### Explanation:

Chef's total sale value is $1\cdot 7 = 7$ while Chefina's total sale value is $10\cdot 7 = 70$.
Thus, the maximum amongst these is $70$.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-13T14:42:55.636Z  

```py
A,B,C=map(int,input().split())
print(max(A,B)*C)
```

---

[View on CodeChef](https://www.codechef.com/problems/IED)