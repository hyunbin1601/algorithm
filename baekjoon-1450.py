import sys, bisect
input = sys.stdin.readline
# bisect 모듈은 정렬된 리스트에 대해 이진 검색(바이너리 서치) 기능을 제공하는 파이썬 모듈

# https://www.acmicpc.net/problem/1450

# 냅색 문제
# meet in the middle 알고리즘?
# 투 포인터를 이용한 문제
# 물건을 반으로 나눠서 각각의 경우의 수를 구하고 합침

# n개의 물건과 최대 c만큼의 무게를 넣을 수 있는 가방이 있을 때
# n개의 물건을 가방에 넣는 방법의 수

n, c = map(int, input().split())

weights = list(map(int, input().split())) # 물건의 무게

# 출력하고자 하는 값은 가방에 넣는 방법의 수

half = n // 2 # 왜 물건을 반으로 나눠? -> 물건을 반으로 나눠서 각각의 경우의 수를 구하고 합침
left = weights[:half] # half 이전까지지 
right = weights[half:] # half 이후부터
# [:half]는 0부터 half-1까지
left_sum = []
right_sum = []



def two_pointer(arr, idx, current_sum, result):
    if current_sum > c:
        return  # 현재 무게가 c를 넘어가면 재귀 종료
    if idx == len(arr): # 모든 물건을 확인했을 때
        result.append(current_sum) # 현재 무게를 결과에 추가
        return 
    # 물건을 선택하지 않는 경우
    two_pointer(arr, idx+1, current_sum, result)
    # 물건을 선택하는 경우
    return two_pointer(arr, idx+1, current_sum+arr[idx], result) # 현재 무게에 idx번의 물건의 무게를 더함(재귀)

two_pointer(left, 0, 0, left_sum) # 각 그룹에 대한 모든 가능한 부분집합의 무게합
two_pointer(right, 0, 0, right_sum) 

right_sum.sort() # 이진 탐색을 위해 정렬

count = 0
for ls in left_sum:
    remain = c - ls
    count += bisect.bisect_right(right_sum, remain)
    

print(count)
