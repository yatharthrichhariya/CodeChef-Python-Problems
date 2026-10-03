# PODIUM - Rating 341

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Podium Finish

Chef got his dream seat in `F1` and secured a $3^{rd}$ place in his debut race. He now wants to know the time gap between him and the winner of the race.

You are his chief engineer and you only know the time gap between Chef and the runner up of the race, given as $A$ seconds, and the time gap between the runner up and the winner of the race, given as $B$ seconds.

Please calculate and inform Chef about the time gap between him and the winner of the race.

### Input Format
- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of a single line of input containing two space-separated integers $A$ and $B$ denoting the time gap between Chef and the runner up and the time gap between the runner up and the winner respectively.
### Output Format

For each test case, output the time gap between Chef and the winner of the race.

### Constraints
- $1 \leq T \leq 100$
- $1 \leq A, B \leq 10$
### Sample 1:
Input
Output

```
4
1 1
2 5
3 2
5 6

```

```
2
7
5
11

```

### Explanation:

 **Test case $1$:**  The time gap between Chef and runner up is $1$ second. The time gap between runner up and the winner is $1$ second. Thus, the time gap between Chef and the winner is $1+1=2$ seconds.

 **Test case $2$:**  The time gap between Chef and runner up is $2$ seconds. The time gap between runner up and the winner is $5$ second. Thus, the time gap between Chef and the winner is $2+5=7$ seconds.

 **Test case $3$:**  The time gap between Chef and runner up is $3$ seconds. The time gap between runner up and the winner is $2$ second. Thus, the time gap between Chef and the winner is $3+2=5$ seconds.

 **Test case $4$:**  The time gap between Chef and runner up is $5$ seconds. The time gap between runner up and the winner is $6$ second. Thus, the time gap between Chef and the winner is $5+6=11$ seconds.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-03T10:38:24.498Z  

```py
T=int(input())
for i in range(T):
    A,B=map(int,input().split())
    print(A+B)
```

---

[View on CodeChef](https://www.codechef.com/problems/PODIUM)