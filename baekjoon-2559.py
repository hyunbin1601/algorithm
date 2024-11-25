import sys

input = sys.stdin.readline

# 누적 합 문제
# dp 배열에 지금까지 더한 합의 값 저장

n, m = map(int, input().split())

number_array = list(map(int, input().split()))  # 숫자가 저장될 배열
# print(number_array)

dp = [0] * (n + 1) # 0으로 초기화, 왜 n+1로 했냐? -> 0번째 인덱스를 사용하기 위해서???? -> 어디다? -> dp[0]은 0이라 의미가 없음

for i in range(1, n+1):
    # 1부터 n까지 반복
    dp[i] = dp[i-1] + number_array[i-1] # dp[i]는 1부터 i까지의 합을 저장함, dp를 n+1 길이의 배열로 만든 이유는 이렇게 dp[i-1]에서의 상황을 고려하기 위해서!
    # dp[i]는 1부터 i까지의 합을 저장함, dp[i-1]은 1부터 i-1까지의 합을 저장하고 있음
    
maximum = dp[m] - dp[0]

def sum_interval(start, end):
    return dp[end] - dp[start-1] # start부터 end까지의 합을 구함, dp[start-1]은 start-1까지의 합을 의미함
    
for i in range(1, n-m+2):  # dp[1]은 1번째까지의 누적합이라고 생각, 인덱스가 number_array와 dp의 인덱스가 조금 다르다!
    maximum = max(maximum, sum_interval(i, i+m-1)) # maximum은 max함수를 사용하여 maximum과 sum_interval(i, i+m-1) 중 큰 값을 저장함
    
print(maximum) # 최댓값 출력


