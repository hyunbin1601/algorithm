import sys
from collections import deque

input = sys.stdin.readline

# 토마토 농장 3차원 버전 문제
# m, n, h(가로, 세로, 높이) 주어짐

m, n, h = map(int, input().split())
graph = []
# graph를 3차원 배열로 만들어야함
for _ in range(h):
    layer = []
    for _ in range(n): # n은 상자의 세로 칸 수이므로로
        layer.append(list(map(int, input().split())))
    graph.append(layer)

dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]


def bfs(graph):
    queue = deque()
    for z in range(h):
        for y in range(n):
            for x in range(m):
                if graph[z][y][x] == 1:
                    queue.append((z, y, x))
                
                
    while queue:
        z, y, x = queue.popleft()
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
            if 0 <= nx < m and 0 <= ny < n and 0 <= nz < h:
                if graph[nz][ny][nx] == 0:
                    graph[nz][ny][nx] = graph[z][y][x] + 1
                    queue.append((nz, ny, nx))
    result = 0
    for layer in graph:
        for row in layer:
            for value in row:
                if value == 0: # 토마토가 익지 않은 게 있다면
                    return -1
                
                result = max(result, value) # 가장 큰 값을 찾기
    return result - 1


print(bfs(graph))
        
            
            