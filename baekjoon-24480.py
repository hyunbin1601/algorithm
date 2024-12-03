import sys
sys.setrecursionlimit(10**6)  # 재귀 호출의 깊이 설정
input = sys.stdin.readline
# 정점을 내림차순으로 방문하는 dfs 문제

n, m, r = map(int, input().split())

graph = [[] for _ in range(n + 1)] # n+1만큼의 그래프 생성

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a) # 무방향 그래프이므로
    # graph[1] = 4로 이어지고 graph[4] = 1로 이어지는데, 이차원 배열이기 때문에 graph[1]에 여러가지 원소가 배정됨
    # 하나의 정점에 여러개의 정점이 연결되었음을 인접 리스트로 표현한 것, 무방향 그래프이므로 양쪽 다 append
    
    
for i in range(n + 1):
    # 정점 번호를 내림차순으로 방문한다.
    graph[i].sort(reverse=True) # 내림차순 정렬
    
print(graph)

def dfs(v, visited, order, count):
    visited[v] = True  # 방문했으므로 true로 변경
    order[v] = count  # 각 정점이 몇번째에 방문되었는지 저장됨
    count += 1
    for neighbor in graph[v]:  # graph 배열은 이차배열, 방문 안한 정점 탐색
        if not visited[neighbor]: # visited[neighbor] = false인경우, 즉 방문을 안한경우
            count = dfs(neighbor, visited, order, count) # 재귀호출
            # 왜 not으로 표현? -> 굳이 if ~ elif로 이어가고 싶지 않아서
            
    return count

visited = [False] * (n + 1)
order = [0] * (n + 1)
dfs(r, visited, order, 1)

for i in range(1, n+1):
    print(order[i])