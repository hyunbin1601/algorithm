import sys
input = sys.stdin.readline

# https://www.acmicpc.net/problem/15652

# 1부터 N까지 자연수 중에서 M개를 고른 수열
# 같은 수를 여러 번 골라도 된다.
# 고른 수열은 비내림차순이어야 한다.
# 길이가 K인 수열 A가 A1 ≤ A2 ≤ ... ≤ AK-1 ≤ AK를 만족하면, 비내림차순이라고 한다.

n, m = map(int, input().split())
out = []

def back_tracking(depth, n, m):
    if depth == m:
        print(' '.join(map(str, out)))
        return
    
    for i in range(n):
        if not out or out[-1] <= i+1:  # out 리스트가 비어있거나 or 현재 배열의 마지막 값이 i+1보다 작거나 같은 경우
            out.append(i+1)
            back_tracking(depth+1, n, m)
            out.pop()
            
            
back_tracking(0, n, m)