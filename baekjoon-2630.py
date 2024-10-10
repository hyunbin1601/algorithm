import sys
input = sys.stdin.readline

line = int(input())  # 몇 줄 입력받을 것인지
paper = []
for _ in range(line):
    paper.append(list(map(int, input().split())))   
    
blue = 0
white = 0
# n = 4일때를 먼저 계산해서 검증
    
def divide_and_conquer(x, y, n):
    global white, blue  # 전역변수를 함수 안에서 변경 가능할 수 있도록 미리 global로 선언
    color = paper[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if color != paper[i][j]:
                divide_and_conquer(x, y, n//2)   # 정수 부분만 반환, 즉 5 // 2일때 2를 반환한다는 의미
                divide_and_conquer(x, y+n//2, n//2)
                divide_and_conquer(x+n//2, y, n//2)
                divide_and_conquer(x+n//2, y+n//2, n//2)
                return  # 함수 자체를 종료함
    if color == 0:
        white += 1
        return
    else:
        blue += 1
        return

divide_and_conquer(0, 0, line)    
print(blue)
print(white)
                
    