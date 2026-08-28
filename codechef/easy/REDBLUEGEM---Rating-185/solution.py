R,B,P,Q=map(int,input().split())
A=R*P
S=B*Q
if A>S:
    print(A)
else:
    print(S)