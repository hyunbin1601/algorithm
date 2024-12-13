from collections import deque
import sys

input = sys.stdin.readline

computer = int(input())
network = int(input()) # 네트워크 상에서 직접 연결되어 있는 컴퓨터 쌍의 개수

graph = [[] for _ in range(computer+1)] # n+1개의 빈 리스트 생성

for _ in range(network):
    a, b = map(int, input().split())
    
    graph[a].append(b)
    graph[b].append(a)
    # a와 b를 연결해줌, 무방향 그래프이므로 두번
    
for i in range(computer+1):
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
                
                
visited = [False] * (computer + 1)
order = [0] * (computer + 1)
bfs(1, visited, order)

print(computer - order.count(0)) # 1번 컴퓨터를 제외한 감염된 컴퓨터 수 출력
    
 