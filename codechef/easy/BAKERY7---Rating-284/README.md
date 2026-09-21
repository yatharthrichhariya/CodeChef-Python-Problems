# BAKERY7 - Rating 284

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Bakery Problem

For today, Chef is out of town, and his evil son has taken over his bakery.

Normally, Chef sells his cakes for $100$ rupees each. However, his son can be bribed with $K$ rupees, to sell each cake for $60$ rupees instead. Note that you have to pay this bribe only one time, not for each cake.

You want to buy $N$ cakes from the bakery. You can choose whether to bribe Chef's son or not. What is the minimum cost of buying the $N$ cakes.

### Input Format
- The first and only line contains $2$ integers - $N$ and $K$, the number of cakes you need to buy, and the bribe amount.
### Output Format

Output the minimum total cost of buying the $N$ cakes.

### Constraints
- $1 \le N \le 10$
- $100 \le K \le 1000$
### Sample 1:
Input
Output

```
5 100

```

```
400
```

### Explanation:

Optimal is to bribe Chef's son for $100$ rupees, and then pay $60 \cdot 5 = 300$ rupees for the $5$ cakes.

### Sample 2:
Input
Output

```
2 100

```

```
200
```

### Explanation:

Here it is optimal to just buy the cakes normally without bribing.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-21T12:15:23.891Z  

```py
N,K=map(int,input().split())
A=(60*N)+K
B=N*100
if A>B:
    print(B)
else:
    print(A)
```

---

[View on CodeChef](https://www.codechef.com/problems/BAKERY7)