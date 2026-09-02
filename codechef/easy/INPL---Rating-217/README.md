# INPL - Rating 217

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### IPL

Chef has already prepared dinner, and it's his favorite time of the day. It's time for a fantastic cricket match tonight.

If the number of runs scored in an over is  **at least**  7, Chef cheers "THALA"; otherwise, he cheers "BOOM".

You are given $X$, the number of runs scored in the over.

- If $X$ is at least $7$, print THALA.
- Otherwise, print BOOM.
### Input Format
- A single integer $X$, representing number of runs scored in an over.
### Output Format
- Print THALA if number of runs scored in the over is at least $7$, otherwise print BOOM.

You may print each character of the string in uppercase or lowercase (for example, the strings `thALa`, `thala`, `Thala`, and `thalA` will all be treated as identical).

### Constraints
- $1 \leq X \leq 36$
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
- Since the number of runs scored is at least $7$, the chef cheers out "THALA".
### Sample 2:
Input
Output

```
4

```

```
BOOM

```

### Explanation:
- Since the number of runs scored is less than $7$, the chef cheers out "BOOM".

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-02T11:45:45.251Z  

```py
X=int(input())
if X>=7:
    print("THALA")
else:
    print("BOOM")
```

---

[View on CodeChef](https://www.codechef.com/problems/INPL)