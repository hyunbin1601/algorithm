import sys
from collections import deque

input = sys.stdin.readline

# 위치가 X일 때 걷는다면 1초 후에 X-1 또는 X+1로 이동하게 된다. 
# 순간이동을 하는 경우에는 0초 후에 2*X의 위치로 이동하게 된다.
# 수빈이와 동생의 위치가 주어졌을 때, 수빈이가 동생을 찾을 수 있는 가장 빠른 시간이 몇 초 후?

n, k = map(int, input().split())
# 수빈, 동생 위치
# bfs 이용해보기

time = [0] * 100001  # graph는 인덱스 1부터 시작하므로, 100001까지 일단 생성
visited = [False] * 100001 # 방문 여부 확인
dx = [-1, 1, 2] # 걷거나 순간이동

def bfs():
    queue = deque()
    queue.append(n) # 수빈 위치
    visited[n] = True
    
    while queue:
        x = queue.popleft()
        if x == k:
            return time[x]
        if x * 2 <= 100000 and not visited[x * 2]: # 아직 방문하지 않은 곳으로 순간이동한 경우
            time[x * 2] = time[x]
            visited[x * 2] = True
            queue.append(x * 2)
            
        for i in range(2):
            nx = x + dx[i]
            if 0 <= nx <= 100000 and not visited[nx]: # 아직 방문하지 않고, 범위를 벗어나지 않았을 경우
                time[nx] = time[x] + 1
                visited[nx] = True
                queue.append(nx)
                
    return time[k]


print(bfs())