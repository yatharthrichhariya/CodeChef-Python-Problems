# MINWAGE - Rating 247

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Minimum Wage

The minimum wage in Chefland is $11$ dollars per hour.

Given that Chef earns $X$ dollars per hour, find whether his income is  **strictly above**  the minimum wage.

### Input Format
- The first and only line contains an integer $X$, denoting the income of Chef per hour.
### Output Format

Output on a new line, `YES`, if Chef's income is  **strictly above**  the minimum wage. Otherwise, output `NO`.

You may print each character of the string in uppercase or lowercase (for example, the strings `YES`, `yEs`, `yes`, and `yeS` will all be treated as identical).

### Constraints
- $1 \le X \le 20$
### Sample 1:
Input
Output

```
20

```

```
YES

```

### Explanation:

Chef's income is $20$ dollars per hour, which is strictly higher than the minimum wage.

### Sample 2:
Input
Output

```
11

```

```
NO
```

### Explanation:

Chef's income is $11$ dollars per hour, which is not higher than the minimum wage.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-08T14:22:47.473Z  

```py
X=int(input())
if X > 11:
    print("Yes")
else:
    print("No")
```

---

[View on CodeChef](https://www.codechef.com/problems/MINWAGE)