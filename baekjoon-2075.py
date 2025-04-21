import sys
import heapq # heapq 모듈은 기본적으로 최소 힙을 제공함
input = sys.stdin.readline
# 이 문제도 최대/최소 힙 문제

n = int(input())
# n * n의 표가 주어졌을때, 표에 채워진 수는 자기보다 한칸 위의 수보다 커야 함
# n번째 큰 수 출력
# 표에 있는 수는 모두 서로 다른 수
min_heap = [] # 최소 힙, 파이썬에서는 기본적으로 heapq 모듈을 불러올 때 최소 힙 제공

for _ in range(n):
    row = (list(map(int, input().split())))
    for num in row:
        if len(min_heap) < n:  # 힙의 길이가 n보다 작을 때
            heapq.heappush(min_heap, num) # 힙에 num을 추가함
            
        else: # 힙의 길이가 n보다 크거나 같을경우
            if min_heap[0] < num:  # min_heap에서 가장 작은 요소가 num보다도 작을 경우
                heapq.heappop(min_heap) # 첫번째 요소를 제거함
                heapq.heappush(min_heap, num) # min_heap에 num을 추가함
                
print(min_heap[0])
            


    
