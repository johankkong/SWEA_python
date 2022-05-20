T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # 두 개의 숫자를 입력받아 a, b에 할당한다.
    a, b = map(int, input().split())
    # 두 수를 비교하여 부등호를 출력한다.
    if a == b:
        print(f"#{test_case} =")
    elif a > b:
        print(f"#{test_case} >")
    else:
        print(f"#{test_case} <")
