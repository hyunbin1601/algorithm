import sys
input = sys.stdin.readline

n = int(input()) 
# n개의 줄에 s가 주어짐
start_and_link = [list(map(int, input().split())) for _ in range(n)]
# start_and_link는 이차원 배열로, n번동안 각각 n번의 입력을 받음

min_val = int(1e9) # 최솟값은 양수 무한대로 초기화해서 초기값과 비교하도록 함


def back_tracking(start_and_link, depth, start, link):
    # start와 link는 팀의 인덱스를 저장하는 배열
    global min_val # 전역변수 접근
    if depth == n: # depth가 n에 도달했을때 재귀 종료
        start_sum = 0 # start팀 능력치 합
        link_sum = 0 # link팀 능력치 합합
        for i in range(n//2):
            for j in range(n//2):
                if i == j:
                    continue  # i, j의 값이 같을 때에는 이번 반복은 넘어감
                start_sum += start_and_link[start[i]][start[j]] # start 배열이 어느정도 요소값이 들어왔을때
                # 이 반복에서 어차피 (i, j)인 경우와 (j, i)인 경우를 모두 고려하게 되어있음
                link_sum += start_and_link[link[i]][link[j]] # 마찬가지로 link 배열이 어느정도 요소값이 들어왔을때
                # start와 link의 배열에는 각각 start_and_link 배열의 반씩 서로 나눠 들어간다
        min_val = min(min_val, abs(start_sum - link_sum))
        return
    else:
        if len(start) < n//2:
            start.append(depth)
            back_tracking(start_and_link, depth+1, start, link) # 재귀 호출 시 start, link에 값이 들어가는데, n//2로 나눌 수 있는 팀의 묶음 경우의 수들이 들어감
            start.pop() # 왜 pop을 하는거야? -> 다음 재귀함수를 위해 pop을 해줘야함
        if len(link) < n//2:
            link.append(depth)
            back_tracking(start_and_link, depth+1, start, link)
            link.pop() # 재귀 호출이 끝난 후에는 이전 상태로 되돌아가야 함 -> 그러기 위해 pop을 이용해서 현재 상태에서 추가된 요소를 제거하고 이전 상태로 되돌아감
    

start = []
link = []
back_tracking(start_and_link, 0, start, link)
print(min_val)
# 출력해야 되는 것은 start와 link 팀 능력치 차이의 최솟값
