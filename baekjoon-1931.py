import sys
input = sys.stdin.readline

n = int(input())

# 각 회의가 겹치지 않게 하면서 회의실을 사용할 수 있는 회의의 최대 개수

meeting_time = []

for _ in range(n):
    start, end = map(int, input().split())
    meeting_time.append((start, end))
    
meeting_time.sort(key=lambda x: (x[1], x[0]))

def greedy(meeting_time):
    count = 0
    end_time = 0
    for start, end in meeting_time:
        if start >= end_time:
            count += 1
            end_time = end
    return count

print(greedy(meeting_time))