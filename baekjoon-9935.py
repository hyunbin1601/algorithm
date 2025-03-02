import sys
input = sys.stdin.readline

# https://www.acmicpc.net/problem/9935
# 문자열 폭발(스택 문제)

# 문자열 입력
s = input().strip()
# 폭발 문자열
bomb = input().strip()

# 스택 생성
stack = []

# 폭발 문자열의 마지막 문자
last_char = bomb[-1]

# 폭발 문자열의 길이
bomb_len = len(bomb)

for char in s:
    stack.append(char)  # 일단 넣고 본다
    # 폭발 문자열의 마지막 문자와 같다면
    if char == last_char and ''.join(stack[-bomb_len:]) == bomb: # stack에 들어있는 값을 문자열로 변환해서 출력
        del stack[-bomb_len:]
        
# 스택이 비어있다면 "FRULA" 출력
if not stack:
    print("FRULA")
    
# 스택이 비어있지 않다면 스택 출력
else:
    print(''.join(stack)) 