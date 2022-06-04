# 10개의 수를 입력받아, 최대 수와 최소 수를 제외한 8개의 수의 평균값을 출력하는 문제
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # 10개의 수를 list로 입력받는다.
    num_list = list(map(int, input().split()))
    # 전체 합산에서 최대 수와 최소 수를 더해서 8로 나눈다.
    sum_eight = sum(num_list) - max(num_list) - min(num_list)
    average_eight = sum_eight / 8
    # 소수점 첫째 자리에서 반올림을 해준다.
    if average_eight - int(average_eight) < 0.5:
        final_ans = int(average_eight)
    else:
        final_ans = int(average_eight) + 1
    # test_case와 함께 결과를 출력해준다.
    print(f'#{test_case} {final_ans}')
