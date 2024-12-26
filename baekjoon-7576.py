import sys
from collections import deque

input = sys.stdin.readline

# 인접한 곳은 왼쪽, 오른쪽, 앞, 뒤 네 방향
# 대각선은 안됨
# 너비 우선 탐색(bfs) 문제
# 너비 우선 탐색 문제의 경우 최단 경로를 구할 때 유용함
m, n = map(int, input().split())
# m은 가로칸 수, n은 세로칸 수

# 상자에 저장된 토마토의 정보
# 1은 익은 토마토 0은 안익은 토마토 -1은 토마토가 없음음
graph = [list(map(int, input().split())) for _ in range(n)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(graph):
    queue = deque()
    
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                queue.append((i, j)) # 튜플 형식으로 위치 저장
                
    while queue:
        x, y = queue.popleft()
        if graph[x][y] == -1:
            continue  # 토마토가 아예 존재하지 않으므로
        
        else:
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                
                if nx < 0 or nx >= n or ny < 0 or ny >= m:
                    continue
                else:
                    if graph[nx][ny] == 0:
                        graph[nx][ny] = graph[x][y] + 1
                        queue.append((nx, ny))
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                return -1 # 토마토가 모두 익지 못한 상황
    return graph[x][y] - 1  # 날짜를 출력해야 하므로, 
# 그리고 토마토가 모두 익어있는 상황이면 0을 출력하게 됨

print(bfs(graph))


                    


