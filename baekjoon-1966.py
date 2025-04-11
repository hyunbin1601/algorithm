from collections import deque
import sys
# https://www.acmicpc.net/problem/1966
# fifo -> 큐 자료구조에 따라 먼저 들어온 데이터가 먼저 나감
input = sys.stdin.readline
test = int(input()) # 테스트 케이스의 개수

# 현재 queue의 가장 앞에있는 문서의 중요도 확인
# 나머지 문서들 중 현재 문서보다 중요도가 높은 문서가 하나라도 있다 
# -> 이 문서를 인쇄하지 않고 queue의 가장 뒤에 재배치
# 그렇지 않을 경우 바로 인쇄

for _ in range(test):
    n, m = map(int, input().split())
    # n은 문서의 개수, m은 몇번째로 인쇄되는지 알고싶은 문서의 큐에서의 위치
    queue = deque() # 큐 자료구조를 사용하기 위한 deque 선언
    queue = deque((priority, idx) for idx, priority in enumerate(map(int, input().split())))
        # enumerate는 파이썬 빌트인 함수로, 값을 입력받고 리스트에 저장 후, 해당 리스트에서 인덱스와 값을 함께 가져와 idx, priority에 부여함
    count = 0 # 우리가 알고자 하는 문서의 인쇄 횟수를 나타내는 변수
    
    while queue: # 큐가 비어있지 않을 때까지\
        current = queue.popleft() # 현재 요소값을 꺼내옴
        if any(current[0] < x[0] for x in queue):
            # any는 iterable한 객체를 인자로 받아 True/False를 반환하는 함수
            # 참고로 iterable함이라는 것은 반복 가능한 개체를 의미함
            queue.append(current) # queue에 있는 모든 요소의 priority를 확인해서 현재 값보다 더 큰 값이 있을경우
        else:
            count += 1 # count 변수가 0부터 시작하기 때문에 먼저 1 증가시키고 if문 비교
            if current[1] == m:
                print(count)
                break
            
        
        
        