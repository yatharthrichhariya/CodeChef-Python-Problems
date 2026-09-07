# DEVDON - Rating 241

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Devouring Donuts

Chef baked a full tray of donuts, but couldn't resist and ate them all!

The tray had $X$ donuts, and each donut contains $Y$ calories.
How many calories did Chef consume in total?

### Input Format

The only line of input contains two space-separated integers $X$ and $Y$ - the number of donuts and the calorie count of each one.

### Output Format

Print a single integer: the total number of calories consumed by Chef.

### Constraints
- $1 \leq X \leq 10$
- $200 \leq Y \leq 300$
### Sample 1:
Input
Output

```
2 280
```

```
560
```

### Explanation:

Chef ate two donuts, each containing $280$ calories. The total number of calories is thus $280 + 280 = 560$.

### Sample 2:
Input
Output

```
6 237
```

```
1422
```

### Explanation:

Chef ate six donuts, each containing $237$ calories. The total number of calories is thus $6\cdot 237 = 1422$.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-07T18:09:54.088Z  

```py
X,Y=map(int,input().split())
print(X*Y)
```

---

[View on CodeChef](https://www.codechef.com/problems/DEVDON)