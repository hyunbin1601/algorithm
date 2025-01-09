import sys

input = sys.stdin.readline

n = int(input())

def is_safe(queen, row, col): # 현재 퀸의 위치가 안전한지 확인
    for r in range(row): # 같은 열에 있는지, 대각선에 있는지 확인
        if queen[r] == col or abs(queen[r] - col) == row - r:
            return False
    return True

def back_tracking(row, cols, diag1, diag2):  # 열, 대각선1, 대각선2에 퀸이 있는지 추적
    if row == n:
        return 1  # 행의 값이 n과 같아질 때 return하고 재귀를 멈춤
    
    count = 0
    for col in range(n):
        if col not in cols and (row - col) not in diag1 and (row + col) not in diag2:
            cols.add(col)
            diag1.add(row-col)
            diag2.add(row+col)
            count += back_tracking(row+1, cols, diag1, diag2)
            cols.remove(col)
            diag1.remove(row-col)
            diag2.remove(row+col)
    return count

print(back_tracking(0, set(), set(), set()))  # 0행부터 시작
            


