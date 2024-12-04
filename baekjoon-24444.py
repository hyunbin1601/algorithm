import sys
from collections import deque

input = sys.stdin.readline

# https://www.acmicpc.net/problem/24444
# bfs 문제, 너비 우선 탐색

n, m, r = map(int, input().split())

graph = [[] for _ in range(n + 1)] # n+1만큼의 그래프 생성

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
for i in range(n + 1):
    graph[i].sort()
    
def bfs(v, visited, order):
    queue = deque([v])
    visited[v] = True
    count = 1
    order[v] = count
    
    while queue:
        v = queue.popleft()
        for neighbor in graph[v]:
            if not visited[neighbor]:
                visited[neighbor] = True
                count += 1
                order[neighbor] = count
                queue.append(neighbor)
                
                
visited = [False] * (n + 1)
order = [0] * (n + 1)
bfs(r, visited, order)

for i in range(1, n+1):
    print(order[i])