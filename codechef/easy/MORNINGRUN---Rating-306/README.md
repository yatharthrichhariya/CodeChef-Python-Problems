# MORNINGRUN - Rating 306

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Morning Run

Chef wants to run  **at least**  $1000$ meters to reach his fitness goal.
There's a rectangular park nearby, with a length of $X$ meters and a width of $Y$ meters.

Can Chef complete his goal by running one loop around the park? (Loop meaning running the entire path around the edge of the park.)

### Input Format
- The only line of input will contain $2$ space-separated integers $X$ and $Y$, the length and the width of the rectangular park.
### Output Format

Print `"YES"` if Chef will be able to complete his fitness goal, otherwise print `"NO"` (without quotes).

You may print each character of the output in either uppercase or lowercase (for example, the strings `YES`, `yEs`, `yes`, and `yeS` will all be treated as identical).

### Constraints
- $1 \leq X, Y \leq 1000$
### Sample 1:
Input
Output

```
400 100

```

```
YES
```

### Explanation:

The perimeter of the ground is $(400 + 100 + 400 + 100) = 1000m$ which is sufficient to complete Chef's morning run.

### Sample 2:
Input
Output

```
300 150

```

```
NO
```

### Explanation:

The perimeter of the ground is $(300 + 150 + 300 + 150) = 900m$ which is not sufficient to complete Chef's morning run.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-23T09:48:39.562Z  

```py
X,Y=map(int,input().split())
A=X+Y+X+Y
if A>=1000:
    print("Yes")
else:
    print("No")
```

---

[View on CodeChef](https://www.codechef.com/problems/MORNINGRUN)