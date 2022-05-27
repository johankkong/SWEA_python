# 1부터 주어진 숫자까지의 합을 출력하는 문제
num_ = int(input())
# for문을 활용하여 합을 더한다.
ans_ = 0
for i in range(1, num_+1):
    ans_ += i
# 합을 출력한다.
print(ans_)