# 패턴에서 반복되는 부분을 마디라고 할 때, 문자열에서 마디의 길이를 출력하는 문제
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # 30자리 문자열을 입력받는다
    pattern_ = input()
    # 마디의 길이는 최대 10이라고 했으므로 1부터 10까지 반복되는 길이를 찾는다.
    for length in range(1, 11):
        if pattern_[0:length] == pattern_[length:length+length]:
            print(f'#{test_case} {length}')
            break