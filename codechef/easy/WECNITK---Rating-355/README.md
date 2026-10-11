# WECNITK - Rating 355

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Access Code Equality

You are attempting to join the Web Club NITK’s exclusive online session. To do so, you need to enter the correct access code.

The correct code is `"WECNITK"` (without quotes).
The code you entered is given by the string $S$, which has length $7$.

Your task is to verify whether the entered code $S$ matches the correct code.
If it does, print `"Welcome to Web Club!"`. Otherwise, print `"Access denied"`.

### Input Format

The first and the only line of input will contain a string $S$ of length $7$, denoting the access code that was entered.

### Output Format

Print the correct output according to the access code $S$.

Each letter of the output may be printed in either uppercase or lowercase - for example the string `"AcCeSS DEniEd"` will be accepted if the correct answer is `"Access denied"`.

### Constraints
- The length of the string $S$ is exactly $7$.
- $S$ contains only uppercase and lowercase English letters, i.e. the characters 'a'-'z' and 'A'-'Z'.
### Sample 1:
Input
Output

```
WECNITK
```

```
Welcome to Web Club!
```

### Explanation:

The access code entered matches the expected one, so you are granted access.

### Sample 2:
Input
Output

```
WECnitk
```

```
Access denied
```

### Explanation:

The access code entered does not match the expected one, so you are not granted access. Note that a mismatch in uppercase/lowercase is still considered a mismatch: the code must match  **exactly**.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-11T18:03:05.451Z  

```py
S=input()
if S=="WECNITK":
    print("Welcome to web Club!")
else:
    print("Access Denied")
```

---

[View on CodeChef](https://www.codechef.com/problems/WECNITK)