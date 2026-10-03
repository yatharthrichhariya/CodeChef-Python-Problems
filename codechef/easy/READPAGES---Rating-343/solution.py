T=int(input())
for i in range(T):
    N,X,Y=map(int,input().split())
    if X*Y>=N:
        print("Yes")
    else:
        print("No")