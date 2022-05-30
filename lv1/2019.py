# 1부터 주어진 횟수만큼 2를 곱해가며 출력하는 문제
num_ = int(input())
for i in range(0, num_ + 1):
    tmp = 1
    for j in range(0, i):
        tmp *= 2
    print(tmp, end=" ")