# 맨 처음 테스트 케이스의 수를 제시해준다고 하였으므로 T에 할당합니다.
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    #테스트 케이스를 입력받아 allNumbers에 int list로 할당합니다.
    allNumbers = list(map(int, input().split()))
    #빈 list인 oddNumbers를 만들고 allNumbers의 각 성분이 홀수인 경우에만 oddNumbers에 추가합니다.
    oddNumbers = list()
    for nums in allNumbers:
        if nums % 2 == 1:
            oddNumbers.append(nums)
    # 테스트 케이스 수와 함께 oddNumbers의 합을 출력합니다. 
    print(f'#{test_case} {sum(oddNumbers)}')