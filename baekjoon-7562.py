import sys
from collections import deque
input = sys.stdin.readline

# 나이트의 이동 문제
# 나이트가 원하는 칸으로 이동하기 위해 몇번 움직여야 하는지 구하는 문제

# 나이트가 이동할 수 있는 경우의 수는 8가지

n = int(input()) # 테스트 케이스 개수

dx = [-2, -1, 1, 2, 2, 1, -1, -2] # 나이트가 이동할 수 있는 x좌표
dy = [1, 2, 2, 1, -1, -2, -2, -1] # 나이트가 이동할 수 있는 y좌표
# x와 y는 조합이 잘 맞게 리스트를 구성해야함

# 너비 우선 탐색 알고리즘
# 최단 경로를 찾고자 할 때 이용
# 튜플을 이용하는 이유 -> 리스트보다 속도가 빠르고, 좌표는 (x, y)로 표현되는, 불변성을 가지는 값이기 때문에 튜플로 하는 편이 속도가 더 빠르다.



def bfs(n, start, end, graph):
    queue = deque()
    queue.append(start)
    
    while queue: # 큐가 빌때까지 반복
        x, y = queue.popleft()
        if x == end[0] and y == end[1]:
            return graph[x][y]
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue # 반복을 건너뜀
            else:
                if graph[nx][ny] == 0:
                    graph[nx][ny] = graph[x][y] + 1
                    queue.append((nx, ny))
    return graph[end[0]][end[1]]

for _ in range(n):
    length = int(input())
    start = tuple(map(int, input().split()))
    end = tuple(map(int, input().split()))
    
    graph = [[0] * length for _ in range(length)]
    
    print(bfs(length, start, end, graph))
    


