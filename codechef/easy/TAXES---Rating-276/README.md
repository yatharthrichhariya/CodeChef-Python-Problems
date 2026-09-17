# TAXES - Rating 276

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Tax in Chefland

In Chefland, a tax of rupees $10$ is deducted if the total income is  **strictly greater**  than rupees $100$.

Given that total income is $X$ rupees, find out how much money you get.

### Input Format
- The first line of input will contain a single integer $T$, denoting the number of test cases.
- The first and only line of each test case contains a single integer $X$ — your total income.
### Output Format

For each test case, output on a new line, the amount of money you get.

### Constraints
- $1 \leq T \leq 100$
- $1 \leq X \leq 1000$
### Sample 1:
Input
Output

```
4
5
105
101
100

```

```
5
95
91
100
```

### Explanation:

 **Test case $1$:**  Your total income is $5$ rupees which is less than $100$ rupees. Thus, no tax would be deducted and you get $5$ rupees.

 **Test case $2$:**  Your total income is $105$ rupees which is greater than $100$ rupees. Thus, a tax of $10$ rupees would be deducted and you get $105-10 = 95$ rupees.

 **Test case $3$:**  Your total income is $101$ rupees which is greater than $100$ rupees. Thus, a tax of $10$ rupees would be deducted and you get $101-10 = 91$ rupees.

 **Test case $4$:**  Your total income is $100$ rupees which is equal to $100$ rupees. Thus, no tax would be deducted and you get $100$ rupees.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-17T17:56:40.089Z  

```py
T = int(input())

for i in range(T):
    X = int(input())
    
    if X > 100:
        print(X - 10)
    else:
        print(X)
```

---

[View on CodeChef](https://www.codechef.com/problems/TAXES)