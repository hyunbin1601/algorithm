import sys
input = sys.stdin.readline

# https://www.acmicpc.net/problem/11725
# 트리의 부모 찾기 문제, DFS 사용
# 출력해야 하는 값 : 
# 첫째 줄부터 N-1개의 줄에 각 노드의 부모 노드 번호를 2번 노드부터 순서대로 출력
# 트리의 루트는 항상 1

n = int(input()) # 트리 노드의 개수
# 트리 알고리즘 -> dfs 이용해서 구현

tree = [[] for _ in range(n+1)] # 트리 생성, 각 노드에 연결된 자식 노드를 저장하는 리스트
parent = [0 for _ in range(n+1)] # 각 노드의 부모 노드 저장, 출력할 값

for _ in range(n-1): # 트리의 간선의 개수는 n-1개(노드의 개수: n개)
    a, b = map(int, input().split())
    tree[a].append(b) # 양방향 간선 -> 입력받아 저장
    tree[b].append(a)
    
def dfs(start, tree, parent): # start는 탐색을 시작할 노드
    stack = [start] # 탐색할 노드 저장, 부모 노드 start부터 시작해서 찾아가기
    while stack:
        node = stack.pop() # 현재 노드를 꺼낸 후
        for i in tree[node]: # 해당 노드에 연결된 자식 노드 탐색
            if parent[i] == 0: # 현재 노드가 아직 방문되지않은 경우? -> 해당 노드를 부모 노드로 설정하기
                parent[i] = node # 현재 노드를 부모 노드로 설정
                stack.append(i) # 해당 노드의 자식 노드를 탐색하기 위해 스택에 저장
                
dfs(1, tree, parent)

for i in range(2, n+1):
    print(parent[i])