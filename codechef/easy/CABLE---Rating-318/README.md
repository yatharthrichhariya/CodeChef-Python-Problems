# CABLE - Rating 318

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Volume Comparison

Alice has two objects:

- A cuboid with length $A$ units, height $B$ units, and width $C$ units.
- A cube with an edge length of $X$ units.

Alice wants to know which of the two objects has a larger volume, or if their volumes are equal.

### Input Format
- The first and only line of input will contain four space-separated integers $A$, $B$, $C$ and $X$, the length of the cuboid, the width of the cuboid, the height of the cuboid, and the length of the edge of the cube.
### Output Format

Print a single line containing the string:

- "Cuboid", if the volume of the cuboid is greater than the volume of the cube.
- "Cube", if the volume of the cube is greater than the volume of the cuboid.
- "Equal", if both objects have equal volume.

Print the string without quotes.
You can print each character of the output in either uppercase or lowercase.
For example, the strings `Cube`, `CUBE`, `cube`, and `CuBe` are considered identical.

### Constraints
- $1 \leq A,B,C,X \leq 10$
### Sample 1:
Input
Output

```
1 3 10 3
```

```
Cuboid
```

### Explanation:

The volume of the cuboid is $1\times 3\times 10 = 30$ cubic units.
The volume of the cube is $3^3 = 27$ cubic units.

The cuboid has larger volume.

### Sample 2:
Input
Output

```
1 1 1 2
```

```
Cube
```

### Explanation:

The volume of the cuboid is $1\times 1\times 1 = 1$ cubic units.
The volume of the cube is $2^3 = 8$ cubic units.

The cube has larger volume.

### Sample 3:
Input
Output

```
8 4 2 4
```

```
Equal
```

### Explanation:

The volume of the cuboid is $8\times 4\times 2 = 64$ cubic units.
The volume of the cube is $4^3 = 64$ cubic units.

Both objects have the same volume.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-24T10:33:18.148Z  

```py
A,B,C,X=map(int,input().split())
if (A*B*C)>(X**3):
    print("Cuboid")
elif (A*B*C)<(X**3):
    print("Cube")
else:
    print("Equal")
```

---

[View on CodeChef](https://www.codechef.com/problems/CABLE)