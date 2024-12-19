import sys
input = sys.stdin.readline

# 테스트 케이스 입력
t = int(input())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]  # 상하좌우 이동
count = [0] * t # 테스트 케이스만큼 배열 생성
# count는 각 테스트 케이스에 대해 필요한 최소 배추흰지렁이수

def dfs(x, y, cabbage_map, visited, n, m):
    stack = [(x, y)]
    while stack:
        x, y = stack.pop()
        if not visited[x][y]:
            visited[x][y] = True
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < n and 0 <= ny < m:
                    if cabbage_map[nx][ny] == 1 and not visited[nx][ny]:
                        stack.append((nx, ny))

for i in range(t):
    m, n, k = map(int, input().split())
    cabbage_map = [[0] * m for _ in range(n)] # 가로 m, 세로 n
    visited = [[False] * m for _ in range(n)] 
    # 방문 여부를 체크하기 위한 리스트
    for _ in range(k):
        x, y = map(int, input().split())
        cabbage_map[y][x] = 1 # 해당 위치에는 배추가 존재함, 첫번째 배열 요소에는 y좌표의 값이, 두번째 배열 요소에는 x좌표의 값이 들어간다
    for j in range(n):
        for k in range(m):
            if cabbage_map[j][k] == 1 and not visited[j][k]:
                dfs(j, k, cabbage_map, visited, n, m) # 해당 블록에서 선언된 visited 배열은 함수 작동으로 인해 요소값이 바뀜
                count[i] += 1                          

for i in range(t):
    print(count[i])