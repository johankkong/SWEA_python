# 두 개의 시각을 입력받아 더하여 출력하는 문제
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # 4개의 정수를 각각 시1, 분1, 시2, 분2 로 입력받는다.
    hour_1, min_1, hour_2, min_2 = map(int, input().split())
    # 분을 먼저 더한다.
    ans_min = (min_1 + min_2) % 60
    # 분을 더한 것이 60을 넘어가는 경우와 그렇지 않은 경우를 나누어 시를 계산한다.
    if min_1 + min_2 >= 60:
        ans_hour = (hour_1 + hour_2) % 12 + 1
    else:
        ans_hour = (hour_1 + hour_2 - 1) % 12 + 1
    # test_case 와 함께 결과를 출력한다.
    print(f'#{test_case} {ans_hour} {ans_min}')
