# INCAT - Rating 210

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Make Cat

Chef loves cats, and tries to search for them everywhere.

Today, Chef saw a string $S$ of length $3$, consisting of lowercase English letters only.
Your task is to tell Chef whether he can rearrange the letters of the string $S$ to form the word "cat".

### Input Format
- The first and only line of input contains a single string $S$ of length $3$, containing only lowercase English letters.
### Output Format

Output the answer on a single line: $\text{YES}$ if some letters of $S$ can be used to form the word "cat", and $\text{NO}$ otherwise.

Each character of the output may be printed in either uppercase or lowercase, i.e. the strings $\text{NO}, \text{No}, \text{nO},$ and $\text{no}$ will all be treated as equivalent.

### Constraints
- $S$ is a string of length $3$.
- $S$ contains only lowercase English letters, i.e. the characters 'a' through 'z'.
### Sample 1:
Input
Output

```
cat

```

```
Yes
```

### Explanation:

No rearrangement is needed: the word is already "cat".

### Sample 2:
Input
Output

```
tic

```

```
No
```

### Explanation:

It's not possible to rearrange "tic" to form "cat".

### Sample 3:
Input
Output

```
tac

```

```
Yes
```

### Explanation:

"tac" can be rearranged to form "cat".

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-08-31T18:30:28.474Z  

```py
S = input()

if sorted(S) == sorted("cat"):
    print("YES")
else:
    print("NO")

```

---

[View on CodeChef](https://www.codechef.com/problems/INCAT)