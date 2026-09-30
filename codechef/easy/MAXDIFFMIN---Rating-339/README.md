# MAXDIFFMIN - Rating 339

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Max minus Min

Chef is given $3$ integers $A, B,$ and $C$ such that $A \lt B \lt C$.

Chef needs to find the value of $max(A, B, C) - min(A, B, C)$.

Here $max(A, B, C)$ denotes the maximum value among $A, B, C$ while $min(A, B, C)$ denotes the minimum value among $A, B, C$.

### Input Format
- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of $3$ integers $A, B, C$.
### Output Format

For each test case, output the value of $max(A, B, C) - min(A, B, C)$.

### Constraints
- $1 \leq T \leq 10$
- $1 \leq A \lt B \lt C \leq 10$
### Sample 1:
Input
Output

```
4
1 3 10
5 6 7
3 8 9
2 5 6

```

```
9
2
6
4

```

### Explanation:

 **Test case $1$:**  Here, $max(1, 3, 10) = 10$ and $min(1, 3, 10) = 1$. Thus, the difference is $9$.

 **Test case $2$:**  Here, $max(5, 6, 7) = 7$ and $min(5, 6, 7) = 5$. Thus, the difference is $2$.

 **Test case $3$:**  Here, $max(3, 8, 9) = 9$ and $min(3, 8, 9) = 3$. Thus, the difference is $6$.

 **Test case $4$:**  Here, $max(2, 5, 6) = 6$ and $min(2, 5, 6) = 2$. Thus, the difference is $4$.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-30T10:59:33.130Z  

```py
T=int(input())
for i in range(T):
    A,B,C=map(int,input().split())
    print(max(A,B,C)-(min(A,B,C)))
```

---

[View on CodeChef](https://www.codechef.com/problems/MAXDIFFMIN)