# TCG - Rating 311

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Capital Gain Tax

The annual budget for ChefLand has been announced and people are concerned about the modification in capital gain tax.

Given that the capital gain tax changed from $X \%$ to $Y \%$, find whether it has `INCREASED`, `DECREASED`, or remained the `SAME`.

### Input Format
- The first and only line of input consists of two space-separated integers $X$ and $Y$ denoting the previous and new value of capital gain tax.
### Output Format

Output on a new line:

- INCREASED, if the capital gain tax has increased;
- DECREASED, if the capital gain tax has decreased;
- SAME, if the capital gain tax remained the same.

You may print each character in uppercase or lowercase. For example, the strings `SAME`, `same`, `Same`, and `sAmE` would be considered identical.

### Constraints
- $10 \leq X, Y \leq 30$
### Sample 1:
Input
Output

```
10 12

```

```
INCREASED
```

### Explanation:

The updated value of capital gain tax is higher, thus it has increased.

### Sample 2:
Input
Output

```
30 25

```

```
DECREASED
```

### Explanation:

The updated value of capital gain tax is lower, thus it has decreased.

### Sample 3:
Input
Output

```
15 15

```

```
SAME
```

### Explanation:

The updated value of capital gain tax is same as the previous value.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-23T10:09:57.990Z  

```py
X,Y=map(int,input().split())
if X>Y:
    print("DECREASED")
elif X<Y:
    print("INCREASED")
else:
    print("SAME")
```

---

[View on CodeChef](https://www.codechef.com/problems/TCG)