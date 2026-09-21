# RCBCSK - Rating 282

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### RCB vs CSK

In the recent RCB vs CSK match, RCB batted first and scored $X$ runs while CSK batted second and scored $Y$ runs.

It is known that RCB qualifies to the playoffs if they win by  **at least**  $18$ runs, otherwise CSK qualify. Knowing the final scores of both teams, find out who qualified to the playoffs.

### Input Format
- The only line of input contains $2$ integers $X$ and $Y$ - the final scores of RCB and CSK respectively.
### Output Format

Output `RCB` if RCB managed to qualify to the playoffs, otherwise output `CSK`.

You may print each character of the string in uppercase or lowercase (for example, the strings `RCB`, `rCb`, `rcb`, and `rcB` will all be treated as identical).

### Constraints
- $150 \le X \le 250$
- $150 \le Y \le X + 6$
### Sample 1:
Input
Output

```
218 191

```

```
RCB
```

### Explanation:

RCB won by $218 - 191 = 27$ runs, which is more than $18$. Thus, RCB qualified.

### Sample 2:
Input
Output

```
218 201

```

```
CSK
```

### Explanation:

RCB won by $218 - 201 = 17$ runs, which is less than $18$. Thus, CSK qualified.

### Sample 3:
Input
Output

```
218 200

```

```
RCB

```

### Explanation:

RCB won by $218 - 200 = 18$ runs, which is equal to $18$. Thus, RCB qualified.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-21T11:40:05.163Z  

```py
X,Y=map(int,input().split())
if (X-Y)>18:
    print("RCB")
else:
    print("CSK")
```

---

[View on CodeChef](https://www.codechef.com/problems/RCBCSK)