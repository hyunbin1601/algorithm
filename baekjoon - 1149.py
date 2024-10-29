import sys
input = sys.stdin.readline

n = int(input())

array = []

for _ in range(n):
    rgb = list(map(int, input().split()))  # i번째 집이 빨강, 파랑, 초록으로 칠하는 비용을 입력받아 리스트에 저장
    array.append(rgb)  # 리스트에 저장
    
# 색칠 비용의 최솟값을 구함
def dp(n, array):
    dp = [[0] * 3 for _ in range(n)] # n x 3의 2차원 배열을 만들어줌
    dp[0] = array[0] # 우선 인자로 받은 배열의 첫번째 원소를 dp[0]에 넣어줌
    for i in range(1, n): # 1부터 n-1까지 반복
        dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + array[i][0] # i번째 집이 빨강으로 칠할 때의 최소 비용
        dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + array[i][1] # i번째 집이 파랑으로 칠할 때의 최소 비용
        dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + array[i][2] # i번째 집이 초록으로 칠할 때의 최소 비용
    return min(dp[n-1]) # dp의 마지막 행의 최소값을 반환

print(dp(n, array)) # 색칠 비용의 최솟값을 출력