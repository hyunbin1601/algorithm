import sys
import heapq

input = sys.stdin.readline

# 다익스트라 알고리즘
# 최단경로

INF = sys.maxsize

v, e = map(int, input().split())
k = int(input()) # k는 시작점

dp = [INF] * (v + 1)
heap =[]
graph = [[] for _ in range(v+1)]

def Dijkstra(start):
    dp[start] = 0 # 시작 정점에 해당하는 가중치는 0으로 초기화
    heapq.heappush(heap, (0, start))
    
    while heap:
        weight, node = heapq.heappop(heap)
        
        if dp[node] < weight:
            continue # 현재 테이블과 비교하였을 때, 가중치가 더 크면 반복 건너뜀
        
        for next_weight, next_node in graph[node]:
            next_node_weight = weight + next_weight
            if next_node_weight < dp[next_node]:
                dp[next_node] = next_node_weight
                heapq.heappush(heap, (next_node_weight, next_node))
                
for _ in range(e):
    u, v, w = map(int, input().split())
    graph[u].append((w, v))
    
Dijkstra(k)
for i in range(1, v+1):
    if dp[i] == INF:
        print("INF")
    else:
        print(dp[i])
            
