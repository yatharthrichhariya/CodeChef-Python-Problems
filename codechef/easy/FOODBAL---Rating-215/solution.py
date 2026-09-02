F1,P1,F2,P2=map(int,input().split())
if abs(F1+P1) > abs(F2+P2):
    print("First")
elif abs(F1+P1) < abs(F2+P2):
    print("Second")
else:
    print('Both')