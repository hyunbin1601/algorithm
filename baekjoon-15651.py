import sys
input = sys.stdin.readline

n, m = map(int, input().split())

# 1부터 n까지 자연수 중 m개를 고른 수열
# 같은 수 여러번 고를 수 있음, 중복 가능

out = []
# 같은 수가 여러번 나올 수 있으므로 visited 배열이 필요없음

def back_tracking(depth, n, m):
    if depth == m:
        print(' '.join(map(str, out)))
        return
    
    for i in range(n):
        out.append(i+1)
        back_tracking(depth+1, n, m)
        out.pop()
        
back_tracking(0, n, m)