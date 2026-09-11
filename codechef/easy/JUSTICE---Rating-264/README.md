# JUSTICE - Rating 264

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### International Justice Day

In honor of International Justice Day, the Supreme Court of Chefland has decided to address all pending cases simultaneously.

For a given case, the accused will be convicted if the convincing power of the prosecution, denoted by integer $X$, is greater than or equal to the convincing power of the defense, denoted by integer $Y$.

Determine whether the accused is convicted.

### Input Format
- The only line of input consists of space-separated integers $X$ and $Y$, denoting the convincing powers of prosecution and defense, respectively.
### Output Format

Output on a new line, `YES`, if the accused is convicted and `NO` otherwise.

You may print each character of the string in uppercase or lowercase (for example, the strings `YES`, `yEs`, `yes`, and `yeS` will all be treated as identical).

### Constraints
- $1 \leq X, Y \leq 10$
### Sample 1:
Input
Output

```
5 4

```

```
YES
```

### Explanation:

The convincing power of prosecution is $5$ which is greater than that of defense, which is $4$.

### Sample 2:
Input
Output

```
1 10

```

```
NO
```

### Explanation:

The convincing power of prosecution is $1$ which is less than that of defense, which is $10$.

### Sample 3:
Input
Output

```
7 7

```

```
YES
```

### Explanation:

The convincing power of prosecution is same as that of defense. Thus, the accused is convicted.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-11T08:50:46.334Z  

```py
X,Y=map(int,input().split())
if X >= Y:
    print("Yes")
else:
    print("No")
```

---

[View on CodeChef](https://www.codechef.com/problems/JUSTICE)