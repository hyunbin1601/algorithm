# https://www.acmicpc.net/problem/31836

import sys
input = sys.stdin.readline

# 해 구성하기 문제
# 두 명이 받게될 기념품에 적힌 피보나치 수의 합이 같아지도록
n = int(input())

# n에 따라 n개의 기념품을 전부 나눠주지 못할 수 있는데, 이때는 최대한 많은 개수의 기념품을 나눠주려고 한다.

# 나눠주는 기념품의 개수를 최대화하면서, 두 명이 받는 기념품에 적힌 수의 합이 같도록 기념품을 나눠주는 방법을 구해보자. 
# 두 사람에게 1개 이상의 기념품을 나눠주는 방법은 항상 존재한다.

# 출력 - 받을 기념품 개수 x, a1, a2, a3, ....를 공백으로 구분해서 출력
# 두번째도 y, b1, b2, b3,....를 공백으로 구분해서 출력
# 가능한 분배 방법이 여러가지 있지만 그중 아무거나 출력
# 기념품에 적힌 번호는 모두 다름
# 최대한 기념품을 많이 나눠줘야함

fib = [0] * (n+1)  # 피보나치 배열 생성
fib[1] = 1
fib[2] = 2
for i in range(3, n+1):
    fib[i] = fib[i-1] + fib[i-2]
    
total = sum(fib[1:n+1])  # 1부터 n까지의 총합
used = [True] * (n+1)

if total % 2 == 1: # 홀수일 경우
    used[1] = False # 1번 기념품은 사용하지 않음
    total -= 1
    
target = total // 2 # 2로 나눈 몫

A = []
current = 0

for i in range(n, 0, -1):
    if not used[i]: # used[i] == False
        continue
    if current + fib[i] <= target:
        current += fib[i]
        A.append(i)
        used[i] = False
     
B = [i for i in range(1, n+1) if used[i]] # used[i]가 True인 i만 B에 추가

print(len(A)) 
print(*A)
print(len(B))
print(*B)


        

        
       
