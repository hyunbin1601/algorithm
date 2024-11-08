import sys
input = sys.stdin.readline

## 동적 계획법 문제 ##
## 백준 1932 https://www.acmicpc.net/problem/1932 ##

n = int(input())
triangle = []

# 삼각형의 값 입력받음
for _ in range(n):
    triangle.append(list(map(int, input().split())))
    
# dp를 사용하기 위한 dp 테이블 초기화
dp = [[0] * (i+1) for i in range(n)] # 삼각형의 크기만큼 0으로 초기화
# 첫번째에는 [0] 1개, 두번째에는 [0] 2개,...이렇게 생성되기 위해서 (i+1)을 곱해줌
dp[0][0] = triangle[0][0] # 첫번째 삼각형의 값은 그대로 dp에 저장 -> 기본적으로 최댓값을 구하기 위해선 첫번째 삼각형은 무조건 더해야함

for i in range(1, n):
    for j in range(i+1):
        if j == 0: # 삼각형의 가장 왼쪽 값일 경우, j값이 커진다 -> 가로 오른쪽으로 이동한다
            dp[i][j] = dp[i-1][j] + triangle[i][j]
        elif j == i: # 삼각형의 가장 오른쪽 값일 경우
            dp[i][j] = dp[i-1][j-1] + triangle[i][j]
        else: # 가장 왼쪽도 가장 오른쪽도 아닐 때
            dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + triangle[i][j]
            
print(max(dp[n-1])) # dp 테이블의 세로줄은 총 n개, 그러므로 최대 인덱스는 n-1
# dp 테이블의 가장 마지막 줄의 max 값 출력