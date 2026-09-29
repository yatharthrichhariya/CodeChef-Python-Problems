# LEGSP - Rating 326

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Leg Space

There are $N$ students  **including**  Chef in a school. The school bus has $M$ seats, and every student in the school travels on the bus.
It is guaranteed that $N \leq M$, so that everyone will have a seat.

Chef is happy when the school bus is  *not*  full.
Given $N$ and $M$, your task is to find out whether Chef will be happy.

### Input Format

The only line of input will contain two space-separated integers $N$ and $M$, denoting the number of students in the school and the number of seats in the school bus respectively.

### Output Format

For each test case, output on a new line the answer: `YES`, if Chef will be happy, and `NO` otherwise.

You may print each character of the string in uppercase or lowercase (for example, the strings `YeS`, `yEs`, `yes`, and `YES` will all be treated as identical).

### Constraints
- $1 \leq N \leq M \leq 10$
### Sample 1:
Input
Output

```
2 3

```

```
YES

```

### Explanation:

There are $2$ students and $3$ seats on the bus.
So, there will be one empty seat on the bus and Chef will be happy.

### Sample 2:
Input
Output

```
6 6

```

```
NO

```

### Explanation:

There are $6$ students and $6$ seats on the bus.
The bus will be full and Chef will not be happy.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-29T10:07:06.883Z  

```py
N,M=map(int,input().split())
if N<M:
    print("Yes")
else:
    print("No")
```

---

[View on CodeChef](https://www.codechef.com/problems/LEGSP)