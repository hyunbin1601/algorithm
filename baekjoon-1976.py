import sys
input = sys.stdin.readline

# https://www.acmicpc.net/problem/1976
# https://chiefcoder.tistory.com/55




n = int(input())
m = int(input())


parent = [i for i in range(n+1)]  # 0 ~ n


def find(x):
    if parent[x] == x:  # 부모가 자기 자신인 경우
        return x   # 해당 부모 노드를 리턴, 함수 종료
    parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    x = find(x)  # x의 부모를 찾기위한 과정
    y = find(y)
    if x != y:
        parent[y] = x
        
for i in range(1, n+1):
    temp = list(map(int, input().split())) 
    for j in range(1, len(temp)+1):
        if temp[j-1] == 1:
            union(i, j)
            
plan = list(map(int, input().split()))
flag = True
for i in range(1, len(plan)):
    if find(plan[i]) != find(plan[i-1]):   # 연결되어 있지 않음
        flag = False
        break
if flag:
    print("YES")
else:
    print("NO")

