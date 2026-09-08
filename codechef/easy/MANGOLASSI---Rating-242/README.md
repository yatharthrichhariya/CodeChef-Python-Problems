# MANGOLASSI - Rating 242

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Summer Time

Mamalesh likes to drink mango lassi when it's hot, and only when it's hot. If (and only if) the temperature on a given day is  **strictly greater**  than $35$ degrees, Mamalesh will drink mango lassi.

Mamalesh sees that today's temperature is $X$ degrees Celsius. Will he drink mango lassi today?
Print `"Yes"` if he will, and `"No"` otherwise (without quotes).

### Input Format
- The only line of input will contain a single integer $X$, denoting today's temperature.
### Output Format

Print `"YES"` if Mamalesh will drink mango lassi today, and `"NO"` otherwise (without quotes).

Each letter of the output may be printed in either uppercase or lowercase, i.e, the strings `NO`, `no`, `No`, and `nO` will all be treated as equivalent.

### Constraints
- $1 \leq X \leq 50$
### Sample 1:
Input
Output

```
35

```

```
NO
```

### Explanation:

Today's temperature is $35$, which is not  **strictly**  greater than $35$ degrees Celsius.
So, Mamalesh will not drink mango lassi today.

### Sample 2:
Input
Output

```
38

```

```
YES
```

### Explanation:

Today's temperature is $38$, which is greater than $35$ degrees Celsius.
So, Mamalesh will drink mango lassi today.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-08T14:09:09.074Z  

```py
X=int(input())
if X>35:
    print("Yes")
else:
    print("No")
```

---

[View on CodeChef](https://www.codechef.com/problems/MANGOLASSI)