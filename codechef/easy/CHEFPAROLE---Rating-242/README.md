# CHEFPAROLE - Rating 242

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Chef and Parole

Chef must spend at least 7 days in prison to be released on parole.

Given the number of days he spent, output YES if will be released, otherwise NO.

### Input Format

The first and only line of input consists of an integer X denoting the number of days spent in prison by the Chef

### Output Format

Output Yes, if the Chef will be released on parole, and No otherwise.

You may print each character of the string in uppercase or lowercase (for example, the strings YES, yEs, yes, and yeS will all be treated as identical).

### Constraints
- $1 \leq X \leq 30$
### Sample 1:
Input
Output

```
5
```

```
No
```

### Explanation:

Chef has not completed 7 days in prison

### Sample 2:
Input
Output

```
12
```

```
Yes
```

### Explanation:

Chef has spent more than 7 days in the prison

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-08T14:10:46.421Z  

```py
X=int(input())
if X>=7:
    print("Yes")
else:
    print("No")
```

---

[View on CodeChef](https://www.codechef.com/problems/CHEFPAROLE)