# 주어진 자연수의 모든 자릿수의 합을 구하는 문제
# 주어진 자연수를 T에 할당
T = int(input())
# answer 변수에 일의 자리를 더하고 T를 10으로 나누어 주는 것을 반복한다.
answer = 0
# 10으로 나누고 int로 type cast 시켜주고 T가 0일 될때까지 반복한다.
while T > 1:
    answer += T % 10
    T = int(T/10)
print(answer)