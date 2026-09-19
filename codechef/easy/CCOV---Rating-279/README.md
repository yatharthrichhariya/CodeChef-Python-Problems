# CCOV - Rating 279

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Overspeeding

Alice is going for a drive. During her drive, she reached a maximum speed of $S$ km/hr.

As per the rules of the government, the speed of the vehicle must  **not exceed**  $40$ km/hr, otherwise the person will be fined.

You need to tell whether Alice will be fined or not.

### Input Format
- The only line of input will contain a single integer $S$ - denoting the maximum speed Alice reached while driving.
### Output Format

Print `YES` if Alice will be fined, otherwise print `NO`.

You may print each character of the string in uppercase or lowercase (for example, the strings `YES`, `yEs`, `yes`, and `yeS` will all be treated as identical).

### Constraints
- $1 \leq S \leq 50$
### Sample 1:
Input
Output

```
40

```

```
NO

```

### Explanation:

Since Alice's speed does not exceed $40$, she will not be fined.

### Sample 2:
Input
Output

```
41

```

```
YES

```

### Explanation:

Since Alice's speed exceeds $40$, she will be fined.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-19T18:15:06.829Z  

```py
S=int(input())
if S<=40:
    print("NO")
else:
    print("YES")
```

---

[View on CodeChef](https://www.codechef.com/problems/CCOV)