import sys

input = sys.stdin.readline

# 수열의 크기 n
n = int(input())

# 수열에 포함되는 수
array = list(map(int, input().split()))  # 스페이스바로 받는 값을 int형변환해서 받음
array.sort()
# 특정 값 x
x = int(input())

# ai + aj = x를 만족하는 (ai, aj) 쌍의개수

def two_pointer():
    count = 0
    start = 0
    end = n - 1 # 끝 인덱스
    
    while start < end:
        sum = array[start] + array[end]
        
        if sum == x:
            count += 1
            start += 1
            end -= 1
            
        elif sum < x:
            start += 1
        else:
            end -= 1
            
    return count

print(two_pointer())