import sys

input = sys.stdin.readline

n = int(input())

arr = list(map(int, input().split()))  # n개의 요소를 받음

# 최장증가수열(lis) 찾기 -> dp 알고리즘 이용

def lis(n, arr):
    dp = [1] * n # 초기 dp 배열은 1로 초기화
    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j]:
                dp[i] = max(dp[i], dp[j]+1)
    return max(dp)

print(lis(n, arr))
