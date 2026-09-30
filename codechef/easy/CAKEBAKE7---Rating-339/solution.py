N,M=map(int,input().split())
A=M%N
B=M//N
if (B>=2):
    print(N)
else:
    print(A)