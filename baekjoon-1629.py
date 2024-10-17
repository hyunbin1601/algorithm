import sys
input = sys.stdin.readline

a, b, c = map(int, input().split())

def divide_and_conquer(a, b, c):
    if b == 1:
        return a % c # %는 파이썬에서 나머지를 구하는 연산자
    elif b % 2 == 0:
        return divide_and_conquer(a, b//2, c) ** 2 % c # **는 파이썬에서 제곱을 구하는 연산자, 재귀 후 제곱을 구하는 이유는 분할정복을 사용하기 위함
    else:  # 매번 재귀 호출에서 b를 절반으로 줄이기 때문에, 재귀 호출의 깊이는 logb에 비례함
        return divide_and_conquer(a, b-1, c) * a % c  # 각 재귀 호출에서 수행되는 연산은 상수 시간 O(1)
    
print(divide_and_conquer(a, b, c)) # a의 b제곱을 c로 나눈 나머지를 출력