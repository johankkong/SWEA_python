# N x N 크기의 단어 퍼즐에 K 길이의 단어가 들어갈 수 있는 자리가 몇 개인지 출력하는 문제
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # N과 K를 입력받는다.
    N, K = map(int, input().split())
    # N x N 크기의 matrix로 입력받는다.
    word_puzzle = [list(map(int, input().split())) for _ in range(0, N)]
    # 가로와 세로로 1이 연속된 구간의 길이가 K 인지 판별한다.
    ans = 0
    tmp = 0
    # 가로
    for i in range(0, N):
        for j in range(0, N):
            if word_puzzle[i][j] == 1:
                tmp += 1
            if word_puzzle[i][j] == 0 or j == N - 1:
                if tmp == K:
                    ans += 1
                tmp = 0
    # 세로
    for j in range(0, N):
        for i in range(0, N):
            if word_puzzle[i][j] == 1:
                tmp += 1
            if word_puzzle[i][j] == 0 or i == N - 1:
                if tmp == K:
                    ans += 1
                tmp = 0
    # 결과를 출력한다.
    print(f'#{test_case} {ans}')