# N x N 크기의 배열안의 M x M 크기의 배열의 수의 합을 구하는 문제
T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    # 크기가 N인 list를 만든다.
    arr = [0] * N
    for i in range(0, N):
        # list의 각 요소에 list를 넣어 2차원 matrix를 만든다.
        arr[i] = list(map(int, input().split()))
    maxOfFly = 0
    for j in range(0,N - M + 1):
        for k in range(0,N - M + 1):
            # M x M 크기의 matrix 내부 합을 구하여 max보다 클 경우 max를 갱신한다.
            numOfFly = 0
            for l in range(0, M):
                numOfFly += sum(arr[j+l][k:k+M])
            if maxOfFly < numOfFly:
                maxOfFly = numOfFly
    print(f'#{test_case} {maxOfFly}')
