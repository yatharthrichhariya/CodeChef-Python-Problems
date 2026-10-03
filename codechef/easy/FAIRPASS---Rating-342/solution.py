T=int(input())
for i in range(T):
    N,K=map(int,input().split())
    if N<K:
        print("Yes")
    else:
        print("No")