import sys
input = sys.stdin.readline

# 1은 집이 있는 곳을, 0은 집이 없는 곳을 나타낸다.
# 연결되었다는 것은 어떤 집이 좌우, 혹은 아래위로 다른 집이 있는 경우를 말한다. 
# 대각선상에 집이 있는 경우는 연결된 것이 아니다. 
# 지도를 입력하여 첫번째 줄에는 단지수를 출력해라
# 두번째 줄에는 각 단지에 속하는 집의 수를 오름차순으로 정렬하여 출력하기
# 그래프와 순회 문제

n = int(input())
# 지도의 크기 n*n

# apartment_map = [list(map(int, input().strip())) for _ in range(n)]
# 지도 정보 입력
apartment_map = []
for _ in range(n):
    line = input().strip()
    sub_map = []
    for i in line:
        sub_map.append(int(i))
    apartment_map.append(sub_map)


visited = [[False] * n for _ in range(n)]
# 각 위치의 방문 여부를 체크하기 위한 리스트

order = []

dx = [-1, 1, 0, 0]  # 상하좌우 방향(x축)
dy = [0, 0, -1, 1] # 상하좌우 방향(y축)

def dfs(x, y):
    stack = [(x, y)] # 튜플로 좌표표현
    count = 0
    
    while stack: # stack이 0이 되기 전까지 계속 반복함
        
        x, y = stack.pop() # 리스트에서 pop함
        if not visited[x][y]: # 방문하지 않은 경우
            visited[x][y] = True # 방문함
            count += 1 # 방문한 집의 수를 1 증가시킴
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx >=0 and nx < n and ny >= 0 and ny < n:
                    if apartment_map[nx][ny] == 1 and not visited[nx][ny]:
                        stack.append((nx, ny))
                        
    return count
    
            
for i in range(n):
    for j in range(n):
        if apartment_map[i][j] == 1 and not visited[i][j]: # 해당 위치에 집이 있고, 방문하지 않은 경우
            order.append(dfs(i, j)) # return 값으로 count를 주므로           

order.sort()
print(len(order))

for i in order:
    print(i)
    
            
        




