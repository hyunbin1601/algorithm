import sys
import math
# 투 포인터 문제
# 자연수가 주어졌을 때, 이 자연수를 연속된 소수의 합으로 나타낼 수 있는 경우의 수 구하기

input = sys.stdin.readline

n = int(input())

array = [True] * (n + 1)
array[0] = False
array[1] = False

if n == 1:
    print(0)
else:
    # 에라토스테네스의 체
    # 2부터 시작해서 주어진 범위 내의 수를 소수로 가정하고 시작
    # 2부터 시작해, 현재 수의 배수 모두 제거
    for i in range(2, int(math.sqrt(n) + 1)):
        if array[i] == True:
            j = 2 # j값 초기화
            while (i * j) <= n:
                array[i * j] = False # 배수일 경우 False로 변경
                j += 1
                
    prime = [i for i in range(2, n + 1) if array[i] == True]  # true인 값들만 소수 배열에 저장
    
        
    start = 0
    end = 0
    count = 0
    sum = prime[0]
    
    while True:
        if sum == n:
            count += 1
            sum -= prime[start]
            start += 1
        elif sum > n:
            sum -= prime[start]
            start += 1
        else: # sum < n인 경우
            end += 1
            if end == len(prime):
                break # 인덱스 벗어난 경우
            sum += prime[end] # end를 증가시켜 sum 값 증가시킴
            
    print(count)
    
