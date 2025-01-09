import sys

input = sys.stdin.readline

n = int(input())

def is_safe(queen, row, col): # 현재 퀸의 위치가 안전한지 확인
    for r in range(row): # 같은 열에 있는지, 대각선에 있는지 확인
        if queen[r] == col or abs(queen[r] - col) == row - r:
            return False
    return True

def back_tracking(queen, row, n):  # 행 단위로 계산함
    if row == n:
        return 1  # 행의 값이 n과 같아질 때 return하고 재귀를 멈춤
    
    count = 0
    for col in range(n): # col = 0, 1, 2,...., n-1
        if is_safe(queen, row, col):  # 0번째 열, 0번째 행부터 시작
            queen[row] = col # is_safe의 값이 true일 경우, row번에 col 값을 넣음
            count += back_tracking(queen, row+1, n)
    return count

queen = [-1] * n
print(back_tracking(queen, 0, n))
