# P1149 - Rating 291

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Approximate Answer

You are solving a problem whose correct answer is the integer $Y$.
The answer you obtained, however, is the integer $X$.

Your answer will be considered correct if the difference between $X$ and $Y$ is at most $K$.
In other words, your answer is considered correct if and only if:

$$ |X-Y| \leq K $$

Given the values of $X$, $Y$, and $K$, determine whether your answer $X$ is correct or not.

Note that $|x|$ denotes the absolute value of $x$.
For example, $|12| = 12, |-15| = 15,$ and $|0| = 0$.

### Input Format
- The first and only line of input will contain three space-separated integers $X$, $Y$ and $K$ — your answer, the correct answer, and the the maximum allowed difference, respectively.
### Output Format

Output the answer on a single line: `"Yes"` if your answer is considered correct, and `"No"` otherwise (without quotes).

Each letter of the output may be printed in either uppercase or lowercase, i.e, the strings `NO`, `no`, `No`, and `nO` will all be treated as equivalent.

### Constraints
- $1 \leq X,Y,K \leq 20$
### Sample 1:
Input
Output

```
10 5 4
```

```
No
```

### Explanation:

$|X-Y| = |10-5| = 5$, while $K = 4$.
Since $|X-Y| \gt K$, the answer is not considered correct.

### Sample 2:
Input
Output

```
10 5 5
```

```
Yes
```

### Explanation:

$|X-Y| = |10-5| = 5$, while $K = 5$.
Since $|X-Y| \leq K$, the answer is considered correct.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-22T09:48:14.805Z  

```py
X,Y,K=map(int,input().split())
if abs(X-Y)<=K:
    print("Yes")
else:
    print("No")
```

---

[View on CodeChef](https://www.codechef.com/problems/P1149)