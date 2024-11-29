import sys
input = sys.stdin.readline

t = int(input())

dp = [0] * 101 # 100번째 값을 저장하는 동적 계획법 문제

def dp_padoban(n):
    dp[1] = 1
    dp[2] = 1
    dp[3] = 1
    dp[4] = 2
    dp[5] = 2
    for i in range(6, n+1):  # 6번째부터 n번째까지 dp에 저장
        dp[i] = dp[i-1] + dp[i-5]
    return dp[n] # t번째 값(dp 배열의 마지막 값) 반환


for _ in range(t):
    n = int(input())
    print(dp_padoban(n))
    
