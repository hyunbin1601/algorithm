import sys
input = sys.stdin.readline
line = int(input())

paper = [list(map(int, input().split())) for _ in range(line)] 
zero = 0
one = 0
minus_one = 0

def divide_and_conquer(x, y, n):
    global zero, one, minus_one
    color = paper[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if color != paper[i][j]:
                divide_and_conquer(x, y, n//3)
                divide_and_conquer(x, y+n//3, n//3)
                divide_and_conquer(x, y+2*n//3, n//3)
                divide_and_conquer(x+n//3, y, n//3)
                divide_and_conquer(x+n//3, y+n//3, n//3)
                divide_and_conquer(x+n//3, y+2*n//3, n//3)
                divide_and_conquer(x+2*n//3, y, n//3)
                divide_and_conquer(x+2*n//3, y+n//3, n//3)
                divide_and_conquer(x+2*n//3, y+2*n//3, n//3)
                return
    if color == 0:
        zero += 1
        return
    elif color == 1:
        one += 1
        return  
    else:
        minus_one += 1
        return

divide_and_conquer(0, 0, line)
print(minus_one)
print(zero)
print(one)
    

