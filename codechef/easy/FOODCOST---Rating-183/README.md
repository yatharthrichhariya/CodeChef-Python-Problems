# FOODCOST - Rating 183

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Food Costs

You're a bit all over the place as a college student. You used to eat out at expensive restaurants almost every day until your parents gave you a talking-to about being irresponsible. Now, you've got to control your eating and spending habits.

So, here's the plan: you'll stick to the college mess for your meals every day, except Sundays. On Sundays, you're treating yourself to those fancy restaurant meals.
The cost is Rs. $X$ for the mess food each day, and Rs. $Y$ for the restaurant splurges.

Now, what's the cost of food per week? Note that you don't have to pay for the mess on Sundays.
A week has seven days, as usual.

### Input Format
- The first and only line of input contains $2$ space-separated integers, $X$ and $Y$.
### Output Format

Output a single integer: the weekly cost of food.

### Constraints
- $1 \le X \lt Y \le 1000$
### Sample 1:
Input
Output

```
100 500

```

```
1100

```

### Explanation:

On Monday, Tuesday, Wednesday, Thursday, Friday and Saturday, your food cost is $100$.

On Sunday, your food cost is $500$.

Thus your total food cost is $100 + 100 + 100 + 100 + 100 + 100 + 500 = 1100$

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-08-27T17:59:37.885Z  

```py
X,Y=map(int,input().split())
print((X*6)+Y)

```

---

[View on CodeChef](https://www.codechef.com/problems/FOODCOST)