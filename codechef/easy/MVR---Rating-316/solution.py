A,B,X,Y=map(int,input().split())
C=A*2+B
Z=X*2+Y
if C>Z:
    print("Messi")
elif C<Z:
    print("Ronaldo")
else:
    print("Equal")