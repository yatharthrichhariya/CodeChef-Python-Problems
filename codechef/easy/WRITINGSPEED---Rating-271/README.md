# WRITINGSPEED - Rating 271

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Writing Speed

Rahul has a $5$-page assignment due in $60$ minutes. He can write one page in $X$ minutes.

Determine if Rahul can complete the assignment within the given time constraint.

### Input Format
- The only line of input will contain a single integer $X$, denoting the time taken (in minutes) by Rahul to write one page.
### Output Format

Print `YES` if Rahul can complete the assignment in time, otherwise print `NO`.

You may print each character of the output in either uppercase or lowercase (for example, the strings `YES`, `yEs`, `yes`, and `yeS` will all be treated as identical).

### Constraints
- $1 \leq X \leq 1000$
### Sample 1:
Input
Output

```
5
```

```
YES
```

### Explanation:

If Rahul can write one page in $5$ minutes, then he can write $5$ pages in $25$ minutes. So, he will be able to complete the assignment in time.

### Sample 2:
Input
Output

```
45
```

```
NO
```

### Explanation:

If Rahul can write one page in $45$ minutes, then he will write $5$ pages in $225$ minutes. So, he will not be able to complete the assignment in time.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-14T18:27:01.392Z  

```py
X = int(input())
if 5 * X <= 60:
    print("YES")
else:
    print("NO")
```

---

[View on CodeChef](https://www.codechef.com/problems/WRITINGSPEED)