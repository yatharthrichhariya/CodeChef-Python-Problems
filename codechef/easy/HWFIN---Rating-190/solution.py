X,Y=map(int,input().split())
A=10-Y
B=A*Y
if X+B<=100:
    print("Yes")
else:
    print("No")