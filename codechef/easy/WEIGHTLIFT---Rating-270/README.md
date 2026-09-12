# WEIGHTLIFT - Rating 270

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Weightlifting

Chef, being an international powerlifter, has participated in a powerlifting competition.

The competition consists of three rounds, i.e., squat, bench press, and, deadlift. In each round, the goal is to lift maximum weight, and Chef gets two attempts to do that.

For each round, the score of best attempt is taken into consideration and the total score is calculated as the sum of scores of all rounds.

You are given Chef's score in both attempts of rounds $1, 2,$ and $3,$ as $A_1, A_2, B_1, B_2, C_1,$ and $C_2$ respectively. Find the value of Chef's total score in the competition.

### Input Format

The first and only line of input consists of $6$ space separated integers $A_1, A_2, B_1, B_2, C_1, C_2$, denoting Chef's score in both attempts of round $1, 2,$ and $3$ respectively.

### Output Format

Output a single integer denoting Chef's total score in the competition.

### Constraints
- $200 \leq A_1, A_2, B_1, B_2, C_1, C_2 \leq 300$
### Sample 1:
Input
Output

```
250 240 205 217 296 299

```

```
766
```

### Explanation:

Chef's score in each round:

- In round $1$, he scored $250$ and $240$ in both attempts. Thus, the score under consideration would be $250$.
- In round $2$, he scored $205$ and $217$ in both attempts. Thus, the score under consideration would be $217$.
- In round $3$, he scored $296$ and $299$ in both attempts. Thus, the score under consideration would be $299$.

Chef's total score in competition is $250+217+299 = 766$.

### Sample 2:
Input
Output

```
207 220 200 200 300 289

```

```
720
```

### Explanation:

Chef's score in each round:

- In round $1$, he scored $207$ and $220$ in both attempts. Thus, the score under consideration would be $220$.
- In round $2$, he scored $200$ in both attempts. Thus, the score under consideration would be $200$.
- In round $3$, he scored $300$ and $289$ in both attempts. Thus, the score under consideration would be $300$.

Chef's total score in competition is $220+200+300 = 720$.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-12T14:12:12.168Z  

```py
A1,A2,B1,B2,C1,C2=map(int,input().split())
A=max(A1,A2)
B=max(B1,B2)
C=max(C1,C2)
print(A+B+C)
```

---

[View on CodeChef](https://www.codechef.com/problems/WEIGHTLIFT)