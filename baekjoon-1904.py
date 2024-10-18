import sys
input = sys.stdin.readline

n = int(input())

# 결국 현재 1 하나만으로 이루어진 타일 또는 0타일을 두 개 붙인 한 쌍의 00타일들만이 남게 되었다. -> 0011, 0000, 1001, 1100, 1111 이런 식으로 나옴

# 1. 1타일로만 이루어진 타일의 개수
# 2. 00타일로만 이루어진 타일의 개수

def dp(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        dp = [0] * (n+1)
        dp[1] = 1
        dp[2] = 2
        for i in range(3, n+1):
            dp[i] = (dp[i-1] + dp[i-2]) % 15746
        return dp[n]
    
print(dp(n))