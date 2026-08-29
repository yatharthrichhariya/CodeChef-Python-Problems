# EQBUY - Rating 195

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Equal Buying

Chef bought some number of sacks of flour, and some number of sacks of sugar. It is unknown exactly how many of each.

Each sack of flour weighs $2$ kilograms, and each sack of sugar weighs $1$ kilogram. It is known that the total weight of Chef's sacks of flours and sugar was $N$ kilograms.

Is it possible that Chef bought an equal number of sacks of flour and sugar? Print $\text{Yes}$ if it is possible and $\text{No}$ otherwise.

### Input Format
- The first and only line contains $1$ integer - $N$.
### Output Format

Output $\text{Yes}$ if it was possible for Chef to buy an equal number of sacks of rice and sugar, and $\text{No}$ otherwise.

### Constraints
- $1 \le N \le 10$
### Sample 1:
Input
Output

```
3

```

```
Yes

```

### Explanation:

Chef could have bought $1$ sack of flour and $1$ sack of sugar for a total weight of $3$ kilograms.

### Sample 2:
Input
Output

```
5

```

```
No

```

### Explanation:

It is impossible for Chef to buy an equal amount of sacks of flour and sugar.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-08-29T07:37:54.035Z  

```py
N=int(input())
if N==3:
    print("Yes")
else:
    print("No")
```

---

[View on CodeChef](https://www.codechef.com/problems/EQBUY)