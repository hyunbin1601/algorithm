import sys
input = sys.stdin.readline

# https://www.acmicpc.net/problem/15686

# 0은 빈칸, 1은 집, 2는 치킨집
# 치킨 거리: 집과 가장 가까운 치킨집 사이의 거리
# m -> 도시에서 가장 수익을 낼 수 있는 치킨집의 개수
# 도시의 치킨 거리가 가장 작게 될 수 있도록 m개의 치킨집을 고름
n, m = map(int, input().split())
array = [] # 도시 정보를 저장할 리스트

for _ in range(n):
    array.append(list(map(int, input().split())))
    
# 치킨집과 집의 좌표를 저장할 리스트
chicken = []
home = []

for i in range(n):
    for j in range(n):
        if array[i][j] == 1:  # array는 이중 리스트
            home.append((i, j))
        elif array[i][j] == 2:  # 각각의 정보를 저장한다
            chicken.append((i, j))
            
            
from itertools import combinations
# 치킨집 중에서 m개를 뽑는 조합 (nCr)

result = int(1e9) # 최소값을 저장할 변수, 1e9는 10^9로 아주 큰 수를 의미함

for chicken_comb in combinations(chicken, m): # 폐업시키지 않을 치킨집을 최대 m개 골랐을 때
    # 도시의 치킨 거리의 최솟값 구하기
    sum = 0 # sum과 result를 비교해서 좀 더 작은 값을 result로 갱신하기
    for home_x, home_y in home:
        min_distance = int(1e9)
        for chicken_x, chicken_y in chicken_comb:
            min_distance = min(min_distance, abs(home_x - chicken_x) + abs(home_y - chicken_y))
        sum += min_distance
    result = min(result, sum)
    
print(result)

            
            

    