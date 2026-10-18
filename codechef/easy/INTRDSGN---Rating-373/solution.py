T=int(input())
for i in range(T):
    X1,Y1,X2,Y2=map(int,input().split())
    if X1+Y1<X2+Y2:
        print(X1+Y1)
    else:
        print(X2+Y2)