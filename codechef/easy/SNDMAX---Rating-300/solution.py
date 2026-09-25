N = int(input())
for i in range(N):
    A, B, C = map(int, input().split())
    numbers = [A, B, C]
    numbers.sort()
    print(numbers[1])