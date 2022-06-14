# N x N 행렬이 주어질 때, 시계방향으로 각각 90도, 180도, 270도 회전한 모양을 출력하는 문제
# 행렬을 90도 회전시키는 함수를 작성합니다.
def turn_matrix(matrix, n):
    turned_matrix = [[0]*n for _ in range(n)]
    for i in range(0, n):
        for j in range(0, n):
            turned_matrix[i][j] = matrix[n - j - 1][i]
    return turned_matrix

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # 행렬의 크기인 N을 입력받습니다.
    N = int(input())
    # N x N 크기의 행렬을 list 형태로 입력받습니다.
    matrix = [list(map(int, input().split())) for _ in range(N)]
    # 90도, 180도, 270도 회전한 list를 만든다.
    matrix_90 = turn_matrix(matrix, N)
    matrix_180 = turn_matrix(matrix_90, N)
    matrix_270 = turn_matrix(matrix_180, N)
    # test_case 와 함께 결과를 출력한다.
    print(f'#{test_case}')
    for i in range(N):
        for j in range(N):
            if j == N - 1:
                print(matrix_90[i][j], end=" ")
            else:
                print(matrix_90[i][j], end="")
        for j in range(N):
            if j == N - 1:
                print(matrix_180[i][j], end=" ")
            else:
                print(matrix_180[i][j], end="")
        for j in range(N):
            if j == N - 1:
                print(matrix_270[i][j])
            else:
                print(matrix_270[i][j], end="")