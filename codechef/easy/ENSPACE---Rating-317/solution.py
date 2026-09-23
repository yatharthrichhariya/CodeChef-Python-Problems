T=int(input())
for i in range(T):
    N,X,Y=map(int,input().split())
    A=X*1+Y*2
    if N>=A:
        print("Yes")
    else:
        print("No")