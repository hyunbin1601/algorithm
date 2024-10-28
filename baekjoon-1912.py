# https://www.acmicpc.net/problem/1912
# 다이나믹 프로그래밍 문제

import sys
input = sys.stdin.readline

n = int(input())
number_array = [int(x) for x in input().split()] # input().split() returns a list of strings, n개 정수를 입력받아 리스트로 저장

def dp(n, array):
    dp = [0] * n
    dp[0] = array[0] # 첫번째 원소를 dp[0]에 넣어줌
    for i in range(1, n): # 1부터 n-1까지 반복
        dp[i] = max(dp[i-1] + array[i], array[i])
    return max(dp) # dp의 최댓값을 반환

print(dp(n, number_array)) # 연속된 수의 합 중 가장 큰 값을 출력
    