
t = int(input())
for i in range(t):
    A, B = map(int, input().split())
    print(min(7 - A, 7 - B))