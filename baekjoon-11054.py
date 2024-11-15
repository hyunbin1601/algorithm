import sys
input = sys.stdin.readline

# https://www.acmicpc.net/problem/11054
# 가장 긴 바이토닉 부분 수열문제, 동적 계획법 사용

n = int(input())
bls_array = list(map(int, input().split()))
# bls 수열 생성

def bls_dp(n, bls_array):
    dp = [1] *n # dp 배열생성
    for i in range(n):
        for j in range(i):
            if bls_array[i] > bls_array[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    return dp

dp1 = bls_dp(n, bls_array)

bls_array.reverse() # bls_array를 뒤집어준다 -> reverse 함수는 리스트를 뒤집어주는 함수

dp2 = bls_dp(n, bls_array) # 뒤집은 bls_array를 dp함수에 넣어준다

dp2.reverse() # dp2를 다시 뒤집어준다

result = [dp1[i] + dp2[i] -1 for i in range(n)] # dp1과 dp2를 더해준다

print(max(result)) # 최댓값을 출력해준다 -> 왜 1을 빼는거야? 
# dp1과 dp2를 더해줄 때, 중복되는 값이 생기기 때문에 1을 빼준다
# 1개 이상 중복된 값이 생길 수 있지않아? -> 중복된 값이 생기면, dp1과 dp2의 값이 같아지기 때문에, 중복된 값이 생기지 않는다