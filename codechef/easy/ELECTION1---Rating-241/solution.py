N,K=map(int,input().split())
A=(N//2)+1
if A-K<0:
    print("0")
else:
    print(A-K)