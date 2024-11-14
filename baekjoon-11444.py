import sys

input = sys.stdin.readline
# https://www.acmicpc.net/problem/11444
# n이 주어졌을 때, n번째 피보나치 수를 구해야함
# 첫째 줄에 n번째 피보나치 수를 1,000,000,007으로 나눈 나머지를 출력하기
# 분할 정복 이용

n = int(input())

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        fib = [[1, 1], [1, 0]]
        return power(fib, n-1)[0][0]
    
def power(fib, n):
    if n == 1:
        return fib
    else:
        temp = power(fib, n//2)
        if n % 2 == 0:
            return multiply(temp, temp)
        else:
            return multiply(multiply(temp, temp), fib)
    
def multiply(fib1, fib2):
    a = fib1[0][0] * fib2[0][0] + fib1[0][1] * fib2[1][0]
    b = fib1[0][0] * fib2[0][1] + fib1[0][1] * fib2[1][1]
    c = fib1[1][0] * fib2[0][0] + fib1[1][1] * fib2[1][0]
    d = fib1[1][0] * fib2[0][1] + fib1[1][1] * fib2[1][1]
    return [[a % 1000000007, b % 1000000007], [c % 1000000007, d % 1000000007]]


print(fibonacci(n))