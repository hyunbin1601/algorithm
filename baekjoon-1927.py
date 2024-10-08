import sys
input = sys.stdin.readline # sys.stdin.readline() is faster than input()
import heapq # python의 heapq module 불러옴
# 만약 큐가 비어있는데 가장 작은값을 출력하라고 하는 경우? -> 0을 출력하면 된다
# python의 heapq는 최소힙 모듈

n = int(input())
hq = []

for i in range(n):
    num = int(input())
    #hq라는 리스트에 최소힙이진트리 형식으로 num을 추가한다
    if num > 0:
        heapq.heappush(hq, num)   # heapq.heappush를 통해 최소힙에 원소 추가 -> 자동으로 최소힙으로 이진트리 식으로 추가된다
    elif num == 0:
        if len(hq) == 0:
            print(0)
        else:
            print(heapq.heappop(hq))




