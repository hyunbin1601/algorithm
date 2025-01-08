import sys
from collections import deque

input = sys.stdin.readline

# 테스트 케이스 개수
k = int(input())

def bfs(start, graph, colors): # bfs 알고리즘을 사용해서 그래프 탐색
    queue = deque([start])
    colors[start] = 1
    
    while queue:
        v = queue.popleft() # 큐에서 하나씩 꺼냄
        for neighbor in graph[v]: 
            if colors[neighbor] == 0: # 아직 색칠되지 않은경우
                colors[neighbor] = -colors[v] # 반대 색깔로 색칠
                queue.append(neighbor)
            elif colors[neighbor] == colors[v]: # 만약 같은 색깔로 색칠되어 있는 경우우
                return False  # 이분 그래프가 아님ㅠ
            
    return True

for _ in range(k):
    v, e = map(int, input().split())
    graph = [[] for _ in range(v+1)]
    
    for _ in range(e):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
        
    colors = [0] * (v + 1) # 0: 방문하지 않음, 1: 색칠한 것, -1: 색칠하지 않은 것
    is_bipartite = True
    
    for i in range(1, v+1):
        if colors[i] == 0:
            if not bfs(i, graph, colors): # bfs의 결과값이 False
                is_bipartite = False
                break # 반복 탈출
            
    if is_bipartite:
        print("YES")
    else:
        print("NO")
               

