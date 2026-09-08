# ACPLZ - Rating 245

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### AC Please

Chef is feeling the heat this summer and wants to switch on the Air Conditioning all the time, but since he doesn't want to harm the environment much, he only switches it on when the room temperature is  **strictly greater**  than $30$ degrees celsius.

Given the room temperature, you need to find whether Chef will switch on the air conditioning or not.

### Input Format
- The only line of input will contain a single integer $T$ - denoting the room temperature.
### Output Format

Print `YES` if Chef will turn the Air Conditioning on, otherwise print `NO`.

You may print each character of the string in uppercase or lowercase (for example, the strings YES, yEs, yes, and yeS will all be treated as identical).

### Constraints
- $1 \leq T \leq 50$
### Sample 1:
Input
Output

```
30

```

```
NO
```

### Explanation:

Since the temperature is not more than $30$ degrees Celsius Chef won't turn on the Air Conditioning.

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

Since the temperature is more than $30$ degrees Celsius Chef will turn on the Air Conditioning.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-08T14:18:26.747Z  

```py
T=int(input())
if T>30:
    print("Yes")
else:
    print("No")
```

---

[View on CodeChef](https://www.codechef.com/problems/ACPLZ)