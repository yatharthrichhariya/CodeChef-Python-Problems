F1,P1,F2,P2=map(int,input().split())
if F1+P1 > F2+P2:
    print("First")
elif F1+P1 < F2+P2:
    print("Second")
else:
    print('Both')