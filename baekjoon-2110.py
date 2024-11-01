# baekjoon 2110
# https://www.acmicpc.net/problem/2110

import sys
input = sys.stdin.readline

n, c = map(int, input().split())

house_distance = []

for _ in range(n):
    house_distance.append(int(input()))
    
house_distance.sort()

start = 1
end = house_distance[-1] - house_distance[0]  # 이진탐색 시작점과 끝점 설정

# 알맞은 result 값을 구하는게 목표
# 이진탐색을 이용하여 공유기 사이의 최대 거리를 구함

def binary_search(house_distance, n, c, start, end):
    result = 0 # 전역변수 result를 사용하기 위해 global 선언, 이제부터 해당 함수 안에서 result 변수에 대한 접근 가능
    while start <= end:
        mid = (start + end) // 2
        value = house_distance[0] # 시작점의 값을 value에 저장
        count = 1 # 공유기 개수 초기화
        for i in range(1, n):
            if house_distance[i] >= value + mid:  # 왜 value + mid의 값과 비교하는거야? 이해가 안됨 -> value + mid는 공유기 사이의 거리를 의미함
                value = house_distance[i]
                count += 1
        if count >= c:
            start = mid + 1
            result = mid
        else:
            end = mid - 1
    return result
            
print(binary_search(house_distance, n, c, start, end))     