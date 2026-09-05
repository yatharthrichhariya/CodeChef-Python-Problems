# PIZZAPARTY - Rating 238

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Pizza Party

Chef is hosting a pizza party and has invited $A$ boys and $B$ girls. Don't forget to include Chef himself; he is a boy.

It is known that a boy eats $4$ slices of pizza while a girl eats $3$ slices of pizza. Further, a single pizza comes with $8$ total slices of pizza.

How many pizzas does Chef need to ensure nobody remains hungry? It is fine to waste some of the food.

### Input Format
- The first and only line of input contains $2$ integers - $A$ and $B$, the number of boys and girls invited to the party.
### Output Format

For each test case, output on a new line the number of pizzas needed.

### Constraints
- $0 \le A, B \le 100$
### Sample 1:
Input
Output

```
2 0

```

```
2

```

### Explanation:

There are $2$ other boys invited apart from Chef, so a total of $3$ boys. They need at least $12$ slices of pizza and $2$ pizzas will have $16$ slices, so it is sufficient.

### Sample 2:
Input
Output

```
0 4

```

```
2

```

### Explanation:

There is only one boy, Chef himself, and $4$ girls. They will eat a total of $16$ slices which is exactly the number of slices in $2$ pizzas.

### Sample 3:
Input
Output

```
100 100

```

```
88
```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-05T18:23:12.669Z  

```py
A, B = map(int, input().split())
if (((A + 1) * 4 + B * 3) % 8 == 0):
    print(((A + 1) * 4 + B * 3) // 8)
else:
    print(((A + 1) * 4 + B * 3) // 8 + 1)

```

---

[View on CodeChef](https://www.codechef.com/problems/PIZZAPARTY)