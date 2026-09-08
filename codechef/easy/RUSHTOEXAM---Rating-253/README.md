# RUSHTOEXAM - Rating 253

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Rush to Exam

Chef has an exam in the next $N$ hours, and he still has to read $M$ pages of a book to be fully prepared for the exam.

Every hour, Chef reads is able to read exactly $A$ pages. Will Chef be able to read all $M$ pages before the exam? Print $\text{Yes}$ or $\text{No}$ accordingly.

### Input Format
- The first and only line contains $3$ integers - $N$, $M$ and $A$.
### Output Format

Print $\text{Yes}$ if Chef will be able to finish reading all $M$ pages, and $\text{No}$ otherwise.

### Constraints
- $1 \le N \le 24$
- $1 \le M \le 100$
- $1 \le A \le 10$
### Sample 1:
Input
Output

```
3 6 2

```

```
Yes

```

### Explanation:

Chef will be able to read exactly $2 \cdot 3 = 6$ pages in the $2$ hours barely finishing in time.

### Sample 2:
Input
Output

```
3 7 2

```

```
No
```

### Explanation:

Chef will be able to read only $6$ pages, falling short of the required $7$ pages.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-08T15:18:15.276Z  

```py
N,M,A=map(int,input().split())
if (A*N) > M:
    print("No")
else:
    print("Yes")
```

---

[View on CodeChef](https://www.codechef.com/problems/RUSHTOEXAM)