import sys
input = sys.stdin.readline

# https://www.acmicpc.net/problem/12015
# 가장 긴 증가하는 부분 수열2
# 이분 탐색을 이용한 LIS 문제
# 수열 A가 주어졌을 때, 가장 긴 증가하는 부분 수열의 길이 출력
n = int(input())

arr = list(map(int, input().split()))  # 제시된 수열

dp = [arr[0]]  # dp 배열에는 반복하면서 지금까지 가장 긴 증가하는 부분 수열의 길이 저장

for i in range(1, n):  # 길이는 1부터 시작하므로
    if arr[i] > dp[-1]: # 가장 마지막 원소보다 크다면
        dp.append(arr[i]) # dp 배열에 추가
    else:
        left, right = 0, len(dp)-1 # 이분 탐색을 위한 left, right 설정
        while left < right: # left와 right가 같아지면 반복문 종료
            mid = (left + right) // 2 # 중간값 설정, 2로 나눈 정수 몫을 반환함
            if dp[mid] >= arr[i]:  # dp[mid]가 arr[i]보다 크거나 같다면
                right = mid # right 변수에 mid 값을 넣고
            else:
                left = mid + 1 # left 값 재설정
        dp[right] = arr[i] # while 문을 빠져나왔을 때 right 값이 가장 큰 값이므로 그 값을 arr[i]로 바꿔줌
        
print(len(dp))


