# TIMA - Rating 181

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Time Machine

Chef is currently in the year $X$ in Chefland. He has a time machine that allows him to travel at most $25$ years into the future, but he can use it only once.

Determine whether Chef can reach the year $2050$ with a single use of the time machine.

### Input Format

A single integer $X$, representing current year in Chefland.

### Output Format

Print `YES` if Chef can reach the year 2050, otherwise print `NO`.

You may print each character of the string in uppercase or lowercase (for example, the strings `YES`, `yEs`, `yes`, and `yeS` will all be treated as identical).

### Constraints
- $2000 \leq X \leq 2050$
### Sample 1:
Input
Output

```
2050

```

```
Yes
```

### Explanation:

Chef is already in the year $2050$, so there's no need to use the time machine.

### Sample 2:
Input
Output

```
2000

```

```
No
```

### Explanation:

Chef can use the time machine to travel up to $25$ years into the future, but that won't take him beyond the year $2025$.

### Sample 3:
Input
Output

```
2030

```

```
Yes
```

### Explanation:

By using the time machine, Chef can travel $20$ years into the future, reaching the year $2050$.

### Sample 4:
Input
Output

```
2025

```

```
Yes
```

### Explanation:

By using the time machine, Chef can travel $25$ years into the future, reaching the year $2050$.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-08-27T17:45:59.818Z  

```py
X=int(input())
A=X+25
if A>=2050:
    print("Yes")
else:
    print("No")
```

---

[View on CodeChef](https://www.codechef.com/problems/TIMA)