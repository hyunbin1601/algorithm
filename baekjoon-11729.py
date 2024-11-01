import sys
input = sys.stdin.readline

n = int(input())

# 하노이의 탑에는 오로지 3개의 장판만이 존재한다.
def hanoi(n, start, end):
    if n == 1:
        print(f'{start} {end}')
        return
    else:
        hanoi(n-1, start, 6-start-end)
        print(f'{start} {end}')
        hanoi(n-1, 6-start-end, end)

print(2**n-1)
hanoi(n, 1, 3)

