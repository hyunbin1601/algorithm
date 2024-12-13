import sys
input = sys.stdin.readline

# 백 트래킹 문제
# 자연수 n, m이 주어졌을때, 1부터 n까지 자연수 중 중복없이 m개를 고를 수열을 모두 구하기

n, m = map(int, input().split())

visited = [False] * n
out = []  # 출력할 중복없이 m개가 골라진 수열

def back_tracking(depth, idx, n, m):
    if depth == m:  # depth는 탐색 깊이, m은 목표 깊이
        print(' '.join(map(str, out)))
        return
    
    for i in range(idx, n):
        if not visited[i]: # visited의 값이 false인 경우
            visited[i] = True # true로 설정
            out.append(i+1) # out에 i+1 추가, 0부터 시작하는 인덱스
            back_tracking(depth+1, i+1, n, m)
            visited[i] = False  
            out.pop()
            
back_tracking(0, 0, n, m) # depth, idx, n, m
