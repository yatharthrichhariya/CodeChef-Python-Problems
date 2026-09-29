# TASTEDEC - Rating 324

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Tasty Decisions

Chef is buying sweet things to prepare for Halloween!

The shop sells both chocolate and candy.

- Each bar of chocolate has a tastiness of $X$.
- Each piece of candy has a tastiness of $Y$.

One packet of chocolate contains $2$ bars, while one packet of candy contains $5$ pieces.

Chef can only buy one packet of something sweet, and so has to make a decision: which one should he buy in order to  **maximize the total tastiness**  of his purchase?

Print `Chocolate` if the packet of chocolate is tastier, `Candy` if the packet of candy is tastier, and `Either` if they have the same tastiness.

### Input Format
- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of one line of input, containing two space-separated integers $X$ and $Y$ — the tastiness of one bar of chocolate and one piece of candy, respectively.
### Output Format

For each test case, output on a new line the answer:

- Chocolate if the packet of chocolate is tastier.
- Candy if the packet of candy is tastier.
- Either if they have the same tastiness.

You may print each character of the output in either uppercase or lowercase, i.e, `Candy`, `CANDY`, `CaNdY` and `cANDy` will all be treated as equivalent.

### Constraints
- $1 \leq T \leq 100$
- $1 \leq X, Y \leq 10$
### Sample 1:
Input
Output

```
4
5 1
5 2
5 3
3 10

```

```
Chocolate
Either
Candy
Candy

```

### Explanation:

 **Test case $1$:**  The packet of chocolate has a tastiness of $2\times 5 = 10$, while the packet of candy has a tastiness of $5\times 1 = 5$. The chocolate is tastier.

 **Test case $2$:**  The packet of chocolate has a tastiness of $2\times 5 = 10$, while the packet of candy has a tastiness of $5\times 2 = 10$. They have the same tastiness.

 **Test case $3$:**  The packet of chocolate has a tastiness of $2\times 5 = 10$, while the packet of candy has a tastiness of $5\times 3 = 15$. The candy is tastier.

 **Test case $4$:**  The packet of chocolate has a tastiness of $2\times 3 = 6$, while the packet of candy has a tastiness of $5\times 10 = 50$. The candy is tastier.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-29T09:52:01.726Z  

```py
T=int(input())
for i in range(T):
    X,Y=map(int,input().split())
    if ((X*2)>(Y*5)):
        print("Chocolate")
    elif ((X*2)==(Y*5)):
        print("Either")
    else:
        print("Candy")
```

---

[View on CodeChef](https://www.codechef.com/problems/TASTEDEC)