A,B,C,X=map(int,input().split())
if (A*B*C)>(X**3):
    print("Cuboid")
elif (A*B*C)<(X**3):
    print("Cube")
else:
    print("Equal")