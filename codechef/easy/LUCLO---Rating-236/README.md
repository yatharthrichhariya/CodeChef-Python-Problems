# LUCLO - Rating 236

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Lucky Clover

Chef heard that four-leaf clovers bring good luck, so he went looking for one.

In his search, Chef found $N$ clovers in total. Out of them,  **exactly one**  was a four-leaf clover, and all the others were three-leaf clovers.
How many leaves did Chef collect in total, across all the clovers?

### Input Format

The only line of input will contain a single integer $N$, the number of clovers Chef found.

### Output Format

Print one integer: the total number of leaves Chef collected.

### Constraints
- $1 \leq N \leq 10$
### Sample 1:
Input
Output

```
5

```

```
16
```

### Explanation:

Chef found $5$ clovers. One of them is a four-leaf clover, and the other four are three-leaf clovers.
So, the total number of leaves is $4 + 3\cdot 4 = 4 + 12 = 16$.

### Sample 2:
Input
Output

```
1

```

```
4
```

### Explanation:

Chef found only one clover. It has to be a four-leaf clover, so Chef collected $4$ leaves in total.

### Sample 3:
Input
Output

```
10

```

```
31
```

### Explanation:

Chef found $10$ clovers. One of them is a four-leaf clover, and the others are three-leaf clovers.
So, the total number of leaves is $4 + 3\cdot 9 = 4 + 27 = 31$.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-03T15:01:01.618Z  

```py
N=int(input())
if N == 1:
    print("4")
else:
    print((N-1)*4)

```

---

[View on CodeChef](https://www.codechef.com/problems/LUCLO)