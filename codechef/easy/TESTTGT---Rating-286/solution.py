X,Y,Z=map(int,input().split())
A=X+Z
B=(A-Y)+1
if A>=Y:
    print(B)
else:
    print("0")