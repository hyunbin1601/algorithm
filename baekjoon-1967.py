import sys

input = sys.stdin.readline

# 트리의 지름 출력
# 트리에 존재하는 모든 경로들 중 가장 긴 것 찾기

n = int(input()) # 노드의 개수
# 첫 번째 정수는 간선이 연결하는 두 노드 중 부모 노드의 번호를 나타내고, 두 번째 정수는 자식 노드를, 세 번째 정수는 간선의 가중치
# 부모 노드의 번호가 작은 것이 먼저 입력되고, 부모 노드의 번호가 같으면 자식 노드의 번호가 작은 것이 먼저 입력

graph = [[] for _ in range(n + 1)] # 노드의 개수만큼 빈 리스트 생성
# 루트 노드는 항상 1

for _ in range(n - 1):
    parent, child, weight = map(int, input().split())
    graph[parent].append((child, weight))
    graph[child].append((parent, weight))
    
def dfs(start):
    visited = [-1] * (n + 1)
    stack = [(start, 0)]
    visited[start] = 0
    
    max_node = [0, 0]
    
    while stack:
        node, cost = stack.pop()
        
        for next_node, next_cost in graph[node]:
            if visited[next_node] == -1:
                visited[next_node] = cost + next_cost
                stack.append((next_node, cost + next_cost))
                
                if max_node[1] < visited[next_node]:
                    max_node = next_node, visited[next_node]
                    
    return max_node

node, _ = dfs(1)  # node가 반환되는데, 노드 번호와 가중치가 반환되므로 -> node는 가장 먼 노드의 번호
_, result = dfs(node) # node를 기준으로 가장 먼 노드의 가중치 값 출력

print(result)
