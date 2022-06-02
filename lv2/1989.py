# 주어진 문자열이 거꾸로 읽어도 같은 문자열인지 판단하는 문제
T = int(input())
for test_case in range(1, T + 1):
    word_ = input()
    flag = True
    for i in range(0, int(len(word_)/2)):
        # 문자열의 앞뒤를 비교해가며 다른 문자가 발견 될 경우 flag를 False로 변경하고 for문을 빠져나온다.
        if word_[i] != word_[-(i+1)]:
            flag = False
            break
    # flag에 따라 1과 0을 출력한다.
    if flag:
        print(f'#{test_case} {1}')
    else:
        print(f'#{test_case} {0}')