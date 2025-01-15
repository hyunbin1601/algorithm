import sys

input = sys.stdin.readline

n, s = map(int, input().split())
array = list(map(int, input().split()))

# 수열에서 연속된 수들의 부분합 중에 그 합이 S 이상이 되는 것 중, 가장 짧은 것의 길이 구하기
# 만약 s 이상이 되는 합을 만드는 게 어렵다면 0 출력

start = 0
end = 0
# 투 포인터 이용
sum = 0 # 부분합

result = 100001 # 최댓값, 10 ≤ N < 100,000 이므로(n은 수열의 길이)

while True:
    if sum >= s: # 현재 부분합이 s 이상인 경우
        result = min(result, end - start) # 현재 길이와 result 중 작은 값을 result로 갱신
        sum -= array[start] # start 값 갱신 -> 더 짧은 길이 찾기
        start += 1
    elif end == n: # end가 n이 되면 break
        break
    else: # 현재 부분합이 s 미만인 경우
        sum += array[end]
        end += 1
        
if result == 100001: # result가 초기값 그대로라면 0 출력
    print(0)
else:
    print(result)
    

    

