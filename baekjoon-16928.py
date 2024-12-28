import sys
from collections import deque

input = sys.stdin.readline
# 정육면체의 주사위 사용
# 1부터 6까지
# 보드판은 10*10의 총 100개의 칸으로 나누어져 있음
# 주사위 굴린 결과가 100번을 넘으면 이동x
# i번째에서 주사위가 4가 나오면 -> i+4로 이동
# 사다리면 -> 위로 올라감(칸의 번호가 커짐)
# 뱀이면 -> 아래로 내려감(칸의 번호가 작아짐)
# 1번에서 100번으로 도착하기 위한 주사위 횟수 최솟값

n, m = map(int, input().split())
# n -> 사다리 수 m -> 뱀 수
ladder = {}
snake = {}

# 사다리 정보
for _ in range(n):
    x, y = map(int, input().split())
    ladder[x] = y # 딕셔너리 형태로 저장하기 때문에 딕셔너리 배열인 {}로 선언
# 뱀의 정보
for _ in range(m):
    u, v = map(int, input().split())
    snake[u] = v
    
graph = [0] * 101

def bfs(graph):
    queue = deque()
    queue.append(1)    # 1부터 시작하므로, 큐에 1을 넣어줌줌
    
    while queue:
        x = queue.popleft()
        for i in range(1, 7):
            nx = x + i
            if nx > 100:
                continue # 반복을 그대로 넘어감
            # 주사위 굴린 결과가 100이 아니라 100보다 커질 경우 아예 이동 불가능
            
            if nx in ladder:
                nx = ladder[nx]
            elif nx in snake:
                nx = snake[nx]
                
            if graph[nx] == 0:
                graph[nx] = graph[x] + 1
                queue.append(nx)
                
    return graph[100]

print(bfs(graph))
                    
        
    