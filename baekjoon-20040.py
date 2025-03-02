import sys
input = sys.stdin.readline

# https://www.acmicpc.net/problem/20040
# 유니온 파인드 알고리즘을 사용하여 사이클을 찾는 문제
# 반복문을 사용해서 경로 압축을 하도록 하자


n, m = map(int, input().split())
# n -> 점의 개수 m -> 진행된 차례의 수

# 0부터 n-1까지 고유 번호가 부여됨
# 이 중 어느 세 점도 일직선 위에 놓이지 않음
# 어느 세 점도 일직선 위에 놓이지 않음
# 이어지는 m개의 입력 줄에 각각 i번째 차례에 선택한 두 점의 번호가 주어짐
# 이때 이미 선택된 두 점이 같은 집합에 속해 있을 경우에는 사이클이 발생함

# 입력으로 주어진 케이스에 대해, m번째 차례까지 게임을 진행한 상황에서 이미 게임이 종료되었을 경우
# 사이클이 처음으로 만들어진 차례의 번호를 양수로 출력
# m번의 차례를 모두 처리한 이후에도 종료되지 않았다면 0 출력

parent = [i for i in range(n)] # 0 ~ n-1
cnt = 0

def find(x):
    while x != parent[x]:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x


def union(x, y):
    x = find(x)
    y = find(y)
    if x != y:
        parent[y] = x
        return False
    return True

for i in range(m):
    a, b = map(int, input().split())
    if union(a, b):
        cnt = i + 1
        break
    
print(cnt)