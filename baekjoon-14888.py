import sys
input = sys.stdin.readline # 입력에서 개행 문자를 포함해서 받음

# n개의 수로 이루어진 수열
# 수와 수 사이에 끼워넣을 n-1개의 연산자
# 연산자는 덧 뺄 곱 나 중 하나

# 나눗셈은 정수 나눗셈으로 몫만 취함
# 음수를 양수로 나눌 때는 양수로 바꾼 뒤 몫을 취하고 그 몫을 음수로 바꿈
# 식의 계산은 연산자 우선 순위를 무시하고 앞에서부터 진행

# 첫째줄 : 최댓값
# 둘째줄 : 최솟값

n = int(input())
nums = list(map(int, input().split())) # 수열

add, sub, mul, div = map(int, input().split()) 
# 각각 덧셈, 뺄셈, 곱셈, 나눗셈의 수

max_val = -int(1e9)   # 최댓값은 음수 무한대로 초기화해서 초기값과 비교하도록 함
min_val = int(1e9) # 최솟값은 양수 무한대로 초기화해서 초기값과 비교하도록 함


def back_tracking(nums, add, sub, mul, div, depth, result): # depth는 현재 수열의 길이
    global max_val, min_val
    if depth == n: # depth가 n에 도달했을때 재귀 종료
        max_val = max(max_val, result)
        min_val = min(min_val, result)
        return
    else:
        if add:  # add, sub, mul, div의 값이 0이 아닐 경우 if문 수행
            back_tracking(nums, add-1, sub, mul, div, depth+1, result+nums[depth]) # 인덱스는 0부터 시작
        if sub:
            back_tracking(nums, add, sub-1, mul, div, depth+1, result-nums[depth])
        if mul:
            back_tracking(nums, add, sub, mul-1, div, depth+1, result*nums[depth]) 
        if div:
            if result < 0:
                back_tracking(nums, add, sub, mul, div-1, depth+1, -((-result)//nums[depth]))
            else:
                back_tracking(nums, add, sub, mul, div-1, depth+1, result//nums[depth])
            
back_tracking(nums, add, sub, mul, div, 1, nums[0])  # 수열의 첫번째 요소부터 시작

print(max_val)
print(min_val)