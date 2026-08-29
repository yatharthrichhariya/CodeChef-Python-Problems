# FONTA - Rating 193

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Fonta

A drink is called  *fanta-like*  if the last three letters of its name are $\tt{'n'}, \tt{'t'},$ and $\tt{'a'}$, in that order.
That is, the name of the drink must end with `nta`.

You bought a drink from a vending machine.
The name of the drink is represented by the string $S$.
It is guaranteed that $S$ consists of  **exactly $5$**  lowercase English letters.

Is the drink  *fanta-like* ?

### Input Format
- The first and only line of input contains a single string $S$ of length $5$, denoting the name of the drink you bought.
### Output Format

Print the answer: $\tt{YES}$ if the drink is  *fanta-like*, and $\tt{NO}$ otherwise.

Each character of the output may be printed in either uppercase or lowercase, i.e. the strings $\tt{NO}, \tt{nO}, \tt{No},$ and $\tt{no}$ will all be treated as equivalent.

### Constraints
- $S$ consists of exactly $5$ lowercase English letters.
### Sample 1:
Input
Output

```
fonta

```

```
Yes
```

### Explanation:

The last three letters of $\tt{"fonta"}$ are `nta`, so it is  *fanta-like*.

### Sample 2:
Input
Output

```
pasta

```

```
No
```

### Explanation:

The last three letters of $\tt{"pasta"}$ are `sta`, so it is not  *fanta-like*.

### Sample 3:
Input
Output

```
plant

```

```
No
```

### Explanation:

The last three letters of $\tt{"plant"}$ are `ant`, so it is not  *fanta-like*.
Note that even though it has the three letters `n`, `t`, and `a`, they are not in the correct order.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-08-29T07:32:56.369Z  

```py
S=input()
if S[-3:]=='nta':
    print("Yes")
else:
    print("No")
```

---

[View on CodeChef](https://www.codechef.com/problems/FONTA)