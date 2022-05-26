T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # a와 b를 입력받습니다.
    a, b = map(int, input().split())
    # test_case와 함께 몫과 나머지를 출력합니다.
    print(f'#{test_case} {int(a/b)} {a%b}')