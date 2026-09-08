# ELHP - Rating 245

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Election Hopes

The elections in Chefland have concluded, and the results are in!

Chef received $X$ votes, and his rival Chefu received $Y$.

Chef thinks he dominated the election if and only if he received  **at least double**  the number of votes Chefu received.
Did Chef dominate the election?

### Input Format
- The only line of input contains two space-separated integers $X$ and $Y$ — the number of votes received by Chef and Chefu, respectively.
### Output Format

Print a single line containing the answer: either `"Yes"` or `"No"` (without quotes), depending on whether Chef dominated the election or not.

Each letter of the output may be printed in either uppercase or lowercase, i.e, the strings `No`, `no`, `NO`, and `nO` will all be treated as equivalent.

### Constraints
- $1 \leq X, Y \leq 100$
### Sample 1:
Input
Output

```
79 40

```

```
No
```

### Explanation:

Chef received $79$ votes, and Chefu received $40$.
Twice of $40$ is $80$, and since Chef didn't receive $\geq 80$ votes, he didn't dominate the election.

### Sample 2:
Input
Output

```
28 14

```

```
Yes
```

### Explanation:

Chef received $28$ votes, and Chefu received $14$.
Twice of $14$ is $28$, and since Chef received $\geq 28$ votes, he dominated the election.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-08T14:21:24.309Z  

```py
X,Y=map(int,input().split())
if X>=Y*2:
    print("Yes")
else:
    print("No")
```

---

[View on CodeChef](https://www.codechef.com/problems/ELHP)