# YOGADAY - Rating 264

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Yoga Day

Surya Namaskar, also known as Sun Salutation, is a series of $12$ yoga poses performed in a sequence.

Chef repeats this sequence of yoga poses multiple times during his session.

Given that Chef has performed $N$ yoga poses, find the number of rounds of Surya Namaskar he completed during the session.

### Input Format

The input will contain a single integer $N$, denoting the number of yoga poses Chef performed during his session.

### Output Format

Output the number of rounds of Surya Namaskar Chef completed during the session.

### Constraints
- $1 \leq N \leq 100$
### Sample 1:
Input
Output

```
55

```

```
4

```

### Explanation:

Chef completed $4$ rounds of Surya Namaskar comprising of $4\cdot 12 = 48$ yoga poses.
The fifth round was incomplete since Chef performed only $7$ poses in that round.

### Sample 2:
Input
Output

```
11
```

```
0
```

### Explanation:

Chef performed $11$ yoga poses whereas each Surya Namaskar consists of $12$ poses. Thus, he did not complete even $1$ round of Surya Namaskar.

### Sample 3:
Input
Output

```
24
```

```
2
```

### Explanation:

Since Chef performed $24$ yoga poses and each Surya Namaskar consists of $12$ poses, he completed $2$ rounds of Surya Namaskar.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-11T08:46:55.315Z  

```py
N=int(input())
print(N//12)
```

---

[View on CodeChef](https://www.codechef.com/problems/YOGADAY)