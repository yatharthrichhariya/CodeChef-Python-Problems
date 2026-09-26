# NEIREM - Rating 319

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Remaining Neighborhoods

As elections approach the country of Chefland, Chef's campaign is in full swing.

Chef's city has exactly $100$ neighborhoods.
Chef has already visited $N$ of them to canvass for votes, and he won't stop till he's visited every last one of them!

How many more neighborhoods does Chef need to visit?

### Input Format

The only line of input will contain a single integer $N$, the number of neighborhoods Chef has already visited.

### Output Format

Print a single integer: the number of neighborhoods Chef still needs to visit.

### Constraints
- $0 \leq N \leq 100$
### Sample 1:
Input
Output

```
78
```

```
22
```

### Explanation:

Chef has visited $78$ out of the $100$ neighborhoods. That leaves $22$ more for him to visit.

### Sample 2:
Input
Output

```
100
```

```
0
```

### Explanation:

Chef has visited every neighborhood already.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-26T11:35:10.525Z  

```py
N=int(input())
print(100-N)
```

---

[View on CodeChef](https://www.codechef.com/problems/NEIREM)