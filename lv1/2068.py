from ssl import ALERT_DESCRIPTION_UNEXPECTED_MESSAGE


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # 10개의 수를 입력받아 list에 할당한다.
    numbers = list(map(int, input().split()))
    # 최댓값을 할당할 변수를 정의해준다.
    max_number = numbers[1]
    # numbers의 각 요소와 하나씩 비교하며 더 큰 값을 max_number 에 저장한다.
    for eachNumber in numbers:
        if max_number < eachNumber:
            max_number = eachNumber
    # test_case 번호와 함께 출력한다.
    print(f'#{test_case} {max_number}')
    
