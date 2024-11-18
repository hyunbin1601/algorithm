import sys

input = sys.stdin.readline
# https://www.acmicpc.net/problem/2565
# lis 알고리즘
# 동적 계획법을 이용하자

n = int(input())

lines = [list(map(int, input().split())) for _ in range(n)]
# 이차원 배열, list(map(int, input().split))으로 2개의 숫자를 받고, 이를 n번 받아서 이차원 배열을 완성
# 서로 교차하지 않게 없애야 하는 전깃줄의 최소 개수 출력

lines.sort(key=lambda x: x[0]) # 첫번째 숫자를 기준으로 정렬

dp = [1] * n # dp 배열 생성

def lis_dp(n, lines):
    for i in range(n):
        for j in range(i):
            if lines[i][1] > lines[j][1]:
                dp[i] = max(dp[i], dp[j] + 1)
    return dp

dp = lis_dp(n, lines)  # dp 배열을 함수를 거쳐 완성시킴

print(n - max(dp)) # 전체 전깃줄의 개수에서 가장 긴 증가하는 부분 수열의 길이를 빼줌