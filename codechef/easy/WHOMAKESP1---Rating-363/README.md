# WHOMAKESP1 - Rating 363

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Who Makes P1

Tyro and Dom are fighting over who makes the first problem of the contest. Both of them are very lazy so they don't want to make it.

Tyro has a patience level of $A$, meaning he will only be convinced on the $A^{th}$ time when Dom asks him to make the problem.
Dom, on the other hand, has decided to convince Tyro  **at most**  $B$ times. If Tyro is not convinced by the $B^{th}$ time, Dom will proceed to make it himself.

Given the values of $A$ and $B$, find out who will end up making the problem.

### Input Format
- The first and only line of input contains $2$ integers, $A$ and $B$ - Tyro's patience level, and the number of times Dom tries to convince Tyro respectively.
### Output Format

For each test case, output on a new line, `Dom` or `Tyro` corresponding to who ends up making the problem.

You can print each character in uppercase or lowercase. For example, the strings `DOM`, `dom`, `Dom`, and `dOM` are considered identical.

### Constraints
- $1 \le A, B \le 10$
### Sample 1:
Input
Output

```
5 5

```

```
Tyro
```

### Explanation:

Dom will convince Tyro for at most $5$ times. Tyro agrees on the $5^{th}$ time and makes the problem.

### Sample 2:
Input
Output

```
4 3

```

```
Dom
```

### Explanation:

Dom will convince Tyro for at most $3$ times. However, Tyro has decided to agree on the $4^{th}$ time. Thus, Dom makes the problem.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-13T10:48:06.626Z  

```py
A,B=map(int,input().split())
if A<=B:
    print("Tyro")
else:
    print("Dom")
```

---

[View on CodeChef](https://www.codechef.com/problems/WHOMAKESP1)