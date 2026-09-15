# GPCK - Rating 263

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Gift Packs

Chef is preparing gifts for a school event. He has $A$ notebooks and $B$ pens.

Each gift pack must contain  **one notebook and one pen**. Each item can be used in only one pack.

Find the  **maximum number of complete gift packs**  Chef can prepare.

### Input Format

The only line contains two integers $A$ and $B$ — the number of notebooks and pens.

### Output Format

Print a single integer — the maximum number of complete gift packs.

### Constraints
- $0 \le A,B \le 1000$
### Sample 1:
Input
Output

```
5 3
```

```
3
```

### Explanation:

Chef can prepare $3$ gift packs using $3$ notebooks and all $3$ pens. The remaining $2$ notebooks cannot form another complete pack.

### Sample 2:
Input
Output

```
2 6
```

```
2
```

### Explanation:

Chef has only $2$ notebooks, so he can prepare at most $2$ gift packs.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-15T18:12:09.248Z  

```py
A,B=map(int,input().split())
print(min(A,B))
```

---

[View on CodeChef](https://www.codechef.com/problems/GPCK)