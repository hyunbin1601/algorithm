import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)  
# 파이썬의 재귀 호출 한도를 설정하는 함수
# 재귀 한도를 미리 설정해야 런타임 에러를 방지할 수 있음


# https://www.acmicpc.net/problem/24479
# 깊이 우선 탐색 문제

n, m, r = map(int, input().split()) # n, m, r을 입력받음
# n은 정점의 수, m은 간선의 수, r은 시작 정점
graph = [[] for _ in range(n + 1)] # 그래프 생성, n+1만큼의 빈 리스트 생성

for _ in range(m): # m번 반복
        a, b = map(int, input().split()) # a, b를 입력받음  
        graph[a].append(b) # a번째 리스트에 b를 추가
        graph[b].append(a)
        # graph는 인접 리스트 형태로 그래프 표현
        # 무방향 그래프이므로, a와 b를 서로 추가해준다

        
for i in range(n + 1): # n+1만큼 반복
    graph[i].sort() # 리스트를 정렬함 # 리스트를 정렬하는 이유는? -> 작은 숫자부터 방문하기 위해서

    
def dfs(v, visited, order, count): # 깊이 우선 탐색 함수 생성
    visited[v] = True # 방문 여부 확인, v는 현재 방문 중인 정점
    order[v] = count  # order는 출력할 값, 몇번 방문했는지 저장
    count += 1  # 재귀하면서 count를 1씩 증가시킴, 지역함수
    for neighbor in graph[v]:  # graph는 내가 입력한 값들이 정렬되어 저장된 배열
        if not visited[neighbor]:  # visite[neighbor]가 false일 경우, 즉 배열이 비어있을 경우
            count = dfs(neighbor, visited, order, count)
            
    return count
                
    
                

visited = [False] * (n + 1) # 방문한 노드를 False로 초기화
order = [0] * (n + 1)  # 방문한 노드를 0으로 초기화
dfs(r, visited, order, 1) # count는 1부터 시작한다, r은 시작 정점
# 애초에 order 배열에는 i번째의 방문 횟수인 count 값이 저장됨
for i in range(1, n+1):
    print(order[i])




    