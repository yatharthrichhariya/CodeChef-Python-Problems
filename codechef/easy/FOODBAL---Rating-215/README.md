# FOODBAL - Rating 215

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Food Balance

Chef is preparing to cook his dinner.

There are two dishes Chef can make. The first one contains $F_1$ grams of fat and $P_1$ grams of protein, while the second contains $F_2$ grams of fat and $P_2$ grams of protein.

Chef would like the quantity of fats and proteins he consumes to be as close to each other as possible, i.e., the absolute difference between the amount of fats and proteins should be as small as possible.

Help Chef by telling him which dish he'll choose; or if both dishes have the same difference.

### Input Format
- The first and only line of input contains four space-separated integers $F_1, P_1, F_2,$ and $P_2$ — the quantities of fat and protein in the first dish and second dish, respectively.
### Output Format

Output a single string:

- "First" (without quotes) if Chef will choose the first dish.
- "Second" (without quotes) if Chef will choose the second dish.
- "Both" (without quotes) if both dishes are equivalent.

Each character of the output may be in either uppercase or lowercase, i.e. if the answer is `Both`, then any of the strings `BOTH`, `both`, `Both`, `bOTh`, and so on will be accepted.

### Constraints
- $1 \leq F_1, P_1, F_2, P_2 \leq 100$
### Sample 1:
Input
Output

```
30 40 35 44

```

```
Second
```

### Explanation:

The first dish has a difference of $|30 - 40| = 10$ between its fats and proteins, while the second dish has a difference of $|35 - 44| = 9$.
Chef will choose the second dish, since it has a smaller difference.

### Sample 2:
Input
Output

```
1 100 100 1

```

```
Both
```

### Explanation:

The first dish has a difference of $|1 - 100| = 99$ between its fats and proteins, while the second dish has a difference of $|100 - 1| = 99$.
Both dishes have the same difference.

### Sample 3:
Input
Output

```
58 56 38 52
```

```
First
```

### Explanation:

The first dish has a difference of $|58 - 56| = 2$ between its fats and proteins, while the second dish has a difference of $|38 - 52| = 14$.
Chef will choose the first dish, since it has a smaller difference.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-01T18:01:59.813Z  

```py
F1,P1,F2,P2=map(int,input().split())
if F1-P1 > F2-P2:
    print("First")
elif F1-P1 < F2-P2:
    print("Second")
else:
    print('Both')
```

---

[View on CodeChef](https://www.codechef.com/problems/FOODBAL)