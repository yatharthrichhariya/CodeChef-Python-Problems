T = int(input())
for i in range(T):
    X, P, Q = map(int, input().split())
    fine = (P - Q) * X
    print(fine)