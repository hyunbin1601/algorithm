import sys
sys.setrecursionlimit(10**6)  # recursion error 방지
input = sys.stdin.readline

n, r, q = map(int, input().split())
# n은 트리의 정점의 수
# r은 루트의 번호
# q는 쿼리의 수
# 트리는 사이클이 없는 그래프
# 특정한 i번째 노드를 루트로 하는 서브 트리에 대해 i번째 루트 노드를 포함했을때와 포함하지 않았을 때 중 조건에 맞는 답 정의
# 루트는 r, 정점 u를 루트로 하는 서브트리에 속한 정점의 개수 출력

# dfs + dp 형식으로 푸는 문제
# 한번 방문한 곳은 visit 복구 x -> 다시는 가지 못하게 한다면 트리를 탐색하는 것과 같은 효과임

# u, v 형태로 트리에 속한 간선의 정보가 주어짐

# 이전에 한번이라도 방문된 노드를 다시 가지 않도록 하면 -> 트리를 탐색하는 것과 마찬가지!
# 구현 로직 : 각 노드들을 출발점으로 하여 연결된 곳들을 탐색하고, 구한 값을 차례대로 누적하여 dp 테이블에 저장

# 트리의 간선 정보를 저장할 리스트
tree = [[] for _ in range(n+1)]

# 트리 생성
for _ in range(n-1):
    u, v = map(int, input().split())
    tree[u].append(v)
    tree[v].append(u)

# dp 테이블 생성
subtree_size = [0] * (n+1)

def dfs(node, parent):
    subtree_size[node] = 1  # 현재 노드 자신 -> 1로 초기화
    for child in tree[node]: # 현재 노드의 자식들 탐색
        if child != parent:   # 부모 노드가 아닌 경우에만 탐색 -> 트리 구조에서 부모 노드로 다시 돌아가는 것을 방지함
            # 자식 노드를 루트로 하는 서브트리의 크기를 구하고 누적
            dfs(child, node) # 재귀를 통해 자식 노드를 루트로 하는 서브트리 구함 -> 현재 노드를 부모 노드로 전달함 -> 해당 노드의 자식들이 탐색됨
            subtree_size[node] += subtree_size[child] # 자식 노드 child를 루트로 하는 서브트리의 크기를 현재 노드의 서브트리 크기에 누적시킴
            

dfs(r, -1)
# 서브트리 루트에 속한 자식의 개수 출력
for _ in range(q):
    u = int(input())
    print(subtree_size[u])
    

