# ICE_CREAM - Rating 354

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### ICE CREAM

Chef wants to buy $2$ ice creams, each costing $X$ dollars, for him and Chefina.
However, he only has $Y$ dollars with him. Will he be able to buy $2$ ice creams?

### Input Format
- The only line of input will contain $2$ space-separated integers $X$ and $Y$, the price of each ice cream and the money Chef has.
### Output Format

Print `YES` if Chef will be able to buy two ice creams, otherwise print `NO`.

You may print each character of the string in uppercase or lowercase (for example, the strings `YES`, `yEs`, `yes`, and `yeS` will all be treated as identical).

### Constraints
- $1 \leq X, Y \leq 100$
### Sample 1:
Input
Output

```
5 10

```

```
YES
```

### Explanation:

He requires $10$ dollars to buy 2 ice creams and he has that amount.

### Sample 2:
Input
Output

```
6 11

```

```
NO
```

### Explanation:

Chef requires $12$ dollars to buy 2 ice creams, he only has $11$ dollars hence he will be unable to buy them.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-11T17:55:11.912Z  

```py
X,Y=map(int,input().split())
if X*2<=Y:
    print("YES")
else:
    print("NO")
```

---

[View on CodeChef](https://www.codechef.com/problems/ICE_CREAM)