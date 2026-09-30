T=int(input())
for i in range(T):
    A,B=map(int,input().split())
    if (A+B)%2==0:
        print("Yes")
    else:
        print("No")