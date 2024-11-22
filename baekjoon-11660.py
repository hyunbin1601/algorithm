import sys

input = sys.stdin.readline

# https://www.acmicpc.net/problem/11660
# 누적 합 문제
#  (x1, y1)부터 (x2, y2)까지 합을 구하는 프로그램 작성

n, m = map(int, input().split())
# 첫째 줄에 표의 크기 N과 합을 구해야 하는 횟수 M이 주어진다. 
# 둘째 줄부터 N개의 줄에는 표에 채워져 있는 수가 1행부터 차례대로 주어진다. 
# 다음 M개의 줄에는 네 개의 정수 x1, y1, x2, y2 가 주어지며, (x1, y1)부터 (x2, y2)의 합을 구해 출력해야 한다. 
# 표의 각 칸에 적힌 수는 1,000보다 작거나 같은 자연수이다.

table = [list(map(int, input().split())) for _ in range(n)]
# 이차원 배열, list(map(int, input().split))으로 2개의 숫자를 받고, 이를 n번 받아서 이차원 배열을 완성

dp = [[0] * (n + 1) for _ in range(n + 1)]
# dp 배열 생성, 0으로 초기화
# 이건 누적 합 문제이므로, dp 배열을 만들어서 누적 합을 저장해놓는다.

for i in range(1, n + 1):
    for j in range(1, n + 1):
        dp[i][j] = dp[i - 1][j] + dp[i][j - 1] - dp[i - 1][j - 1] + table[i - 1][j - 1]
        # dp[i][j] = dp[i - 1][j] + dp[i][j - 1] - dp[i - 1][j - 1] + table[i - 1][j - 1]
        # dp[i][j] = (i, j)까지의 누적 합
        # dp[i - 1][j] = (i - 1, j)까지의 누적 합
        # dp[i][j - 1] = (i, j - 1)까지의 누적 합
        # dp[i - 1][j - 1] = (i - 1, j - 1)까지의 누적 합
        # table[i - 1][j - 1] = (i, j)의 값
        # 이를 이용해서 누적 합을 구한다.
        # 왜 dp[i - 1][j - 1]을 빼주는지는 잘 모르겠다. -> 이건 겹치는 부분을 빼주기 위해서이다.
        
for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    # x1, y1, x2, y2를 입력받음
    print(dp[x2][y2] - dp[x1 - 1][y2] - dp[x2][y1 - 1] + dp[x1 - 1][y1 - 1])
    # dp[x2][y2] - dp[x1 - 1][y2] - dp[x2][y1 - 1] + dp[x1 - 1][y1 - 1]
    # (x1, y1)부터 (x2, y2)까지의 합을 구하는 식
    # dp[x2][y2] = (x2, y2)까지의 누적 합
    # dp[x1 - 1][y2] = (x1 - 1, y2)까지의 누적 합
    # dp[x2][y1 - 1] = (x2, y1 - 1)까지의 누적 합
    # dp[x1 - 1][y1 - 1] = (x1 - 1, y1 - 1)까지의 누적 합
    # 이를 이용해서 (x1, y1)부터 (x2, y2)까지의 합을 구한다.
    # dp[x1 - 1][y1 -1]을 더하는 이유는...? -> 두번 빼준 부분을 다시 더해주기 위해서이다.