T=int(input())
for i in range(T):
    A,B=map(int,input().split())
    if A<B:
        print(A)
    elif A==B:
        print(7)
    else:
        print(B)