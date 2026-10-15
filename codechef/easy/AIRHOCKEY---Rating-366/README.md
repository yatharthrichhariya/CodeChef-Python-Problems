# AIRHOCKEY - Rating 366

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Air Hockey

Alice is playing Air Hockey with Bob. The first person to earn seven points wins the match. Currently, Alice's score is $A$ and Bob's score is $B$.

Charlie is eagerly waiting for his turn. Help Charlie by calculating the minimum number of points that will be further scored in the match before it ends.

### Input Format
- The first line of input will contain an integer $T$ — the number of test cases. The description of $T$ test cases follows.
- The first and only line of each test case contains two space-separated integers $A$ and $B$, as described in the problem statement.
### Output Format

For each test case, output on a new line the minimum number of points that will be further scored in the match before it ends.

### Constraints
- $1 \leq T \leq 50$
- $0 \leq A, B \leq 6$
### Sample 1:
Input
Output

```
4
0 0
2 5
5 2
4 3
```

```
7
2
2
3

```

### Explanation:

 **Test case $1$:**  The current score is $0-0$. If either Alice or Bob scores $7$ consecutive points, then the score will become $7-0$ or $0-7$ respectively, and the game will end. It can be proven that at least $7$ points will be further scored in the match before it ends.

 **Test case $2$:**  The current score is $2-5$. If Bob scores $2$ consecutive points, then the score will become $2-7$ and the game will end. It can be proven that at least $2$ points will be further scored in the match before it ends.

 **Test case $3$:**  The current score is $5-2$. If Alice scores $2$ consecutive points, then the score will become $7-2$ and the game will end. It can be proven that at least $2$ points will be further scored in the match before it ends.

 **Test case $4$:**  The current score is $4-3$. If Alice scores $3$ consecutive points, then the score will become $7-3$ and the game will end. It can be proven that at least $3$ points will be further scored in the match before it ends.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-15T18:19:41.211Z  

```py
T=int(input())
for i in range(T):
    A,B=map(int,input().split())
    if A<B:
        print(A)
    elif A==B:
        print(7)
    else:
        print(B)
```

---

[View on CodeChef](https://www.codechef.com/problems/AIRHOCKEY)