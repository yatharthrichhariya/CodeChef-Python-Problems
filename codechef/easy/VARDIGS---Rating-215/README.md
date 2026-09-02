# VARDIGS - Rating 215

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Varied Digits

A $2$-digit integer is called  *varied*  if it contains two  **different**  digits.

You are given a $2$-digit integer $X$. Decide if $X$ is  *varied*  or not.

### Input Format
- The only line of input will contain a single $2$-digit integer, $X$.
### Output Format

Output the string `Yes` if $X$ is  *varied*  and `No` otherwise.

Each character of the output can be printed in either uppercase or lowercase, i.e. the strings `NO`, `No`, `nO`, and `no` will be considered equivalent.

### Constraints
- $10 \le X \le 99$
### Sample 1:
Input
Output

```
22

```

```
No
```

### Explanation:

$22$ has two equal digits $2$ and $2$, so it's not  *varied*.

### Sample 2:
Input
Output

```
48

```

```
Yes
```

### Explanation:

$48$ has two different digits $4$ and $8$, so it is  *varied*.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-02T11:32:14.696Z  

```py
A=int(input())
if A%11==0:
    print("No")
else:
    print("Yes")
```

---

[View on CodeChef](https://www.codechef.com/problems/VARDIGS)