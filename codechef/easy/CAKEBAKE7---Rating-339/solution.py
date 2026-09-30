N,M=map(int,input().split())
A=N%M
B=N//M
if (B>=2):
    print(M)
else:
    print(A)