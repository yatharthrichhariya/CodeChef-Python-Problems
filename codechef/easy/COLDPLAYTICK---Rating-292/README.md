# COLDPLAYTICK - Rating 292

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Coldplay Tickets

You want to go to the Coldplay concert along with $N$ of your friends. You are buying tickets for everyone.

Each ticket costs $5000$ INR. Calculate the total amount you need to pay (in INR).

### Input Format
- The first and only line of input contains $N$ — the number of friends you have.
### Output Format

For each test case, output on a new line the total cost of all tickets for yourself and your friends.

### Constraints
- $1 \le N \le 5$
### Sample 1:
Input
Output

```
1

```

```
10000

```

### Explanation:

You are buying tickets for yourself and one friend of yours. Thus, the cost is $2 \cdot 5000 = 10000$.

### Sample 2:
Input
Output

```
5

```

```
30000

```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-22T09:48:09.993Z  

```py
N=int(input())
print((N*5000)+5000)
```

---

[View on CodeChef](https://www.codechef.com/problems/COLDPLAYTICK)