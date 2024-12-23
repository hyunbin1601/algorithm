import sys
from collections import deque
input = sys.stdin.readline

# n * m 크기의 미로
# 미로에서 1은 이동가능, 0은 이동불가능
# (1, 1)에서 출발해서 (n, m)으로 이동하는 최소 칸수
# bfs 문제

n, m = map(int, input().split())
# n개의 줄에 m개의 정수로 미로가 주어짐
maze_map = []
for _ in range(n):
    maze = input().strip()
    maze_map.append(list(map(int, maze))) 
    # maze를 처음 입력받을 때 문자열로 받고, map을 이용해서 문자 하나씩 int로 형변환해서 maze_map에 저장
    
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1] # 상하좌우 이동


def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or nx >= n or ny < 0 or ny >= m: # [nx][ny]로 들어오므로, ny는 x축, nx는 y축(반대로 생각하면 편함함)
                continue # 반복을 건너뜀
            
            if maze_map[nx][ny] == 0:
                continue # 이동 불가능한 칸
            else:
                if maze_map[nx][ny] == 1:
                    maze_map[nx][ny] = maze_map[x][y] + 1
                    queue.append((nx, ny))
    return maze_map[n-1][m-1] # (n, m)까지의 최소 칸수
                
print(bfs(0, 0)) # (1, 1)에서 출발
