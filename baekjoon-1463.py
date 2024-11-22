import sys

input = sys.stdin.readline

# 정수 X에 사용할 수 있는 연산은 다음과 같이 세 가지 이다.

# X가 3으로 나누어 떨어지면, 3으로 나눈다.
# X가 2로 나누어 떨어지면, 2로 나눈다.
# 1을 뺀다.
# 정수 N이 주어졌을 때, 위와 같은 연산 세 개를 적절히 사용해서 1을 만들려고 한다.

# 연산을 하는 횟수의 최솟값 구하기
# 동적 계획법 사용

n = int(input())

def memoization(n):
    dp = [0] * (n + 1) # 0으로 초기화
    if n == 1:
        return 0
    elif n == 2:  # dp[0]은 그냥 0으로 둔다.(인덱스 값, dp에 저장된 값은 횟수, 인덱스는 n 숫자가 주어졌다는 의미)
        dp[2] = 1
    elif n == 3:
        dp[3] = 1
    else:
        dp[2] = 1
        dp[3] = 1
        for i in range(3, n+1):
            dp[i] = dp[i-1] + 1
            if i % 2 == 0:
                dp[i] = min(dp[i], dp[i//2] + 1)  # //는 몫을 구하는 연산자
            if i % 3 == 0:
                dp[i] = min(dp[i], dp[i//3] + 1)
    return dp[n]

print(memoization(n))