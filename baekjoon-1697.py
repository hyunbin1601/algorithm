import sys
from collections import deque
input = sys.stdin.readline

# bfs 문제
# 점 n, m이 주어지고, 1초후 n-1 또는 n + 1로 이동하거나, 
# 순간이동의 경우 2 * n의 위치로 이동함

# 수빈이와 동생의 위치가 주어졌을때, 동생을 찾을 수 있는 가장 빠른 시간?

n, k = map(int, input().split())
visitied = [False] * 100001 # 0 ~ 100000 총 10만개 존재함
graph = [0] * 100001

dx = [-1, 1, 0] # -1은 n-1, 1은 n+1, 0은 순간이동
dy = [0, 0, 2] # 0은 순간이동, 2는 2 * n  
# dx는 양옆이동, dy는 순간이동

def bfs(n, k, visited, graph):
    queue = deque() # 방문한 노드를 저장하는 큐
    queue.append(n) # 수빈이의 초기 위치를 큐에 넣음
    visited[n] = True # 수빈이의 초기 위치를 방문했으므로 True로 변경
    graph[n] = 0 # 수빈이의 초기 위치는 0
    
    while queue:
        x = queue.popleft()
        if x == k:
            return graph[x]
        else:
            for i in range(3):
                if i == 2:
                    nx = x * dy[i]
                else:
                    nx = x + dx[i]
                if nx < 0 or nx >= 100001:
                    continue
                if not visited[nx]:
                    visited[nx] = True
                    graph[nx] = graph[x] + 1
                    queue.append(nx)
    return graph[k]

print(bfs(n, k, visitied, graph))
            
    
