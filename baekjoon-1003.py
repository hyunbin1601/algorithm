import sys
input = sys.stdin.readline

# https://www.acmicpc.net/problem/1003
# 피보나치 함수 문제
# 동적 프로그래밍 알고리즘을 활용한 문제
# fibonacci(n)을 호출
# 총 0과 1이 각각 몇번 출력되었는지 구해야함

t = int(input()) # test case

for _ in range(t):
    n = int(input())
    dp = [[0, 0] for _ in range(n+1)] # 0부터 n까지 dp 배열을 생성해야 하므로
    # dp=[[0, 0] * (n+1)] 과도 같다
    # 여기서 [0, 0]이 의미하는것 -> 0번째 인덱스는 0이 몇번 나왔는지, 1번째 인덱스는 1이 몇번 나왔는지
    # dp[0][0] = 1 # 0번째(0일때) 0이 1번 나옴
    # dp[1][1] = 1 # 1번째(1일때) 1이 1번 나옴
    
    
    # 위의 고정값 설정은 인덱스 오류를 발생시킴 -> n=0, n=1일때 dp 배열에서 위의 값까지 범위가 확장되지 않았으므로
    if n == 0:
        print("1 0")
        continue
    elif n == 1:
        print("0 1")
        continue
    
    dp = [[0, 0] for _ in range(n+1)] # 0부터 n까지 dp 배열을 생성해야 하므로
    dp[0] = [1, 0] # 0일때 0이 1번 나옴
    dp[1] = [0, 1] # 1일때 1이 1번 나옴
    dp[2][0] = 1 # 2일때 0이 1번 나옴
    dp[2][1] = 1 # 2일때 1이 1번 나옴
    
    
    for i in range(3, n+1):
        dp[i][0] = dp[i-1][0] + dp[i-2][0]
        dp[i][1] = dp[i-1][1] + dp[i-2][1]
        
    print(dp[n][0], dp[n][1]) # n번째 인덱스에서 0과 1이 각각 몇번 나왔는지 출력