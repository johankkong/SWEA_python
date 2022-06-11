    # 최소의 화폐 수로 주어진 금액과 같게 만드는 화폐 갯수를 구하는 문제
    T = int(input())
    # 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
    for test_case in range(1, T + 1):
        # 주어진 금액을 입력받는다.
        N = int(input())
        # 50000원 단위부터 차례로 갯수를 표현할 list를 정의한다.
        count_cash = [0] * 8
        # 큰 단위부터 차례로 나눠가며 몫과 나머지를 구한다.
        # 몫은 화폐의 갯수가 되고 나머지는 다음 화폐로 몫과 나머지를 구하게 된다.
        count_cash[0] = int(N / 50000)
        tmp = N % 50000
        count_cash[1] = int(tmp / 10000)
        tmp = tmp % 10000
        count_cash[2] = int(tmp / 5000)
        tmp = tmp % 5000
        count_cash[3] = int(tmp / 1000)
        tmp = tmp % 1000
        count_cash[4] = int(tmp / 500)
        tmp = tmp % 500
        count_cash[5] = int(tmp / 100)
        tmp = tmp % 100
        count_cash[6] = int(tmp / 50)
        tmp = tmp % 50
        count_cash[7] = int(tmp / 10)
        # test_case와 함께 결과를 출력한다.
        print(f'#{test_case}')
        print(*count_cash)

