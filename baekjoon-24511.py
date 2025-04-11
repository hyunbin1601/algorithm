import sys
input = sys.stdin.readline
from collections import deque
# https://www.acmicpc.net/problem/24511

# queuestack 문제
# 큐와 스택을 이용한 문제
# queuestack의 작동은 다음과 같다.
# $x_0$을 입력받는다.
# $x_0$을 $1$번 자료구조에 삽입한 뒤 $1$번 자료구조에서 원소를 pop한다. 그때 pop된 원소를 $x_1$이라 한다.  
# $x_1$을 $2$번 자료구조에 삽입한 뒤 $2$번 자료구조에서 원소를 pop한다. 그때 pop된 원소를 $x_2$이라 한다.
# $x_{N-1}$을 
# $N$번 자료구조에 삽입한 뒤 
# $N$번 자료구조에서 원소를 pop한다. 그때 pop된 원소를 
# $x_N$이라 한다.
# $x_N$을 리턴한다.
# 길이 $M$의 수열 $C$를 가져와서 수열의 원소를 앞에서부터 차례대로 queuestack에 삽입할 것이다. 이전에 삽입한 결과는 남아 있다.
# queuestack에 넣을 원소들이 주어졌을 때, 해당 원소를 넣은 리턴값을 출력하는 프로그램을 작성해보자

n = int(input()) # queuestack을 구성하는 자료구조의 개수 n
a_list = list(map(int, input().split()))
# a_list는 i번 자료구조가 큐일 경우 a_list[i]=0, 스택이면 1
b_list = list(map(int, input().split()))
# b_list는 i번 자료구조에 있는 원소

m = int(input())
# 삽입할 수열의 길이 m
c_list = list(map(int, input().split())) # 해당 리스트의 원소를 차례대로 queuestack에 삽입했을 때의 리턴값을 공백으로 구분하여 출력

queuestack = [None] * (n+1)
queuestack[0] = 0 # 왜 더미값?

for i in range(n): # queuestack을 구성하는 자료구조의 개수 n
    if a_list[i] == 0: # i번 자료구조가 큐일 경우
        queuestack[i+1] == deque() # 큐를 추가 -> deque
    else: # i번 자료구조가 스택일 경우
        queuestack[i+1] = [] # 스택을 추가 -> 리스트
        
# 각 자료구조에 초기원소값 b_list를 넣어줌
for i in range(n):
    queuestack[i+1].append(b_list[i])
    
result = []
        
for c in c_list:
    if a_list[0] == 0:
        queuestack[1].append(c)
        x = queuestack,[1].popleft()
    else:
        queuestack[1].append(c)
        x = queuestack[1].pop()
        
    for i in range(2, n+1):
        if a_list[i-1] == 0:
            queuestack[i].popleft()
            x = queuestack[i].popleft()
            
        else:
            queuestack[i].append(x)
            x = queuestack[i].pop()
            
    result.append(x)
    
print(" ".join(map(str, result)))

    
    

