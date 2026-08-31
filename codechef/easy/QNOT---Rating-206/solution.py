N, X, Y = map(int, input().split())

if N >= 2 * max(X, Y):
    print("YES")
else:
    print("NO")