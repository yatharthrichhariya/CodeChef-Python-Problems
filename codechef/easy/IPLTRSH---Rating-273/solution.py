T=int(input())
for i in range(T):
    N,M=map(int,input().split())
    if N>=M:
        print(N-M)
    else:
        print("0")
