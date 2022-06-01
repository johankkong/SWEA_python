# 정수 N을 입력받아 N 크기의 파스칼 삼각형을 출력하는 문제
T = int(input())

# 파스칼 삼각형의 다음 줄을 구하는 함수를 작성하였다.
def next_line(upper):
    upper = upper + [0]
    tmp = [0] + upper
    lower = [0] * len(upper)
    for i in range(0, len(upper)):
        lower[i] = upper[i] + tmp[i]
    return lower

# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # 정수 N을 입력받는다.
    print(f'#{test_case}')
    N = int(input())
    for i in range(0, N):
        if i == 0:
            upper = [1]
        print(*upper)
        lower = next_line(upper)
        upper = lower