import sys

# https://www.acmicpc.net/problem/3584
# 가장 가까운 조상 찾기

t = int(input())

for _ in range(t):
    n = int(input())
    parent = [0] * n
    
    for _ in range(n-1):
        a, b = map(int, input().split())
        parent[b-1] = a
    
    a, b = map(int, input().split())
    
    a_parent = [a]
    b_parent = [b]
    
    while parent[a-1] != 0:
        a = parent[a-1]
        a_parent.append(a)
        
    while parent[b-1] != 0:
        b = parent[b-1]
        b_parent.append(b)
        
    a_parent.reverse() # 조상 리스트 뒤집기 -> root에서 시작하도록 만들기
    b_parent.reverse()
    
    common = 0
    for x, y in zip(a_parent, b_parent):
        if x == y:  # zip 함수 -> 파이썬의 내장 함수중 하나, 여러개의 iterable을 인자로 받아 각 iterable의 같은 인덱스에 위치한 요소들을 하나의 튜플로 묶어줌
            common = x
        else:
            break
    print(common)
            
            
        
    