# 입력값을 받고 -> 최소힙을 이용하여 이진트리로 배열
# 이진트리로 배열 시 -> O(log2n)의 시간복잡도를 가지게 됨
# 최소힙을 이용하여 절댓값이 가장 작은 수부터 출력

import heapq
import sys
#abs는 파이썬의 내장함수(빌트인 함수)로 절댓값 반환함

input = sys.stdin.readline

n = int(input())
hq = [] # 최소힙을 이용하여 이진트리로 저장할 배열

for i in range(n):
    num = int(input())
    if abs(num) > 0:
        heapq.heappush(hq, (abs(num), num))  # 우선순위가 같을 때에는...? -> 절댓값이 같을 때에는 원래 수(두번째 요소인 num 기준)를 기준으로 정렬
    elif abs(num) == 0:
        if len(hq) == 0:
            print(0)
        else:
            print(heapq.heappop(hq)[1])  # 튜플에서 두번째 요소를 꺼내면 된다 -> 두번째 요소란 원래수인데, 위에서처럼 저장할 경우 pop을 할 때 우선순위가 같은 값이 존재하면 (절댓값, 원래수) 형태로 튜플을 반환하는데, 이 튜플에서 두번째 요소인 num을 얻기 위해 [1]을 사용하여 추출한다
    
    

