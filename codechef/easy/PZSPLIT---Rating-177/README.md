# PZSPLIT - Rating 177

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Pizza Split

Chef and Chefina are ordering pizza for dinner.
Each pizza has $N$ slices.

What is the minimum number of pizzas they need to order, so that both Chef and Chefina can eat an equal number of slices?
Chef and Chefina must eat a  **positive integer**  number of slices.

### Input Format
- The first and only line of input will contain a single integer $N$, the number of slices in one pizza.
### Output Format

Print a single integer: the minimum number of pizzas that must be ordered so that Chef and Chefina can eat an equal number of slices.

### Constraints
- $1 \leq N \leq 10$
### Sample 1:
Input
Output

```
6

```

```
1

```

### Explanation:

One pizza has $6$ slices. Chef and Chefina can eat $3$ each.

### Sample 2:
Input
Output

```
3

```

```
2

```

### Explanation:

One pizza is not enough for Chef and Chefina to eat an equal number of slices.
Instead, they must order two pizzas, and then eat $3$ slices each.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-08-26T18:04:33.544Z  

```py
N=int(input())
if N%2==0:
    print('1')
else:
    print('2')
```

---

[View on CodeChef](https://www.codechef.com/problems/PZSPLIT)