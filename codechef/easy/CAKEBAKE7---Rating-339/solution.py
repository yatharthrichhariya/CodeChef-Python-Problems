N,M=map(int,input().split())
A=M-1
if N%2==0 and N>=2:
    print(N//2)
elif N>=2:
    print(A//2)