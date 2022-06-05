# 각 학생의 점수가 주어졌을때, K번째 학생의 학점을 출력하는 문제
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # N명의 전체 학생 수와 K번째 학생임을 입력 받는다.
    N, K = map(int, input().split())
    # 전체 학생의 성적을 list로 입력받는다.
    score_board = [0] * N
    for i in range(0, N):
        score_board[i] = list(map(int, input().split()))
    # 시험 점수와 과제 점수를 총점으로 변환한다.
    for i in range(0, N):
        score_board[i] = score_board[i][0] * 0.35 + score_board[i][1] * 0.45 + score_board[i][2] * 0.2
    # K번째 학생의 점수를 변수에 저장하고 list를 정렬하여 몇번째 그룹에 있는지에 따라 결과를 출력한다.
    K_score = score_board[K - 1]
    score_board.sort()
    if K_score < score_board[int(N / 10)]:
        print(f'#{test_case} D0')
    elif K_score < score_board[int(2 * N / 10)]:
        print(f'#{test_case} C-')
    elif K_score < score_board[int(3 * N / 10)]:
        print(f'#{test_case} C0')
    elif K_score < score_board[int(4 * N / 10)]:
        print(f'#{test_case} C+')
    elif K_score < score_board[int(5 * N / 10)]:
        print(f'#{test_case} B-')
    elif K_score < score_board[int(6 * N / 10)]:
        print(f'#{test_case} B0')
    elif K_score < score_board[int(7 * N / 10)]:
        print(f'#{test_case} B+')
    elif K_score < score_board[int(8 * N / 10)]:
        print(f'#{test_case} A-')
    elif K_score < score_board[int(9 * N / 10)]:
        print(f'#{test_case} A0')
    else:
        print(f'#{test_case} A+')