# EQUALDIST - Rating 330

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Equal Distribution

Alice and Bob are very good friends and they always distribute all the eatables equally among themselves.

Alice has $A$ chocolates and Bob has $B$ chocolates. Determine whether Alice and Bob can distribute  **all**  the chocolates  **equally**  among themselves.

Note that:

- It is not allowed to break a chocolate into more than one piece.
- No chocolate shall be left in the distribution.
### Input Format
- The first line of input will contain an integer $T$ — the number of test cases. The description of $T$ test cases follows.
- The first and only line of each test case contains two space-separated integers $A$ and $B$, the number of chocolates that Alice and Bob have, respectively.
### Output Format

For each test case, output on a new line $\texttt{YES}$ if Alice and Bob can distribute all the chocolates equally, else output $\texttt{NO}$. The output is case insensitive, i.e, $\texttt{yes}$, $\texttt{YeS}$, $\texttt{yES}$ will all be accepted as correct answers when Alice and Bob can distribute the chocolates equally.

### Constraints
- $1 \leq T \leq 1000$
- $1 \leq A, B \leq 10^5$
### Sample 1:
Input
Output

```
4
1 1
1 3
1 2
1 4

```

```
YES
YES
NO
NO

```

### Explanation:

 **Test case $1$** : Both Alice and Bob already have equal number of chocolates, hence it is possible to distribute the chocolates equally among Alice and Bob.

 **Test case $2$** : If Bob gives one of his chocolates to Alice, then both of them will have equal number of chocolates, i.e. $2$. So, it is possible to distribute the chocolates equally among Alice and Bob.

 **Test case $3$** : There are total $3$ chocolates. These chocolates cannot be divided equally among Alice and Bob.

 **Test case $4$** : Alice and Bob cannot have equal number of chocolates, no matter how they distribute the chocolates.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-29T11:42:02.996Z  

```py
T=int(input())
for i in range(T):
    A,B=map(int,input().split())
    if A<B and B+A==B and A:
        print("Yes")
    else:
        print("No")
```

---

[View on CodeChef](https://www.codechef.com/problems/EQUALDIST)