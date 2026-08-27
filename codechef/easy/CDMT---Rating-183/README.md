# CDMT - Rating 183

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### CodeMat

 **Code-mat**  is an annual programming competition organized by the  **Mathematics and Computing Society (MACS)**  at  **IIT BHU**. Last year, the event had $X$ participants, while this year it attracted $Y$ participants. Determine whether this year's event was more successful by checking if $Y$ is greater than $X$. If it was more successful, print Yes. Otherwise, print No.

### Input Format

The input consists of two space-separated integers $X$ and $Y$, where:

- $X$ denotes the number of participants last year.
- $Y$ denotes the number of participants this year.
### Output Format

Print `YES` if this year's event had more participants than last year, otherwise print `NO`.

You may print each character of the string in uppercase or lowercase (for example, the strings `YES`, `yEs`, `yes`, and `yeS` will all be treated as identical).

### Constraints
- $1 \leq X \leq 1000$
- $1 \leq Y \leq 1000$
### Sample 1:
Input
Output

```
234 643
```

```
Yes
```

### Explanation:

Since this year's event attracted more participants and was more successful, so the answer is `Yes`.

### Sample 2:
Input
Output

```
976 899
```

```
No
```

### Explanation:

Since fewer participants attended this year compared to last year, so the answer is `No`.

### Sample 3:
Input
Output

```
250 250
```

```
No
```

### Explanation:

This year's event was not more successful than the previous year, as the number of participants remained the same. So, the answer is `No`.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-08-27T18:05:17.150Z  

```py
X,Y=map(int,input().split())
if X>Y:
    print("No")
else:
    print("Yes")
```

---

[View on CodeChef](https://www.codechef.com/problems/CDMT)