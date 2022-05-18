# test_case의 수를 T에 할당
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # 10개의 정수를 list에 할당한다.
    numbers = list(map(int, input().split()))
    # list의 평균을 구한다.
    average_ = sum(numbers) / 10
    # 소수점 첫째 자리에서 반올림
    if average_ - int(average_) >= 0.5:
        average_ = int(average_) + 1
    else:
        average_ = int(average_)
    print(f"#{test_case} {average_}")