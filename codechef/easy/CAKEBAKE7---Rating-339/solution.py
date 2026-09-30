N,M=map(int,input().split())
B=M//N
if (B>=2):
    print(N)
else:
    print(M%N)