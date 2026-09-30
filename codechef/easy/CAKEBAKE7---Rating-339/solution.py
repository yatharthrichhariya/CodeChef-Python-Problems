N,M=map(int,input().split())
A=M-1
if N%2==0 and N>=2:
    print(N//2)
else:
    print(A//2)