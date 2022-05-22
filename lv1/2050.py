# 알파벳들을 string type으로 입력받는다.
alphabets = input()
# 알파벳들을 아스키코드를 통해 숫자로 변환한다.
for i in alphabets:
    print(ord(i)-64, end=" ")