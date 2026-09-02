# MOVEMENT - Rating 215

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Move Grid

You are located at the coordinate $(0, 0)$ on a $2$D grid with perpendicular $X$ and $Y$ axes.

You will do the following moves:

- first, $A$ units along positive $X$ axis
- then, $B$ units along positive $Y$ axis
- then, $C$ units along negative $X$ axis
- finally, $D$ units along negative $Y$ axis

Find the coordinates of your final position.

### Input Format
- The first and only line of input contains $4$ integers - $A, B, C$ and $D$.
### Output Format

For each test case, output on a new line the $X$ and $Y$ coordinates of your final position.

### Constraints
- $1 \le A, B, C, D \le 10$
### Sample 1:
Input
Output

```
5 4 7 3

```

```
-2 1

```

### Explanation:

Initially, you started at $(0, 0)$

- $5$ steps along positive $X$, so you reached $(5, 0)$
- $4$ steps along positive $Y$, so you reached $(5, 4)$
- $7$ steps along negative $X$, so you reached $(-2, 4)$
- $3$ steps along negative $Y$, so you reached $(-2, 1)$

Thus, your final position is $(-2, 1)$.

### Sample 2:
Input
Output

```
1 1 1 1

```

```
0 0

```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-02T11:26:58.360Z  

```py
A,B,C,D=map(int,input().split())
X=A-C
Y=B-D
print(X,Y)
```

---

[View on CodeChef](https://www.codechef.com/problems/MOVEMENT)