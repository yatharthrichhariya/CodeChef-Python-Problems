# ELECTION1 - Rating 241

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Election

Chef's party is contesting an election with $N$ total seats. It has won $K$ seats.

A party can form the government only if it has a strict majority, i.e. at least $\left\lfloor \frac{N}{2} \right\rfloor + 1$ seats.

Chef's party may form a coalition with other parties to get additional seats.

Find the minimum number of additional seats Chef's party needs to form the government.

### Input Format

The input consists of two space-separated integers $N$ and $K$ — the total number of seats and the number of seats that Chef's party has won.

### Output Format

Output a single integer — the minimum number of additional seats required.

### Constraints
- $1 \leq N \leq 500$
- $0 \leq K \leq N$
### Sample 1:
Input
Output

```
234 108
```

```
10
```

### Explanation:

Chef needs $118$ seats to win, he has $108$ seats currently. Therefore, he needs $10$ more.

### Sample 2:
Input
Output

```
293 207
```

```
0
```

### Explanation:

Chef's party already has a majority.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-07T18:20:00.590Z  

```py
N,K=map(int,input().split())
A=(N//2)+1
print(max(0,A-K))
```

---

[View on CodeChef](https://www.codechef.com/problems/ELECTION1)