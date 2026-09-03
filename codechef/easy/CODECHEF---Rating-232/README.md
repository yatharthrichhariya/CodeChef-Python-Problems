# CODECHEF - Rating 232

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Codechef Round

Codechef rounds are held on every Wednesday now, and not on any other days.

You are wondering whether there is a Codechef round today. You know it is the $N^{th}$ day of the week (Sunday is $1$st, Monday is $2$nd, Tuesday is $3$rd, Wednesday is $4$th and so on).

Can you tell whether there is a Codechef round today?

### Input Format
- The first and only line of input contains a single integer $N$, the day of the week.
### Output Format

Output `YES` if there is a Codechef round today, else `NO`.

You may print each character of the string in uppercase or lowercase (for example, the strings `YES`, `yEs`, `yes`, and `yeS` will all be treated as identical).

### Constraints
- $1 \le N \le 7$
### Sample 1:
Input
Output

```
1

```

```
NO
```

### Explanation:

$1$st day of the week is Sunday, but Codechef rounds are not held anymore on Sunday.

### Sample 2:
Input
Output

```
4

```

```
YES
```

### Explanation:

$4$th day of the week is Wednesday, which is when all Codechef rounds are held now.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-03T14:42:14.276Z  

```py
N=int(input())
if N==4:
    print("Yes")
else:
    print("No")
```

---

[View on CodeChef](https://www.codechef.com/problems/CODECHEF)