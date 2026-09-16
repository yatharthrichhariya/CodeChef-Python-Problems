# FIZZBUZZ2301 - Rating 273

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Fan Poll

 *Chef Sports*  conducted a fan poll to find out who their fans thought was the best captain.
The three players nominated were Dhoni, Rohit, and Kohli. They received $A, B,$ and $C$ votes, respectively.

Find out whether Dhoni won the poll, i.e, if he received the maximum number of votes.

 **Note:**  It is guaranteed that no two players received the same number of votes.

### Input Format

The only line of input contains three space-separated integers $A$, $B$, and $C$ — the number of votes obtained by Dhoni, Rohit, and Kohli, respectively.

### Output Format

Print the answer on a single line: `"Yes"` (without quotes) if Dhoni won the poll, and `"No"` (without quotes) otherwise.

Each character of the output may be printed in either uppercase or lowercase, i.e, the strings `No`, `no`, nO`, and `NO` will all be treated as equivalent.

### Constraints
- $1 \leq A \leq 1000$
- $1 \leq B \leq 1000$
- $1 \leq C \leq 1000$
- $A \neq B$, $A \neq C$, and $B\neq C$
### Sample 1:
Input
Output

```
50 23 28
```

```
Yes
```

### Explanation:

Dhoni received $50$ votes, which is higher than the other two. This makes him the winner.

### Sample 2:
Input
Output

```
25 22 26
```

```
No
```

### Explanation:

Dhoni received $25$ votes, but Kohli received $26$ which is larger - so, Dhoni didn't win.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-16T15:27:40.196Z  

```py
A,B,C=map(int,input().split())
if A>B and A>C:
    print("Yes")
else:
    print("No")
```

---

[View on CodeChef](https://www.codechef.com/problems/FIZZBUZZ2301)