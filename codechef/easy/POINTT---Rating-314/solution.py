X, Y, A, B = map(int, input().split())
if X > A:
    print("Alice")
elif X < A:
    print("Bob")
elif Y > B:
    print("Alice")
elif Y < B:
    print("Bob")
else:
    print("Alice")