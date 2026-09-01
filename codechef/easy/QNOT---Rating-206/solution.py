N, X, Y = map(int, input().split())

if N >= 2 * X and N >= 2 * Y:
    print("YES")
else:
    print("NO")