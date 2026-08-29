# SSNK - Rating 196

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Snaky Strings

Chef calls a string  *snaky*  if it either starts or ends with the letter `'s'`.

You are given a string $A$ of length $4$, consisting of only lowercase English letters.
Is the string $A$  *snaky* ?

### Input Format
- The only line of input contains a string $A$ of length $4$, containing only lowercase English letters.
### Output Format

Output a string denoting the answer: `Yes` if the string $A$ is  *snaky*  and `No` otherwise.

Each character of the output may be printed in either uppercase or lowercase, i.e. the strings `NO`, `No`, `nO`, and `no` will be treated as equivalent.

### Constraints
- $A$ has length $4$.
- Every character of $A$ is a lowercase English letter, i.e. one of $\{\tt{a}, \tt{b}, \ldots, \tt{z}\}$.
### Sample 1:
Input
Output

```
hiss

```

```
Yes
```

### Explanation:

The string `"hiss"` ends with the letter `'s'`, so it is  *snaky*.

### Sample 2:
Input
Output

```
rock

```

```
No
```

### Explanation:

The string `"rock"` neither starts nor ends with the letter `'s'`, so it is not  *snaky*.

### Sample 3:
Input
Output

```
snow

```

```
Yes
```

### Explanation:

The string `"snow"` starts with the letter `'s'`, so it is  *snaky*.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-08-29T07:46:21.639Z  

```py
A=input()
if A[-1]=="s":
    print("Yes")
elif A[0]=="s":
    print("Yes")
else:
    print("No")

```

---

[View on CodeChef](https://www.codechef.com/problems/SSNK)