# COMP4 - Rating 247

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Competition of 4

You are participating in an elite chess tournament for $4$ people in the world only.

There are prizes in this tournament, obviously. If you finish rank $i$, you get $1000 \cdot 2^{4 - i}$ rupees. Thus, the prizes are as follows:

- Rank $1$: $8000$ rupees
- Rank $2$: $4000$ rupees
- Rank $3$: $2000$ rupees
- Rank $4$: $1000$ rupees

You finished at rank $X$. How much prize money did you win?

### Input Format
- The first and only line of input contains a single integer $X$, your rank.
### Output Format

Output the amount of prize money you won in rupees.

### Constraints
- $1 \le X \le 4$
### Sample 1:
Input
Output

```
1

```

```
8000

```

### Explanation:

As explained in the statement, rank $1$ wins $1000 \cdot 2^{(4 - 1)} = 8000$ rupees.

### Sample 2:
Input
Output

```
4

```

```
1000

```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-08T14:59:30.219Z  

```py
X=int(input())
print(1000*(2**(4-X)))
```

---

[View on CodeChef](https://www.codechef.com/problems/COMP4)