import sys
input = sys.stdin.readline

line = int(input())
quadtree = []

for _ in range(line):
    quadtree.append(list(map(int, input().strip())))
    
def divide_and_conquer(x, y, n):
    color = quadtree[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if color != quadtree[i][j]:
                print("(", end="")   # 만약 색이 일치하지 않는다면 일단 ()를 출력
                divide_and_conquer(x, y, n//2)   # input 값이 y 기준으로 역순으로 들어오기 때문에 오른쪽으로 이동 -> y축 기준으로 이동한다고 생각하면 될 듯
                divide_and_conquer(x, y+n//2, n//2)  # [[11110000][11110000][00011100][00011100][11110000] ~] 이런 식으로 들어옴
                divide_and_conquer(x+n//2, y, n//2)
                divide_and_conquer(x+n//2, y+n//2, n//2)  # x, y는 x는 행, y는 열의 의미로 생각해야 한다. 0부터 시작하고, 만약 quadtree[2][3]일 경우, x는 3번째 행, y는 4번째 열을 가리킨다. 즉 1
                print(")", end="")
                return
    print(color, end="")
    
divide_and_conquer(0, 0, line)