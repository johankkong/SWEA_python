# 정수 N을 입력받아 N의 약수를 오름차순으로 출력하는 문제
N = int(input())
# 1부터 하나씩 늘려가며 약수인지 확인하고 출력한다.
for i in range(1, N+1):
    if N % i == 0:
        print(i, end=" ")