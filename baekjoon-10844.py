import sys

input = sys.stdin.readline

n = int(input()) # 1 <= n <= 100
# 1,000,000,000으로 나눈 나머지 출력

# dp_array = [[0]*10 for _ in range(n+1)]
# print(dp_array)

def dp(n):
    dp = [[0]*10 for _ in range(n+1)]  # 처음에는 모두 0으로 초기화
    for i in range(1, 10):
        dp[1][i] = 1 # 10개의 칸, 첫번째 칸은 항상 0
    for i in range(2, n+1): # 새로운 for문, 위의 것이랑 다름, 0번째도 카운트가 가능해짐
        for j in range(10):
            if j == 0:
                dp[i][j] = dp[i-1][1] 
            elif j == 9:
                dp[i][j] = dp[i-1][8]
            else:
                dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]
    return dp[n]


print(sum(dp(n))%1000000000)
            
    