
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # 날짜를 표시하는 8자리 수를 string type으로 입력받는다.
    dateCandidate = input()
    # 각 자리에 해당하는 연, 월, 일로 int로 type cast를 진행한다.
    year_ = int(dateCandidate[0:4])
    month_ = int(dateCandidate[4:6])
    day_ = int(dateCandidate[6:8])
    # 날짜가 유효한지 판단한다.
    if month_ < 1 or month_ > 12 or day_ < 1 or day_ > 31:
        print(f'#{test_case} -1')
    elif month_ == 2 and day_ > 28:
        print(f'#{test_case} -1')
    elif month_ in (4, 6, 9, 11) and day_ > 30:
        print(f'#{test_case} -1')
    else:
        print(f'#{test_case} {dateCandidate[0:4]}/{dateCandidate[4:6]}/{dateCandidate[6:8]}')
