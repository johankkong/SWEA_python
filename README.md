# SWEA_python

SW Expert Academy_python 풀이모음입니다.

22.05.17 시작!

## LEVEL 1

### 1545

22.05.19 풀이

자연수 하나를 입력받아 그 수부터 0까지 연달아 출력하는 문제

`for`문을 이용하여 `T`에서 0부터 T까지 빼면서 하나씩 출력하였다.

> 기억해둘 것

`print(T - numbers)`를 할 경우, 매번 줄바꿈이 되어리기때문에

`print(T - numbers, end = " ")`를 이용하였다.

### 1933

22.05.28 풀이

정수 N을 입력받아 N의 약수를 오름차순으로 출력하는 문제

`for`문과 `if`문을 활용하여 1부터 N까지 각 자연수가 약수인지 판별하고 출력하였다.

### 1936

22.05.29 풀이

1대1 가위바위보를 숫자에 대입하여 이긴 사람을 출력하는 문제

비기는 경우는 없으므로 A 가 3이 아닌 경우, 숫자가 더 큰 사람이 이기는 것이며 A가 3인 경우엔 B가 2인 경우에 A가 이기고 나머지는 B가 이기는 것으로 경우의 수를 나누어 풀이하였다.

### 1938

두 개의 자연수에 대한 사칙연산 결과를 출력하는 문제

`print()`함수를 이용하여 각 사칙연산의 결과를 출력하였다.

`/`의 경우 소숫점 아래는 버린다고 하였으므로, `int()`를 이용하여 정수화를 해주었다.

### 2019

22.05.30 풀이

1부터 주어진 숫자만큼 2를 곱해가며 출력하는 문제

이중 `for`문을 활용하였다. 

첫번째 `for`문은 주어진 숫자만큼 반복하게 하는 역할, 두번째 `for`은 거듭제곱을 담당하게 하였다.

### 2025

22.05.27 풀이

1부터 주어진 숫자까지의 합을 구하는 문제

`for`문과 `range()`를 활용하여 1부터 숫자를 더해나가는 것을 반복하여 해결하였다.

### 2027

22.05.26 풀이

주어진 텍스트를 그대로 출력하는 문제

`print`함수에 기본적으로 줄바꿈이 들어가 있기때문에 한 줄 씩 출력해주면 된다.

### 2029

22.05.26 풀이

두 자연수 a와 b를 입력받아 a를 b로 나눈 몫과 나머지를 각각 출력하는 문제

이때 몫을 자연수로 출력해야 하기 때문에 `int(a / b)`로 정수화 해주었다.

### 2043

22.05.24 풀이

세자리 비밀번호를 잊어버린 상태에서, 정답 P와 시도를 시작하는 수 K를 입력받아 몇번만에 비밀번호를 맞출 수 있는지 출력하는 문제

단순히 P에서 K를 빼고 1을 더해서 출력해주면 된다.  

### 2046

22.05.23 풀이

주어진 숫자를 입력받아 그 숫자만큼 #을 출력하는 문제

주어진 숫자만큼 반복하게 되는 `for`을 활용하여 #을 출력하였다.

> 생각해볼 것

`for`문을 활용하지 않고 `"#" * num_`으로 바로 출력해도 된다.

### 2047

22.05.23 풀이

영어 문장을 입력받아 소문자를 대문자로 변환하여 출력하는 문제

`upper()`함수를 이용하여 소문자 알파벳을 대문자로 바꾼 뒤 출력하였다.

> 생각해볼 것

`upper()`함수를 이용하지 않는다면 어떨까?
	`for`문을 활용하여 문자를 하나씩 받아 알파벳 소문자인 경우 아스키코드를 활용하여 대문자 알파벳으로 바꿔주는 방법이 있을 것 같다.

### 2050

22.05.22 풀이

알파벳 나열을 입력받아 A부터 Z를 각각 1부터 26으로 출력하는 문제

알파벳 나열을 `string`으로 입력받고 `for`문을 이용하여 한 글자씩 아스키코드에서 64를 빼주는 것을 통해 숫자로 변환하였다.

> 기억해둘 것

한 문자의 아스키코드를 받는 함수`ord()`를 이용하는 것

### 2056

22.05.21 풀이

8자리 숫자를 입력받아 유효한지 판단하고 유효한 날짜에 대해 날짜 형식으로 `/`를 추가하여 출력하는 문제

8자리 수를 string형태로 입력받고 인덱싱과 int typecast를 통해 유효한 날짜인지 판단하는 코드를 작성하였다.

> 어려웠던 점

- `month_`변수가 4월, 6월, 9월, 11월 중에 하나일 경우를 표현함에 있어서 `and`로 연결하지 않고 `month_ in (4, 6, 9, 11)`방식으로 작성하는 것을 떠올리기까지 오래걸렸다.
- 결과를 출력하는 방식에서 int로 변환한 변수를 사용했더니 맨 앞에 오는 0이 생략되는 문제가 있어, 인덱싱을 이용하여 `print(f'#{test_case} {dateCandidate[0:4]}/{dateCandidate[4:6]}/{dateCandidate[6:8]}')`방식으로 출력하였다.

### 2058

22.05.21 풀이

자연수를 입력받아 각 자릿수를 더한 값을 출력하는 문제

입력받은 자연수를 10씩 나눠가며 일의 자리를 `answer`변수에 더해주는 것을 반복하는 것으로 해결하였다.

> 기억해둘 것

입력받은 자연수를 그냥 10으로 나누기만 한다면 정수가 아니게 되기 때문에 `int(T/10)`을 사용하였다.

### 2063

22.05.20 풀이

홀수개의 점수를 입력받아 중간값을 출력하는 문제

처음에 점수의 갯수가 주어지고 점수가 나열되는데 점수의 갯수를 T에 할당하고 나열된 점수들을 list에 할당하였다.

list를 오름차순으로 배열한뒤 T/2 번째 성분을 출력하였다.

> 기억해둘 것

list를 오름차순으로 정렬하는 메소드 : `list.sort()`
		`sort()` 메소드를 사용하지 않는다면 어떻게 짜야할까?

중간값은 `(T+1)/2` 가 아닌 `(T-1)/2`번째 성분, 따라서 `int(T/2)`를 사용하였다.

### 2068

22.05.20 풀이

10개의 수를 입력받아 가장 큰 수를 출력하는 문제

10개의 수를 list에 저장하고 `max_number`변수를 정의하여 list의 요소 하나씩 비교하며 더 큰 수를 max_number에 할당하였다.

### 2070

22.05.20 풀이

2개의 수를 입력받아 크기를 비교하여 등호 또는 부등호를 출력하는 프로그램

2개의 수를 입력받아 `a, b`에 할당하고 `if`문을 활용하여 크기 비교하여 결과를 출력하였다.

### 2071

22.05.18 풀이

주어진 10개 정수의 평균을 구해 소수점 첫째 자리에서 반올림하는 문제

test_case를 T에 할당하여 T만큼 반복하는 것은 예시로 주어져 있었다.

test_case를 받아 빈칸을 기준으로 나눠 list화(`list(map(int, input().split()))`)한 후

그 list의 합을 10으로 나누어 실행시켰지만, 소수점에서 반올림하는 코드를 작성해야했다.

반올림 코드를 작성하기 위해 평균을 정수화하고 빼는 것을 통해 소수점만 남겨 0.5와 비교하여 크다면 올리고 작으면 버리는 작업을 수행하도록 했다.

> 기억해둘 것

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

> 기억해둘 것

정수의 나열을 `map(int, input().split())`을 통해 입력받는 것

## LEVEL 2

### 1961

22.06.14 풀이

주어진 행렬을 각각 90도 180도 270도 회전시켜 출력하는 문제

행렬과 행렬의 크기를 입력받아, 90도 회전시키는 함수를 만들

```python
for i in range(0, n):
    for j in range(0, n):
        turned_matrix[i][j] = matrix[n - j - 1][i]
```

> 어려웠던 점

행렬끼리는 띄어쓰기 없이 출력하고 행렬사이는 띄어쓰기는 넣어줘야했던 점
	`for`문을 통해서 `end=""`와 `end=" "`를 이용해서 출력하였다.

### 1966

22.06.12 풀이

주어진 숫자들을 오름차순으로 정렬하여 출력하는 문제

숫자의 갯수를 `N`으로 입력받고 숫자 나열을 `list`로 입력받아, `list.sort()`를 이용하여 결과를 출력하였다.

> 생각해볼 점

숫자 갯수 `N`을 이용하지 않은 점 

`sort()`함수를 이용하지 않는다면 어떻게 풀이하는 것이 좋을까?

### 1970

22.06.11 풀이

금액을 입력받아, 최소 화폐 갯수로 표현할 때 각각 몆개의 화폐가 필요한지 출력하는 문제

큰 화폐단위가 많을 수록 최소 화폐 수를 충족하기 때문에 가장 큰 단위부터 나누는 것을 통해 몫을 그 화폐를 갯수, 나머지를 다음 단위로 나누는 것을 반복하여 풀이하였다.

> 생각해볼 점

각 화폐 단위마다 하나하나 코드를 작성하였지만, 따로 함수를 작성하여 풀이해보는 것도 생각해볼만한 것 같다.

### 1974

22.06.10 풀이

스도쿠를 입력받아 규칙을 위반하고 있는지 검증하는 문제

각각 가로, 세로, 네모로 나누어 검증을 하여 위반될 경우 `ans = 0`을 하는 방식으로 풀이하였다.

> 어려웠던 점

각 성분을 다른 성분들과 비교하는 과정에서 자기자신과 비교하는 것을 제외하는 것이 중요했다.
가로, 세로는 비교적 수월했지만, 네모 부분을 검증하는 부분이 어려웠다.
	네모 부분은 각 네모의 좌상단을 지정하고 그 좌상단에서 3 x 3 크기의 부분을 탐색하는 방식으로 진행했는데, 총 6중 `for`문을 사용하여, 비효율적이라는 생각을 하였다. 다른 풀이를 생각해봐야 할 듯하다.

### 1976

22.06.09 풀이

두개의 시간을 입력받아 두 시간을 더해 그 결과를 출력하는 문제

분끼리 더해서 60으로 나눈 나머지로 결과 분을 계산하였다.

분끼리 더한 결과가 60을 넘을 경우 시를 더한 값에 1을 더해주는 방식으로 계산하였다.

> 어려웠던 점

시의 범위가 1 ~ 12 이므로 12로 나눈 나머지를 이용할 경우 12를 출력하지 못하는 어려움이 있었다.
	12로 나눈 나머지를 계산하기 전에 1을 빼고 나머지를 계산한 뒤에 1을 더해주는 방식을 채택하였다.

### 1979

22.06.08 풀이

N x N 크기의 낱말퍼즐에서 K 길이의 빈칸이 몇개 있는지 출력하는 문제

N x N 크기의 matrix로 입력받아 연속된 1의 길이가 K 인 경우가 몇개 인지 판단하도록 하였다.

가로와 세로로 나누어 `for`문을 통해 1인 경우 `tmp`변수에 1을 더하고 0을 만나거나 행 또는 열의 끝을 만나면 `tmp`의 크기가 `K`와 같은 지 판단하여 같은 경우 `ans`변수에 1을 더하는 방식으로 풀이하였다.

> 기억해둘 것

N x N matrix를 간편하게 입력받는 방법
	`[list(map(int, input().spilt())) for _ in range(N)]`

구간을 나누어 탐색하기 보단 알아서 구간이 되도록 하는 방식이 훨씬 수월하다.

### 1983

22.06.05 풀이

N명의 성적을 입력 받아 K번째 학생의 학점을 출력하는 문제

중간고사, 기말고사, 과제 성적을 하나의 `list`로 입력받아 2차원 `list`를 만든다.

각각의 `list`를 총점으로 계산하여 다시 `list`를 만든다.

K번째 학생의 총점을 다른 변수에 저장한 후, `list`를 오름차순으로 정렬한다.

그 다음 K번째 학생의 점수가 `list`를 10개의 그룹중에서 몇 번째 그룹에 속해있는지 확인하고 성적을 출력하였다.

> 기억해둘 것

`list`를 정렬할 경우, `list.sort()`를 하면 되는데 `list = list.sort()`를 하면 에러가 난다.

index를 할 때는 반드시 정수여야한다. 예를 들어, `10 / 10`일 지라도 그 결과가 `1.0`이기때문에 index로 사용하고 싶다면 `list[int(10/10)]`으로 해줘야한다.

### 1984

22.06.04 풀이

10개의 수를 입력받아 최대 수와 최소 수를 제외한 8개 수의 평균을 구하는 문제

10개의 수를 `list`로 입력받아 `max()`, `min()`, `sum()` 함수를 이용하여 8개 수의 평균을 구하였다.

마지막으로 소수점 첫째자리에서 반올림해주는 작업으로 마무리해주었다.

> 기억해둘 것

`list`에서 최댓값과 최솟값을 구하는 함수는 `max(list)`, `min(list) `이다.

반올림하는 과정

### 1986

22.06.03 풀이

1부터 `N`까지 홀수는 더하고 짝수는 빼는 것의 합산을 구하는 문제

`N`을 입력받아 `for`문을 통해 1부터 N까지 반복하였고 `if`문을 통해 홀수일 경우 더하고 짝수일 경우 빼주는 작업을 진행하였다.

> 기억해둘 것

1부터 `N`까지의 수를 고려해야 하므로 `range(1, N + 1)`을 사용해야한다.

### 1989

22.06.02 풀이

앞뒤 어디로 읽어도 같은 단어인 회문인지 판단하는 문제

문자열을 입력받아 `for`문을 이용하여 각 문자가 반대편 뒤쪽의 문자열과 같은지 판단하는 방식으로 풀이하였다.

> 기억해둘 것

`list`혹은 `string`에서 indexing을 할때 맨 처음은 `list[0]`이고 맨뒤는 `list[-1]`이다.

`flag`를 이용하여 특정 조건에서만 `flag = False`를 할당하는 방식이 유용하다.

### 2001

22.06.02 풀이

N x N 크기의 배열안의 M x M 크기의 배열 중 그 합의 최댓값을 구하는 문제

N x N 크기의 배열을 `list`안의 `list`로 입력받았고, 이중 `for`문을 이용하여 모든 M x M 배열을 탐색하였다.

M x M 배열의 합은 `for`문과 `sum()`함수를 이용하여 구했다.

한번 합을 구할때마다 `max`와 비교하여 더 크다면 `max`를 갱신하는 방식으로 풀이하였다.

> 기억해둘 것

2차원 `list`에서 `sum([i][j:j+k])`와 같이 내부 `list`의 부분 합을 구할 수 있다.

### 2005

22.06.01 풀이

주어진 정수의 크기를 갖는 파스칼 삼각형을 출력하는 문제

각 줄을 `list`로 생각하여 이전 줄을 입력받아 다음줄을 `return`하는 함수를 만들어 사용하고자 하였다.

이전줄의 앞에 0을 추가한 `list`와 뒤에 0을 추가한 `list`의 각 요소를 더하는 방식으로 다음줄을 구하는 함수를 작성하여 풀이하였다.

> 기억해둘 것

`[0] * 5`의 결과값은 `[0, 0, 0, 0, 0]`이다.

`list`의 길이를 구하는 함수는 `len(list)`이다.

`print(*list)`를 통해 `list`를 해체하여 출력이 가능하다.

### 2007

22.05.31 풀이

패턴에서 반복되는 부분을 마디라고 할 때, 문자열에서 마디의 길이를 출력하는 문제

30개의 문자열을 `string`형태로 입력받아 1부터 10까지의 길이로 끊어 바로 다음과 일치하는 코드를 작성하여 해결하였다.

> 기억해둘 것

`string[a:b]`일 때, `b-1`까지 출력된다는 것

`for`이나 `while`문에서 `break`를 통해 반복문을 종료하는 것

> 생각해볼 것

마디의 최대길이가 정해지지 않았다면? 
`while True:`로 마디의 길이가 나올때까지 반복!



