import sys
input = sys.stdin.readline

# 포도주 시식 -> 한번 마신건 모두 마셔야 하고, 연속으로 놓여있는 3잔을 모두 마실순 x
# n개의 포도주 잔 -> 최대한 많은 양의 포도주 마셔야함

n = int(input())

wine = [int(input()) for _ in range(n)]
# 입력값을 배열로 저장
# 동적 계획법 사용 문제

dp = [0] * n  # dp배열을 0번부터 n-1번까지 생성

def wine_dp(n):
    if n == 1:
        return wine[0]
    elif n == 2:
        return wine[0] + wine[1]
    elif n == 3:
        return max(wine[0] + wine[2], wine[1] + wine[2], wine[0] + wine[1])
    else:
        dp[0] = wine[0]
        dp[1] = wine[0] + wine[1]
        dp[2] = max(wine[0] + wine[2], wine[1] + wine[2], dp[1])
        for i in range(3, n):
            dp[i] = max(dp[i-3] + wine[i-1] + wine[i], dp[i-2] + wine[i], dp[i-1])
        return dp[n-1]

print(wine_dp(n))