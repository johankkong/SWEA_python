# 주어진 숫자들을 오름차순으로 정렬하여 출력하는 문제
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # 숫자의 갯수를 입력받습니다.
    N = int(input())
    # 주어진 숫자들을 list로 입력 받습니다.
    number_list = list(map(int, input().split()))
    # list를 오름차순으로 정렬합니다.
    number_list.sort()
    # test_case와 함께 결과를 출력합니다.
    print(f'#{test_case}', end=" ")
    print(*number_list)