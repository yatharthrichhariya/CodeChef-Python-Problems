# CRCK - Rating 217

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Christmas Cake

Chef plans to celebrate Christmas by baking a cake.

Christmas falls on the $25$-th of December.
Every day before Christmas, till the $24$-th of December, Chef will bake  **exactly one**  practice cake.

Today is the $X$-th of December. How many practice cakes will Chef bake starting from today?

### Input Format
- The first and only line of input will contain a single integer $X$ — today's date.
### Output Format

For each test case, output a single integer: the number of practice cakes Chef will bake.

### Constraints
- $1 \leq X \leq 24$
### Sample 1:
Input
Output

```
18

```

```
7

```

### Explanation:

If today is the $18$-th of December, Chef will bake one cake on each of the dates $18, 19, 20, 21, 22, 23, 24$, which is $7$ in total.

### Sample 2:
Input
Output

```
1
```

```
24
```

### Explanation:

Chef will bake one cake on every day from $1$ to $24$, which is $24$ cakes in total.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-02T11:44:03.202Z  

```py
X=int(input())
print(25-X)
```

---

[View on CodeChef](https://www.codechef.com/problems/CRCK)