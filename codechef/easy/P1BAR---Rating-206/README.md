# P1BAR - Rating 206

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Basketball Score

A basketball team scored $X$ successful  **3-pointers**  and $Y$ successful  **2-pointers**  in a game.
Your task is to compute the  **total score**  of the team.

Each 3-pointer is worth  **3 points**, and each 2-pointer is worth  **2 points**.

### Input Format
- A single line containing two integers $X$ and $Y$ — the number of successful 3-pointers and 2-pointers respectively.
### Output Format

Print a single integer — the total score of the team.

### Constraints
- $1 \leq X,Y \leq 10$
### Sample 1:
Input
Output

```
2 3
```

```
12
```

### Explanation:
- $2$ 3-pointers and $3$ 2-pointers are scored respectively. So total score is $2 *3 + 3* 2 = 12$.
### Sample 2:
Input
Output

```
1 3
```

```
9
```

### Explanation:
- $1$ 3-pointers and $3$ 2-pointers are scored respectively. So total score is $1 *3 + 3* 2 = 9$.
### Sample 3:
Input
Output

```
10 1
```

```
32
```

### Explanation:
- $10$ 3-pointers and $1$ 2-pointers are scored respectively. So total score is $10 *3 + 1* 2 = 32$.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-08-30T17:06:07.097Z  

```py
X,Y=map(int,input().split())
print((X*3)+(Y*2))
```

---

[View on CodeChef](https://www.codechef.com/problems/P1BAR)