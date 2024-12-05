import sys
input = sys.stdin.readline

# https://www.acmicpc.net/problem/25682
# 누적 합 문제
# python3에서 자꾸 시간초과 에러가 난다면 pypy3에서 실행해보자
# pypy3는 jit compiler를 사용하기 때문에 좀 더 빠른 실행가능
# pypy와 python은 대부분 호환되지만 일부 c 모듈은 호환되지 않을 수 있음주의

n, m, k = map(int, input().split())

chess = []

chess = [input().strip() for _ in range(n)] 
    
# 체스판의 각 칸이 체스판 규칙에 맞지 않는 경우 -> 누적 합 배열에 저장
# 체스판의 규칙은 무조건 B와 W가 번갈아가면서 나와야함

sum_b = [[0] * (m + 1) for _ in range(n + 1)] # B로 시작하는 체스판의 누적 합
sum_w = [[0] * (m + 1) for _ in range(n+1)] # W로 시작하는 체스판의 누적 합

for i in range(1, n+1):
    for j in range(1, m+1):
        add_b = 0  # 현재 칸을 B로 시작하는 경우 추가 값
        add_w = 0  # 현재 칸을 W로 시작하는 경우 추가 값
        if (i+j) % 2 == 0:
            if chess[i-1][j-1] == 'B':  # 체스칸이 B로 시작하는 경우
                sum_b[i][j] = sum_b[i-1][j] + sum_b[i][j-1] - sum_b[i-1][j-1]
                sum_w[i][j] = sum_w[i-1][j] + sum_w[i][j-1] - sum_w[i-1][j-1] + 1  # w로 시작하는 체스칸을 수정해야함
            else: # 체스칸이 W로 시작하는 경우
                sum_b[i][j] = sum_b[i-1][j] + sum_b[i][j-1] - sum_b[i-1][j-1] + 1 # b로 시작하는 체스칸을 수정해야함
                sum_w[i][j] = sum_w[i-1][j] + sum_w[i][j-1] - sum_w[i-1][j-1]

        else:
            if chess[i-1][j-1] == 'B': # 체스칸이 W로 시작하는 경우
                sum_b[i][j] = sum_b[i-1][j] + sum_b[i][j-1] - sum_b[i-1][j-1] + 1
                sum_w[i][j] = sum_w[i-1][j] + sum_w[i][j-1] - sum_w[i-1][j-1]
            else: # 체스칸이 B로 시작하는 경우
                sum_b[i][j] = sum_b[i-1][j] + sum_b[i][j-1] - sum_b[i-1][j-1]
                sum_w[i][j] = sum_w[i-1][j] + sum_w[i][j-1] - sum_w[i-1][j-1] + 1
    
min_paint = float('inf')   # min_paint라는 변수를 infinite, 즉 무한대로 초기화하겠다는 의미, 이는 이후 계산값이 이 초기값보다 작을 때마다 갱신하기 위함        
for i in range(k, n+1):   # k가 될 수 있는 값의 범위는 n-k+1 까지이므로
    for j in range(k, m+1): # k가 될 수 있는 값의 범위는 m-k+1 까지이므로
        min_paint = min(min_paint, sum_b[i][j] - sum_b[i-k][j] - sum_b[i][j-k] + sum_b[i-k][j-k]) # sum_b[i-k][j]는 k*k의 위쪽 영역, sum_b[i][j-k]는 k*k의 왼쪽 영역, 두번 빠진 부분을 sum_b[i-k][j-k]를 통해 더해줌
        min_paint = min(min_paint, sum_w[i][j] - sum_w[i-k][j] - sum_w[i][j-k] + sum_w[i-k][j-k])
    
print(min_paint) 