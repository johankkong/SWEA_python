# 입력받는 점수의 갯수 T
T = int(input())
# 점수의 나열을 list에 할당
score_list = list(map(int, input().split()))
# list를 오름차순으로 배열
score_list.sort()
# 배열된 list의 중간값인 T/2 번째 성분을 출력한다.
print(score_list[int(T / 2)])