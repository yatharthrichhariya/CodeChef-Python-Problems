# EXUNPIZZA - Rating 173

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Exun and the Pizzas

The Exunites are preparing for the $2025$ edition of their annual event, Exun!

After a long day of work, they go to the canteen to buy refreshments.
At the canteen, Chef is selling $N$ pizzas. However, the Exunites only require $K$ pizzas.

Each pizza costs $R$ rupees.
Chef wants to know: after selling $K$ pizzas to the Exunites, how much revenue can he obtain by selling all his remaining pizzas?

### Input Format

The first and only line of input contains $3$ space-separated integers $N, K,$ and $R$ — the number of pizzas Chef is selling, the number of pizzas required by the Exunites, and the cost of each pizza.

### Output Format

Print a single integer — the amount of money (in Rupees) Chef's remaining pizzas can sell for.

### Constraints
- $1 \leq K \leq N \leq 100$
- $1 \leq R \leq 100$
### Sample 1:
Input
Output

```
10 6 15
```

```
60
```

### Explanation:

Chef has $10$ pizzas, the Exunites buy $6$ of the pizzas so he has $10 - 6 = 4$ pizzas left.
Each of these pizzas sell for $15$ rupees, so the total revenue from selling all of the remaining pizzas is $4 \cdot 15 = 60$ rupees.

### Sample 2:
Input
Output

```
25 18 20

```

```
140
```

### Explanation:

Chef has $25$ pizzas, the Exunites buy $18$ of the pizzas so he has $25 - 18 = 7$ pizzas left.
Each of these pizzas sell for $20$ rupees, so the total revenue from selling all of the remaining pizzas is $7 \cdot 20 = 140$ rupees.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-08-26T17:47:49.822Z  

```py
N,K,R=map(int,input().split())
print((N-K)*R)
```

---

[View on CodeChef](https://www.codechef.com/problems/EXUNPIZZA)