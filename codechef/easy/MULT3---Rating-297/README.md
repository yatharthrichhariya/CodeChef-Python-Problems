# MULT3 - Rating 297

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Multiple of 3

Given a positive integer $N$, find the nearest multiple of $3$.

Multiples of $3$ are $\ldots -6, -3, 0, 3, 6, 9, 12, 15, \ldots$.

Formally, find $X$, the multiple of $3$ with minimum value of $|N - X|$.

It can be proven that the answer is always unique, i.e. $2$ different multiples of $3$ cannot be nearest at the same time.

### Input Format
- The only line of input contains a single integer $N$.
### Output Format

For each test case, output on a new line the nearest multiple of $3$.

### Constraints
- $1 \le N \le 10$
### Sample 1:
Input
Output

```
1

```

```
0

```

### Explanation:

The nearest multiple is $0$.

For example, $3$ is not the answer because $|1 - 0| = 1 < |1 - 3| = 2$.

### Sample 2:
Input
Output

```
5

```

```
6

```

### Explanation:

The nearest multiple of $3$ is $6$.

### Sample 3:
Input
Output

```
9

```

```
9

```

### Explanation:

$9$ is itself a multiple of $3$.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-23T18:15:25.954Z  

```py
N = int(input())
if N % 3 == 0:
    print(N)
elif N % 3 == 1:
    print(N - 1)
else:
    print(N + 1)
```

---

[View on CodeChef](https://www.codechef.com/problems/MULT3)