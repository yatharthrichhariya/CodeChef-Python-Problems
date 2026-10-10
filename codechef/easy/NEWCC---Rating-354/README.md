# NEWCC - Rating 354

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### All New CodeChef

 *CodeChef has just finished migrating to a new judging system.* 

Chef would like to test the performance of the new judging system.

Chef has some code for an older task, which he knows ran in $X$ milliseconds on the old judging server.
On resubmitting the code to the new judging server, it ran in $Y$ milliseconds.

Which judging system is faster?

### Input Format
- The only line of input will contain two space-separated integers $X$ and $Y$ — the runtime on the old judging system, and the runtime on the new judging system.
### Output Format

Print:

- Old, if the older judging system is faster
- New, if the new judging system is faster
- Same, if they're equally fast

Each letter of the output may be printed in either uppercase or lowercase, i.e, the strings `Old`, `OlD`, `old`, `oLD` will all be treated as equivalent.

### Constraints
- $1 \leq X, Y \leq 3000$
### Sample 1:
Input
Output

```
255 230
```

```
New
```

### Explanation:

The code ran in $255$ ms on the old judging system, and $230$ ms on the new one.
The new one is faster.

### Sample 2:
Input
Output

```
1045 1309
```

```
Old
```

### Explanation:

The code ran in $1045$ ms on the old judging system, and $1309$ ms on the new one.
The old one is faster.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-10T18:02:46.572Z  

```py
X,Y=map(int,input().split())
if X<Y:
    print('Old')
elif X>Y:
    print("New")
else:
    print("Same")
```

---

[View on CodeChef](https://www.codechef.com/problems/NEWCC)