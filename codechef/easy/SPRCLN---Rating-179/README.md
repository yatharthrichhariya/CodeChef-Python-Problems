# SPRCLN - Rating 179

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Spring Cleaning

Chef is now performing a thorough cleaning of every room in his house.

Chef's house has $X$ small rooms and $Y$ large rooms.
Each small room requires $30$ minutes to clean, and each large room requires $60$ minutes.

How many minutes does Chef need to clean his entire house?

### Input Format
- The only line of input contains two space-separated integers $X$ and $Y$ — the number of small and large rooms in Chef's house, respectively.
### Output Format

Output a single integer: the number of minutes Chef requires to clean his house.

### Constraints
- $1 \le X, Y \le 10$
### Sample 1:
Input
Output

```
4 3

```

```
300
```

### Explanation:

There are $4$ small rooms, each needing $30$ minutes to clean. The total time needed for the small rooms is hence $4\times 30 = 120$ minutes.
There are $3$ large rooms, each needing $60$ minutes to clean. The total time needed for the large rooms is hence $3\times 60 = 180$ minutes.
The total time needed for all rooms is $120 + 180 = 300$ minutes.

### Sample 2:
Input
Output

```
2 10

```

```
660
```

### Explanation:

There are $2$ small rooms, each needing $30$ minutes to clean. The total time needed for the small rooms is hence $2\times 30 = 60$ minutes.
There are $10$ large rooms, each needing $60$ minutes to clean. The total time needed for the large rooms is hence $10\times 60 = 600$ minutes.
The total time needed for all rooms is $60 + 600 = 660$ minutes.

### Sample 3:
Input
Output

```
7 3

```

```
390
```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-08-26T18:25:31.419Z  

```py
X,Y=map(int,input().split())
print((X*30)+(Y*60))

```

---

[View on CodeChef](https://www.codechef.com/problems/SPRCLN)