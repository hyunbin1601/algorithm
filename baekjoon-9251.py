import sys

input = sys.stdin.readline

# lcs 문제 (최장 공통 부분 수열)
# 동적 계획법 사용
# 두 문자열이 두 줄에 걸쳐 주어질 때, 두 문자열의 lcs의 길이 출력

s1 = input().rstrip() # 오른쪽 공백 제거 -> 왜 여백을 제거하는거야? -> 문자열의 끝에 있는 개행문자를 제거하기 위함 -> 왜? -> 개행문자가 있으면 문자열의 길이가 달라질 수 있음
s2 = input().rstrip() 

dp = [[0] * (len(s1) + 1) for _ in range(len(s2) + 1)] # 0으로 초기화
# s2의 문자열을 기준으로 s1의 문자열과 비교해나가며 풀어나간다

for i in range(1, len(s2) + 1):
    for j in range(1, len(s1)+1):
        if s2[i-1] == s1[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])
# s1의 i번째 문자와 s2의 j번째 문자가 같다면, dp[i][j] = dp[i-1][j-1] + 1

print(dp[-1][-1]) # s1의 마지막 문자와 s2의 마지막 문자까지의 lcs의 길이 출력
# 왜 dp[-1][-1]로 출력하는거야? 왜 이게 길이를 나타내는거야? -> dp의 마지막 요소가 lcs의 길이를 나타내기 때문