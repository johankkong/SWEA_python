# 1대1 가위바위보
# 가위는 1, 바위는 2, 보는 3에 해당하고 A와 B중 누가 이겼는지 출력하는 문제
A, B = map(int, input().split())
if A != 3:
    if A < B:
        print('B')
    else:
        print("A")
else:
    if B == 2:
        print('A')
    else:
        print('B')