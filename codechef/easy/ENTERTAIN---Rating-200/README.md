# ENTERTAIN - Rating 200

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Entertainments

Chef is trying to entertain $N$ children. He has $2$ options:

- Buy a single television for all the children to watch. This will cost $1000$ rupees.
- Buy $N$ toys, one for each child. This will cost $200$ rupees for each toy.

What is the minimum cost Chef needs to pay to entertain all the children?

### Input Format
- The first and only line of input contains a single integer $N$ - the number of children.
### Output Format

Output the cost to entertain all children.

### Constraints
- $1 \le N \le 10$
### Sample 1:
Input
Output

```
1

```

```
200
```

### Explanation:

Chef can buy $1$ toy for the only child and spend $200$ rupees. This is cheaper than buying a television for $1000$ rupees.

### Sample 2:
Input
Output

```
10

```

```
1000

```

### Explanation:

Chef can buy a television for all $10$ children to watch. This is cheaper than buying $10$ individual toys costing $2000$ rupees.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-08-30T16:59:02.883Z  

```py
N = int(input())

if N < 5:
    print(N * 200)
else:
    print(1000)
```

---

[View on CodeChef](https://www.codechef.com/problems/ENTERTAIN)