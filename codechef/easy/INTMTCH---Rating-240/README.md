# INTMTCH - Rating 240

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Interesting Match

Chefland and Byteland are playing a football match against each other.

Chef thinks a football match is  *interesting*  if the  **absolute difference**  in the number of goals scored by both teams is  **at most $2$.** 

In this match, Chefland scored $X$ goals and Byteland scored $Y$ goals.
Did Chef find the match interesting?

### Input Format
- The input contains two space-separated integers $X$ and $Y$ — the number of goals scored by Chefland and Byteland, respectively.
### Output Format

Output the answer: the string "`Interesting`" if Chef found the match interesting, and the string "`Boring`" otherwise (without quotes).

Each letter of the output may be printed in either uppercase or lowercase, i.e. the strings `Boring`, `BORING`, `bOrInG`, and `boRIng` will all be considered equivalent.

### Constraints
- $0 \le X, Y \le 10$
### Sample 1:
Input
Output

```
2 4
```

```
Interesting

```

### Explanation:

Chefland scored $2$ goals and Byteland scored $4$ goals.
The difference in the number of goals is $2$, so Chef thinks the match is interesting.

### Sample 2:
Input
Output

```
7 1
```

```
Boring
```

### Explanation:

Chefland scored $7$ goals and Byteland scored $1$ goal.
The difference in the number of goals is $6$. This is larger than $2$, so Chef finds the match boring.

### Sample 3:
Input
Output

```
0 0
```

```
Interesting
```

### Explanation:

Chefland and Byteland both scored $0$ goals.
The difference in the number of goals is $0$. This is $\le 2$, so Chef finds the match interesting.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-06T15:14:01.738Z  

```py
X,Y=map(int,input().split())
if abs(Y-X)<=2:
    print("Interesting")
else:
    print("Boring")
```

---

[View on CodeChef](https://www.codechef.com/problems/INTMTCH)