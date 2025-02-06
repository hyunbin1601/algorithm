import sys

input = sys.stdin.readline

# https://www.acmicpc.net/problem/10986
# 나머지 합 / 누적 합 문제
# 수 N개 A1, A2, ..., AN -> 이때, 연속된 부분 구간의 합이 M으로 나누어 떨어지는 구간의 개수를 구하는 프로그램
# 즉, Ai + ... + Aj (i ≤ j) 의 합이 M으로 나누어 떨어지는 (i, j) 쌍의 개수

n, m = map(int, input().split())

array = list(map(int, input().split()))

# 나머지 합을 저장하는 배열
remainder = [0] * m

# 나머지 합을 저장하는 배열의 첫번째 요소는 1로 초기화
remainder[0] = 1

# 누적 합
sum = 0
count = 0

for i in array:
    sum += i
    # 누적 합을 M으로 나눈 나머지를 저장
    sum %= m
    # 나머지 합을 저장하는 배열의 sum번째 요소를 1 증가
    remainder[sum] += 1
    
for i in remainder:
    # 나머지 합이 2 이상인 경우, iC2의 경우의 수를 구한다
    count += i * (i - 1) // 2
    
print(count)

