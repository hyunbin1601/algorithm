import sys
input = sys.stdin.readline

# https://www.acmicpc.net/problem/1717

# n+1개의 집합
# m은 입력으로 주어지는 연산의 개수
# 유니온 파인드 알고리즘 사용

# union find 알고리즘
# find : 주어진 원소가 속한 집합의 루트 원소 찾기
# union : 두 집합을 하나의 집합으로 합침
# 트리 구조를 사용해 집합 표현

n, m = map(int, input().split())

# 합집합 -> 0 a b // a가 포함된 집합과 b가 포함된 집합을 합치겠다
# 같은 집합에 포함되어 있는가? -> 1 a b

# 출력은 1로 시작하는 입력에 대해, a와 b가 같은 집합에 포함되어 있을 경우 -> yes
# 아니면 no
parent = [i for i in range(n+1)]  # 0 ~ n

def find(x):  # x의 부모 찾는 함수
    if parent[x] == x:
        return x  # 자기 자신이 부모인 경우 -> 자기 자신 반환
    parent[x] = find(parent[x]) # 부모를 찾아서 저장 -> 재귀함수에 의해 최종적으로 부모가 리턴됨
    return parent[x]   # 결국 부모를 리턴함

def union(x, y):
    x = find(x) # x의 부모 찾기
    y = find(y) # y의 부모 찾기
    if x != y:
        parent[y] = x
        
for _ in range(m):
    c, a, b = map(int, input().split())
    if c == 0:
        union(a, b)
    else:
        if find(a) == find(b):
            print("YES")
        else:
            print("NO")
    



