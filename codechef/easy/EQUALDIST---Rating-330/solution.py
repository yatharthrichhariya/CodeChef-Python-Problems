T=int(input())
for i in range(T):
    A,B=map(int,input().split())
    if A<B and B+A==B and A:
        print("Yes")
    else:
        print("No")