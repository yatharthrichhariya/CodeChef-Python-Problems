# QNOT - Rating 206

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Qualified or Not

TanMinati and Bhavy participated in the first round of a coding competition organized by the Coding Club, IIT Ropar during  **Advitiya**.

To qualify for the next round, a participant must  *defeat*   **both**  TanMinati and Bhavy.

A participant can  *defeat*  another participant by solving  **at least twice**  the number of problems as that participant.

Given that TanMinati solved $X$ problems and Bhavy solved $Y$ problems, determine whether a participant who solved $N$ problems can participate in the next round.

### Input Format
- The first and only line of input will contain three integers $N$, $X$, and $Y$, denoting the number of problems solved by the participant, TanMinati, and Bhavy respectively.
### Output Format

Output `YES` if the participant qualifies. Otherwise, output `NO`.

You may print each character of the string in either uppercase or lowercase (for example, the strings `yEs`, `yes`, `Yes` and `YES` will all be treated as identical).

### Constraints
- $1 \leq N,X,Y \leq 10$
### Sample 1:
Input
Output

```
4 2 2
```

```
YES
```

### Explanation:

We have $N = 4, X = 2, Y = 2$.

- $N \ge 2X$ means the participant defeats TanMinati.
- $N \ge 2Y$ means the participant defeats Bhavy as well.

So, the participant qualifies to the next round.

### Sample 2:
Input
Output

```
5 3 1
```

```
NO
```

### Explanation:

We have $N = 5, X = 3, Y = 2$.

- $N \lt 2X$ so TanMinati is undefeated.
- $N \ge 2Y$ means the participant defeats Bhavy.

Since TanMinati was not defeated, the participant does not qualify to the next round.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-08-31T18:29:14.648Z  

```py
N, X, Y = map(int, input().split())

if N >= 2 * X and N >= 2 * Y:
    print("YES")
else:
    print("NO")
```

---

[View on CodeChef](https://www.codechef.com/problems/QNOT)