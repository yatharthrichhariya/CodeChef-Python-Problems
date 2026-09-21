# HEATWAVE - Rating 284

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Heat Wave

During a scorching heat wave, the temperature in a Chefland reached a record high of $X$ degrees.

The next day, the recorded temperature was $Y$ degrees. Find whether this was a new record high or not.

### Input Format
- The first and only line of input will contain two space separated integers $X$ and $Y$ denoting the highest recorded temperature and the temperature on a given day respectively.
### Output Format

Output on a new line, `YES`, if a new high was created. Otherwise print `NO`.

You may print each character of the string in uppercase or lowercase (for example, the strings `YES`, `yEs`, `yes`, and `yeS` will all be treated as identical).

### Constraints
- $100 \leq X, Y \leq 150$
### Sample 1:
Input
Output

```
135 110
```

```
NO
```

### Explanation:

The temperature recorded is $110$ which is less than the highest recorded temperature. Thus, it did not make a new high.

### Sample 2:
Input
Output

```
121 121
```

```
NO
```

### Explanation:

The temperature recorded is $121$ which is equal to the highest recorded temperature. Thus, it did not make a new high.

### Sample 3:
Input
Output

```
101 150
```

```
YES
```

### Explanation:

The temperature recorded is $150$ which is greater than the highest recorded temperature. Thus, it made a new high.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-21T12:06:50.131Z  

```py
X,Y=map(int,input().split())
if X<Y:
    print("Yes")
else:
    print("No")
```

---

[View on CodeChef](https://www.codechef.com/problems/HEATWAVE)