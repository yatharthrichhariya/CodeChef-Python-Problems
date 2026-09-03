# IOI2024 - Rating 219

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### IOI 2024

IOI $2024$ is being held in Egypt, starting from the $1$-st of September and ending on the $8$-th of September.

Given a date $X$ in September, output `YES` if IOI is ongoing then, otherwise `NO`.

### Input Format
- The first and only line of input contains one integer $X$ - the date in September.
### Output Format

Output either `YES` or `NO`, depending on whether IOI is ongoing on September $X$.

Each character of the output may be printed in either lowercase or uppercase - that is, the strings `no`, `NO`, `No`, and `nO` will all be treated as equivalent.

### Constraints
- $1 \le X \le 30$
### Sample 1:
Input
Output

```
8

```

```
YES

```

### Explanation:

IOI is said to be ongoing even on its last day.

### Sample 2:
Input
Output

```
9

```

```
NO
```

### Explanation:

IOI already ended on $8$-th of September.

### Sample 3:
Input
Output

```
3

```

```
YES
```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-03T10:08:54.962Z  

```py
X=int(input())
if X>=8:
    print("Yes")
else:
    print("No")
```

---

[View on CodeChef](https://www.codechef.com/problems/IOI2024)