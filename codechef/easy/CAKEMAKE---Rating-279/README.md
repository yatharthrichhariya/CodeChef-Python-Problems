# CAKEMAKE - Rating 279

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Cake Making

There are exactly $100$ colours in the world, numbered $1$ to $100$.

Chef is making a $2$-layered cake, and all that is left is deciding the colours of the $2$ layers.

Chef has decided that we can choose any of the colours $1, 2, \ldots, A$ for the first layer, and any of the colours $1, 2, \ldots, B$ for the second layer.

However, there is an  **extra constraint**. To encourage diversity, the first and the second layer should not have the same colour.

How many different cakes are possible while following the above rules? $2$ cakes are said to be different when either the first layer or the second layer has a different colour.

### Input Format
- The first and only line of input contains $2$ integers $A$ and $B$.
### Output Format

Output the total number of possible cakes.

### Constraints
- $1 \le A, B \le 100$
### Sample 1:
Input
Output

```
2 3

```

```
4

```

### Explanation:

The following cakes are possible: (The first number represents the colour of layer $1$ and the second number the colour of layer $2$)

- $(1, 2)$
- $(1, 3)$
- $(2, 1)$
- $(2, 3)$
### Sample 2:
Input
Output

```
1 1

```

```
0

```

### Explanation:

There are no possible cakes because we must make sure layer $1$ and layer $2$ do not have the same colour.

### Sample 3:
Input
Output

```
100 5

```

```
495

```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-01T18:00:51.272Z  

```py
A,B=map(int,input().split())
print((A*B)-(min(A,B)))
```

---

[View on CodeChef](https://www.codechef.com/problems/CAKEMAKE)