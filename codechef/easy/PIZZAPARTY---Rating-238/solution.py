A, B = map(int, input().split())
if (((A + 1) * 4 + B * 3) % 8 == 0):
    print(((A + 1) * 4 + B * 3) // 8)
else:
    print(((A + 1) * 4 + B * 3) // 8 + 1)
