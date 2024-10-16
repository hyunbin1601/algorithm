import sys
input = sys.stdin.readline

dp = [[[0] * 21 for _ in range(21)] for _ in range(21)] # 3차원 배열 생성
# 만약 배열의 값이 0이 아니면 -> 값이 저장되어 있으므로 그대로 쓰고, 0이면 연산해서 값을 저장함(memoization)

# 기본 조건설정
for i in range(21):  # 21x21x21 배열 설정 -> 어차피 20 기준으로 값이 정해지므로 0에서 20까지만 설정 -> 총 범위는 21개
    for j in range(21):
        for k in range(21):
            if i <= 0 or j <= 0 or k <= 0:
                dp[i][j][k] = 1
            elif i < j and j < k:
                dp[i][j][k] = dp[i][j][k-1] + dp[i][j-1][k-1] - dp[i][j-1][k]   # 재귀함수를 호출하는 형식이 아니라 배열을 하나 정해 해당 배열에 값을 넣어주는 형식으로 구현(memoization)
            else:
                dp[i][j][k] = dp[i-1][j][k] + dp[i-1][j-1][k] + dp[i-1][j][k-1] - dp[i-1][j-1][k-1]
                
def w(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    if a > 20 or b > 20 or c > 20:
        return dp[20][20][20]
    return dp[a][b][c]  # 이미 위에서 조건을 설정했기 때문에 그냥 dp[a][b][c]만 해도 된다.

while True:
    a, b, c = map(int, input().split())
    
    if a == -1 and b == -1 and c == -1:
        break
    print(f"w({a}, {b}, {c}) = {w(a, b, c)}")   # f-string을 사용하여 출력, w(a, b, c) = dp[a][b][c]와 같다. f-string을 통해 함수를 호출하여 출력할 수 있다