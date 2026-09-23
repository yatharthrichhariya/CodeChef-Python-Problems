# CREDS - Rating 306

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Number of Credits

In the current semester, you have taken $X$ RTP courses, $Y$ Audit courses and $Z$ Non-RTP courses.

The credit distribution for the courses are:

- $4$ credits for clearing each RTP course.
- $2$ credits for clearing each Audit course.
- No credits for clearing a Non-RTP course.

Assuming that you cleared all your courses, report the number of credits you obtain this semester.

### Input Format

The first line contains a single integer $T$, the number of test cases. $T$ test cases follow. Each test case consists of one line, containing $3$ integers separated by spaces.

- The first integer is $X$, the number of RTP courses.
- The second integer is $Y$, the number of Audit courses.
- The third integer is $Z$, the number of non-RTP courses.
### Output Format

The output must consist of $T$ lines. The $i^{th}$ should consist of a single integer: the number of credits one gets for the $i^{th}$ test case.

### Constraints
- $1 \le T \le 10$
- $1 \le X, Y, Z \le 10$
### Sample 1:
Input
Output

```
4
6 6 5
8 7 2
9 3 8
9 2 4

```

```
36
46
42
40

```

### Explanation:

 **Test case $1$:**  You obtain $4$ credits for each of the RTP courses, accounting for $4 \cdot 6 = 24$ credits. You also obtain $2$ credits for each audit course, accounting for $2 \cdot 6 = 12$ credits. Finally, you get $0$ credits for each of the non-RTP courses, accounting for $0 \cdot 5 = 0$ credits. This accounts for a total of $24 + 12 + 0 = 36$ credits.

 **Test case $2$:**  You obtain $4$ credits for each of the RTP courses, accounting for $4 \cdot 8 = 32$ credits. You also obtain $2$ credits for each audit course, accounting for $2 \cdot 7 = 14$ credits. Finally, you get $0$ credits for each of the non-RTP courses, accounting for $0 \cdot 2 = 0$ credits. This accounts for a total of $32 + 14 + 0 = 46$ credits.

 **Test case $3$:**  You obtain $4$ credits for each of the RTP courses, accounting for $4 \cdot 9 = 36$ credits. You also obtain $2$ credits for each audit course, accounting for $2 \cdot 3 = 6$ credits. Finally, you get $0$ credits for each of the non-RTP courses, accounting for $0 \cdot 8 = 0$ credits. This accounts for a total of $36 + 6 + 0 = 42$ credits.

 **Test case $4$:**  You obtain $4$ credits for each of the RTP courses, accounting for $4 \cdot 9 = 36$ credits. You also obtain $2$ credits for each audit course, accounting for $2 \cdot 2 = 4$ credits. Finally, you get $0$ credits for each of the non-RTP courses, accounting for $0 \cdot 4 = 0$ credits. This accounts for a total of $36 + 4 + 0 = 40$ credits.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-23T09:13:30.524Z  

```py
T=int(input())
for i in range(T):
    X,Y,Z=map(int,input().split())
    A=X*4
    B=Y*2
    C=Z*0
    print(A+B+C)
```

---

[View on CodeChef](https://www.codechef.com/problems/CREDS)