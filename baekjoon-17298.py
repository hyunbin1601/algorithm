import sys
input = sys.stdin.readline

# https://www.acmicpc.net/problem/17298
# 오큰수, 스택 문제

# 오큰수는 오른쪽에 있으면서 자신보다 큰 수중 가장 왼쪽에 있는 수를 의미함

n = int(input())
array = list(map(int, input().split())) # 띄어쓰기 단위로 입력받음
# 리스트 i번째 값의 오큰수를 저장할 배열(i번에 오큰수 저장)
result = [-1] * n 

# 스택 생성
stack = []

for i in range(n):
    # while문은 걸린 조건이 true인 경우에만 반복하고 그 외에는 탈출
    while stack and array[i] > array[stack[-1]]: # 스택의 마지막 값보다 현재 배열의 값이 더 큰 경우
        result[stack.pop()] = array[i] # 스택의 마지막 값을 빼서, result에 현재 배열의 값을 넣음
    stack.append(i)
    
print(' '.join(map(str, result))) # result 배열을 하나하나씩 str으로 변환 후 띄어쓰기 단위로 출력
    
