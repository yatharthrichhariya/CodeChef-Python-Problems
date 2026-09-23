# ENSPACE - Rating 317

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Enough Space

Chef's computer has $N$ GB of free space. He wants to save $X$ files, each of size `1` GB and $Y$ files, each of size `2` GB on his computer. Will he be able to do so?

Chef can save all the files on his computer only if the total size of the files is  **less than or equal**  to the space available on his computer.

### Input Format
- The first line contains an integer $T$, denoting the number of test cases. The $T$ test cases then follow:
- The first and only line of each test case contains three integers $N, X, Y$, denoting the free-space in computer, the number of 1 and 2 GB files respectively.
### Output Format

For each test case, print `YES` if Chef is able to save the files and `NO` otherwise.

You may print each character of the string in uppercase or lowercase (for example, the strings `yEs`, `yes`, `Yes` and `YES` will all be treated as identical).

### Constraints
- $1 \leq T \leq 100$
- $1 \leq N, X, Y \leq 100$
### Sample 1:
Input
Output

```
4
6 3 1
2 2 2
4 3 2
5 1 2

```

```
YES
NO
NO
YES

```

### Explanation:

 **Test case $1$:**  The total size of files is $3 + 1 \cdot 2 =5$, which is smaller than the remaining space on the computer. Thus Chef will be able to save all the files.

 **Test case $2$:**  The total size of files is $2 + 2 \cdot 2 =6$, which is greater than the remaining space on the computer. Thus Chef will not be able to save all the files.

 **Test case $3$:**  The total size of files is $3 + 2 \cdot 2 =7$, which is greater than the remaining space on the computer. Thus Chef will not be able to save all the files.

 **Test case $4$:**  The total size of files is $1 + 2 \cdot 2 =5$, which is equal to the remaining space on the computer. Thus Chef will be able to save all the files.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-23T10:49:46.297Z  

```py
T=int(input())
for i in range(T):
    N,X,Y=map(int,input().split())
    A=X*1+Y*2
    if N>=A:
        print("Yes")
    else:
        print("No")
```

---

[View on CodeChef](https://www.codechef.com/problems/ENSPACE)