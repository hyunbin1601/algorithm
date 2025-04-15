# https://www.acmicpc.net/problem/14725

import sys
input = sys.stdin.readline

n = int(input()) # 먹이의 정보 개수
food = dict() # 딕셔너리 형태로 전체 먹이 정보 저장
# 딕셔너리 -> var = {key: value} 이런 식으로
# 딕셔너리에서 정보를 불러올 땐? -> var[key] 이런식으로!

for _ in range(n): # n번 반복, 각 먹이 정보 처리
    food_info = list(input().rstrip().split()) # 먹이 개수, 먹이 이름(왼쪽부터 순서대로 각 층마다 지나온 방에 있는 먹이 정보, 먹이 이름)
    food_info.pop(0) # 첫 번째 -> 먹이의 개수, 그러므로 제거거
    temp = food # 먹이 정보 포인터, 딕셔너리를 가리킨다
    for i in food_info: # food_info를 하나씩 가리킴
        if i not in temp: # 만약 food_info[i]가 temp에 없다면
            temp[i] = dict() # 새로운 먹이 정보 추가
        temp = temp[i] # 다음 먹이 정보로 이동
        
# 먹이 정보 출력
def dfs(food, depth):
    for i in sorted(food.keys()): # food의 키를 정렬함
        print("--" * depth + i) # 현재 먹이 정보 출력
        # --를 depth만큼 반복한 후, 그 뒤에 i에 저장된 문자열을 이어붙여 출력함
        dfs(food[i], depth + 1) # 다음 먹이 정보로 이동
        
dfs(food, 0) # 깊이 우선 탐색 시작 
