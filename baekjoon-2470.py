import sys

input = sys.stdin.readline

# 전체 용액의 수
n = int(input())

# 용액의 특성값
array = list(map(int, input().split()))
array.sort()

# 특성값이 0에 가까운 용액 만들기
# 투 포인터 문제

def two_pointer():
    start = 0
    end = n-1
    closest_sum = float('inf') # 무한에 가까운 값
    result = (0, 0) # 튜플로 초기화함
    
    while start < end:
        current_sum = array[start] + array[end]
        
        if abs(current_sum) < abs(closest_sum):
            closest_sum = current_sum
            result = (array[start], array[end])
            
        if current_sum == 0:
            break  # 루프 탈출
        elif current_sum < 0:
            start += 1
        else:
            end -= 1
    return result

result = two_pointer()

print(result[0], result[1]) # 튜플의 값을 하나씩 불러낼 때도 []의 인덱스로 호출
    