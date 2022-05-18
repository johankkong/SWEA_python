# SWEA_python

SW Expert Academy_python 풀이모음입니다.

## LEVEL 1

### 2071

22.05.18 풀이

주어진 10개 정수의 평균을 구해 소수점 첫째 자리에서 반올림하는 문제

test_case를 T에 할당하여 T만큼 반복하는 것은 예시로 주어져 있었다.

test_case를 받아 빈칸을 기준으로 나눠 list화(`list(map(int, input().split()))`)한 후

그 list의 합을 10으로 나누어 실행시켰지만, 소수점에서 반올림하는 코드를 작성해야했다.

반올림 코드를 작성하기 위해 평균을 정수화하고 빼는 것을 통해 소수점만 남겨 0.5와 비교하여 크다면 올리고 작으면 버리는 작업을 수행하도록 했다.

> 핵심

소수점 첫째 자리에서 반올림

`if average_ - int(average_) >= 0.5:`
`      	    average_ = int(average_) + 1`
`else:`
`average_ = int(average_)`

### 2072

22.05.17 풀이

test_case 수를 먼저 T에 저장하는 것은 예시에 주어져 있었고 T만큼 반복하며 test_case에서의 홀수의 합을 구하는 문제였다.

test_case를 받아 빈칸을 기준으로 나눠 list화(`list(map(int, input().split()))`)한 후

그 list에서 성분 하나씩 홀수 인지 판단하여 다른 list에 추가하였다.

마지막으로 새롭게 생성된 list의 총합을 구하는 방식으로 출이하였다. 

> 핵심

정수의 나열을 `map(int, input().split())`을 통해 입력받는 것

