import sys
from collections import deque

input = sys.stdin.readline

n, m, v = map(int, input().split())
# n은 정점의 개수, m은 간선의 개수, v는 탐색을 시작할 정점의 번호
# 출력하고자 하는 값
# 첫째 줄에 DFS를 수행한 결과를, 그 다음 줄에는 BFS를 수행한 결과를 출력한다. 
# v부터 방문된 점을 순서대로 출력하면 된다.

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)  # 무방향 그래프
 
for i in range(n + 1):
    graph[i].sort() 

def dfs(v, visited):
    visited[v] = True
    print(v, end=' ')

    
    for neighbor in graph[v]:
        if not visited[neighbor]:
            dfs(neighbor, visited)
            

    
def bfs(v, visited): # 출력하고자 하는 것은 방문한 정점의 번호이므로
    queue = deque([v])
    visited[v] = True
    print(v, end=' ')
    
    while queue:
        v = queue.popleft()
        for neighbor in graph[v]:
            if not visited[neighbor]:
                visited[neighbor] = True
                print(neighbor, end=' ')
                queue.append(neighbor)
                
visited_dfs = [False] * (n + 1)
dfs(v, visited_dfs)
print()

visited_bfs = [False] * (n + 1)
bfs(v, visited_bfs)
print()    
    
    
