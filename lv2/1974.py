# 9 x 9 크기의 스도쿠를 입력받아 규칙에 받게 입력되어있는지 판단하는 문제
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # 스도쿠를 9 x 9 matrix 형태로 입력받는다.
    sudoku = [list(map(int, input().split())) for _ in range(0, 9)]
    ans = 1
    tmp = 0
    # 가로 검증
    for i in range(0, 9):
        if ans == 0:
            break
        for j in range(0, 9):
            if ans == 0:
                break
            tmp = sudoku[i][j]
            for k in range(j + 1, 9):
                if sudoku[i][k] == tmp:
                    ans = 0
    # 세로 검증
    for j in range(0, 9):
        if ans == 0:
            break
        for i in range(0, 9):
            if ans == 0:
                break
            tmp = sudoku[i][j]
            for l in range(i + 1, 9):
                if sudoku[l][j] == tmp:
                    ans = 0
    # 네모 검증
    for i in range(0, 3):
        if ans == 0:
            break
        for j in range(0, 3):
            if ans == 0:
                break
            I = 3 * i - 3
            J = 3 * j - 3
            for a in range(0, 3):
                if ans == 0:
                    break
                for b in range(0, 3):
                    if ans == 0:
                        break
                    tmp = sudoku[I + a][J + b]
                    for c in range(0, 3):
                        if ans == 0:
                            break
                        for d in range(0, 3):
                            if not(I + a == I + c and J + b == J + d):
                                if sudoku[I + c][J + d] == tmp:
                                    ans = 0
    # 검증이 끝난 후 test_case와 함께 출력
    print(f'#{test_case} {ans}')
