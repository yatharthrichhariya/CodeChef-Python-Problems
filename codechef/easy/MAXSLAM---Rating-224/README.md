# MAXSLAM - Rating 224

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Maximum Slams

Chef is a professional tennis player, and his aim is to win more Grand Slams than anyone ever has!

Currently, Chef has won $X$ Grand Slams in total.
Chef needs to win  **at least**  $25$ Grand Slams in total to break the record for most total wins.

Every year, there are exactly $4$ Grand Slams. Assuming Chef is skilled enough to always win every Grand Slam, what's the minimum number of years Chef needs to break the record?

### Input Format
- The first and only line of input will contain a single integer $X$, Chef's current number of Slams.
### Output Format

For each test case, output on a new line the minimum number of years Chef needs to break the record for most Grand Slam wins.

### Constraints
- $0 \leq X \leq 24$
### Sample 1:
Input
Output

```
0

```

```
7

```

### Explanation:

Chef currently has $X = 0$ wins.
Every year, he can get $4$ wins. So, after $7$ years, he can have upto $4\times 7 = 28$ wins which is more than the $25$ he needs.
$6$ years is not enough since only $24$ wins are attainable, so the answer is $7$.

### Sample 2:
Input
Output

```
9
```

```
4
```

### Explanation:

Chef currently has $X = 9$ wins.
Four more years, each with $4$ wins, will give him another $4\times 4 = 16$ wins. That makes a total of $9 + 16 = 25$ wins, which is enough.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-04T11:48:44.236Z  

```py
X = int(input())
if (25-X)%4==0:
    print((25-X)//4)
else:
    print(((25-X)//4)+1)
```

---

[View on CodeChef](https://www.codechef.com/problems/MAXSLAM)