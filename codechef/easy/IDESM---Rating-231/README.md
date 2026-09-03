# IDESM - Rating 231

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### The Ides of March

 *Beware the ides of March.* 

Julius Caesar was warned by a soothsayer to be wary of the ides of March — namely, the $15$-th of March.

Today is the $N$-th day of March. Your task is to tell Caesar whether it is the ides of March, so that he can take extra safety precautions if necessary.

### Input Format

The only line of input will contain a single integer $N$, today's date in March.

### Output Format

Print `"Yes"` if today is the ides of March, and `"No"` otherwise (without quotes).

Each letter of the output may be printed in either uppercase or lowercase, i.e, the strings `NO`, `no`, `nO`, and `No` will all be treated as equivalent.

### Constraints
- $1 \leq N \leq 15$
### Sample 1:
Input
Output

```
14
```

```
No
```

### Explanation:

The $14$-th of March is not the ides of March, so Caesar doesn't need to take any extra care.

### Sample 2:
Input
Output

```
15
```

```
Yes
```

### Explanation:

$15$-th is the ides of March, so Caesar should take extra safety precautions.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-03T14:40:38.504Z  

```py
N=int(input())
if N == 15:
    print("Yes")
else:
    print("No")
```

---

[View on CodeChef](https://www.codechef.com/problems/IDESM)