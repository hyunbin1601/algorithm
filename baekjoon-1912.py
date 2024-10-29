# https://www.acmicpc.net/problem/1912
# 다이나믹 프로그래밍 문제

import sys
input = sys.stdin.readline

n = int(input())
number_array = [int(x) for x in input().split()] # input().split() returns a list of strings, n개 정수를 입력받아 리스트로 저장

def dp(n, array):
    dp = [0] * n
    dp[0] = array[0] # 우선 인자로 받은 배열의 첫번째 원소를 dp[0]에 넣어줌
    for i in range(1, n): # 1부터 n-1까지 반복
        dp[i] = max(dp[i-1] + array[i], array[i]) # dp의 각 배열 원소에는 지금까지 배열원소의 합이 들어가는데, 최댓값을 구하기 위해 만약 좀 더 작아졌다? -> 그러면 그냥 array[i]를 넣는다...
    return max(dp) # dp의 최댓값을 반환

print(dp(n, number_array)) # 연속된 수의 합 중 가장 큰 값을 출력
    