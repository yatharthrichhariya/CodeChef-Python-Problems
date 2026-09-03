# GLPR - Rating 219

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Glass Prices

Chef is buying spectacles, and is now deciding on which frame to purchase.

Chef has narrowed his options down to two choices: a plastic frame that costs $X$ rupees, and a metal frame that costs $Y$ rupees.

Chef will buy the metal frame  **if and only if**  it costs  *at most twice*  the price of the plastic frame - otherwise he will buy the plastic frame.

Can you decide which frame Chef will buy?

### Input Format
- The first and only line of input will contain two integers $X$ and $Y$ - the price of the plastic frame and the metal frame, respectively.
### Output Format

For each test case, output on a new line the answer: the type of frame Chef will purchase.
This is either the string `"PLASTIC"` or the string `"METAL"` (without quotes) depending on the outcome.

Each letter of the output may be printed in either uppercase or lowercase - for example, the strings `METAL`, `MeTaL`, `metal`, and `mEtAL` will all be treated as equivalent.

### Constraints
- $1 \leq X \leq 2000$
- $1 \leq Y \leq 2000$
### Sample 1:
Input
Output

```
499 999

```

```
PLASTIC

```

### Explanation:

The plastic frame costs $499$ rupees, and the metal one costs $999$ rupees.

$2\times 499 = 998$ is less than $999$, so Chef will prefer the plastic frame.

### Sample 2:
Input
Output

```
499 998

```

```
METAL

```

### Explanation:

The plastic frame costs $499$ rupees, and the metal one costs $998$ rupees.

$2\times 499 = 998$ is equal to $998$, so Chef will prefer the metal frame.

### Sample 3:
Input
Output

```
698 1099

```

```
METAL

```

### Explanation:

The plastic frame costs $698$ rupees, and the metal one costs $1099$ rupees.

$2\times 698 = 1396$ is greater than $1099$, so Chef will prefer the metal frame.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-03T10:13:53.643Z  

```py
X,Y=map(int,input().split())
if X*2==Y:
    print("METAL")
else:
    print("PLASTIC")
```

---

[View on CodeChef](https://www.codechef.com/problems/GLPR)