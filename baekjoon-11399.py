import sys
input = sys.stdin.readline

n = int(input())
time = list(map(int, input().split()))

time.sort()  # time 배열 -> 오름차순 정렬

def greedy(time):
    result = 0
    time_wait = 0
    for i in range(n):
        time_wait += time[i]
        result += time_wait
    return result

print(greedy(time))
        