# 거꾸로 출력해보아요
# 주어진 숫자부터 0까지 거꾸로 출력하는 프로그램
# DATE : 22.05.19

# 주어지는 숫자를 T에 할당합니다.
T = int(input())
# numbers를 0에서부터 1씩 늘려가며 T에서 뺀 수를 출력합니다.
for numbers in range(0, T + 1):
    print(T - numbers, end = " ")
    # 끝에 end = " " 를 추가해주지 않으면 print할때 마다 줄바꿈이 일어납니다.