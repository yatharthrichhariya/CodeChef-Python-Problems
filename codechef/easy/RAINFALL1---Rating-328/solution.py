T=int(input())
for i in range(T):
    X=int(input())
    if X<3:
        print("LIGHT")
    elif X<7:
        print("MODERATE")
    else:
        print("HEAVY")