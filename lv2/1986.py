# 1부터 N까지의 숫자에서 홀수는 더하고 짝수는 뺏을 때의 결과를 출력하는 문제
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # N을 입력받는다.
    N = int(input())
    # 합산을 넣을 변수를 정의한다.
    ans = 0
    # N번 만큼 반복한다.
    for i in range(1, N + 1):
        # i가 홀수인 경우와, 짝수인 경우를 나누어 ans에 합산한다.
        if i % 2 == 1:
            ans += i
        else:
            ans -= i
    # 더하고 뺀 합산을 문제 번호와 함께 출력한다.
    print(f'#{test_case} {ans}')