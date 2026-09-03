# THALA7 - Rating 235

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Thala For A Reason

You are given an integer $N$.

Print `THALA` if $N=7$, otherwise print `SADGE`.

### Input Format
- The only line of input contains an integer $N$.
### Output Format

Output a single string, print `THALA` if $N=7$, otherwise print `SADGE`.

You may print each character of the string in uppercase or lowercase (for example, the strings `THALA`, `thALa`, `thala`, and `tHalA` will all be treated as identical).

### Constraints
- $1 \leq N \leq 10$
### Sample 1:
Input
Output

```
7

```

```
THALA
```

### Explanation:

Since $N = 7$, output is `THALA`.

### Sample 2:
Input
Output

```
1

```

```
SADGE
```

### Explanation:

Since $N \neq 7$, output is `SADGE`.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-03T14:54:17.391Z  

```py
N=int(input())
if N==7:
    print("THALA")
else:
    print("SADGE")
```

---

[View on CodeChef](https://www.codechef.com/problems/THALA7)