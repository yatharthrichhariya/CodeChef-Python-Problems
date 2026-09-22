T=int(input())
for i in range(T):
    X,Y=map(int,input().split())
    if X>Y:
        print(abs(X-Y))
    else:
        print("0")