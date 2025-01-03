import sys
input = sys.stdin.readline

# 동적 계획법과 최단거리 역추적
# 1로 만들기

# X가 3으로 나누어 떨어지면, 3으로 나눈다.
# X가 2로 나누어 떨어지면, 2로 나눈다.
# 1을 뺀다.
# 이렇게 해서 1을 만들고자 할때, 연산 사용 횟수의 최솟값 구하기
# 1 <= X <= 1000000

x = int(input())

# 출력값 첫째줄에는 연산횟수 최솟값
# 둘째줄에는 N을 1로 만드는 방법에 포함되어 있는 수 출력

dp = [0] * 1000001

def dp_programming(x):
    for i in range(2, x+1): # dp는 1부터 시작하므로
        dp[i] = dp[i-1] + 1  # dp에는 인덱스 i일때 연산 횟수가 저장된다
        if i % 2 == 0:
            dp[i] = min(dp[i], dp[i//2] + 1)
        if i % 3 == 0:
            dp[i] = min(dp[i], dp[i//3] + 1)
    return dp[x]

def trace(x):
    if x != 1:
        if x % 3 == 0 and dp[x] == dp[x//3] + 1:  # 위의 dp_programming 함수에서 계산한 이후 적용
            print(x, end=' ')
            trace(x // 3)  # 재귀함수 사용, 1이 될 때까지 print 후 계속 반복함
        elif x % 2 == 0 and dp[x] == dp[x//2] + 1:
            print(x, end=' ')
            trace(x // 2)
        else:
            print(x, end=' ')
            trace(x - 1)
    else:
        print(1, end=' ')


print(dp_programming(x))
trace(x)