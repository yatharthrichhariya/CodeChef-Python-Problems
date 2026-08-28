# FUELCHK - Rating 186

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Fuel Check

Chef plans to go on a long drive, and is now checking whether he has enough fuel for the trip.

Chef's car has $X$ units of fuel remaining.
The car has a fuel efficiency of $Y$, meaning that for each unit of fuel it has, it can travel a distance of $Y$ kilometers.

Chef knows that the distance he needs to travel is exactly $100$ kilometers.
Does he have enough fuel for his trip?

### Input Format
- The only line of input will contain two space-separated integers $X$ and $Y$ — the amount of fuel remaining and the car's fuel efficiency, respectively.
### Output Format

For each test case, output on a new line the answer: `Yes` if Chef has enough fuel remaining, and `No` otherwise.

Each character of the output can be printed in either uppercase or lowercase, i.e. the strings `NO`, `no`, `No`, and `nO` will all be treated as equivalent.

### Constraints
- $1 \le X, Y\le 100$
### Sample 1:
Input
Output

```
10 13

```

```
Yes
```

### Explanation:

There are $X = 10$ units of fuel remaining.
Each unit of fuel allows the car to travel for $Y = 13$ kilometers.
So, the total distance the car can travel equals $10\times 13 = 130$ kilometers.
Since $130 \ge 100$, Chef has enough fuel for the trip.

### Sample 2:
Input
Output

```
5 8

```

```
No
```

### Explanation:

There are $X = 5$ units of fuel remaining.
Each unit of fuel allows the car to travel for $Y = 8$ kilometers.
So, the total distance the car can travel equals $5\times 8 = 40$ kilometers.
Since $40 \lt 100$, Chef does not have enough fuel for the trip.

### Sample 3:
Input
Output

```
5 20

```

```
Yes
```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-08-28T17:20:28.450Z  

```py
X,Y=map(int,input().split())
A=X*Y
if A>=100:
    print("Yes")
else:
    print("No")
```

---

[View on CodeChef](https://www.codechef.com/problems/FUELCHK)