import sys
from collections import deque

input = sys.stdin.readline

# bfs 문제

n, m, r = map(int, input().split())
# n은 정점의 수, m은 간선의 수, r은 시작 정점

graph = [[] for _ in range(n+1)]
# n+1개의 빈 리스트 생성

for _ in range(m):
    a, b = map(int, input().split())
    
    graph[a].append(b)
    graph[b].append(a)
    # a와 b를 연결해줌, 무방향 그래프이므로 두번
 
for i in range(n+1):
    graph[i].sort(reverse=True) # 내림차순으로 정렬
    
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
        

