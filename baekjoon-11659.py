import sys
input = sys.stdin.readline

# 누적 합 문제
# 구간 합 구하기, dp 배열 이용해서 누적 합 구함
n, m = map(int, input().split())

number_array = [0] + list(map(int, input().split())) # 0을 추가해서 인덱스를 1부터 시작하게 만듦
# 왜 0을 추가하는거지? -> 인덱스를 1부터 시작하게 만들기 위해서
# 구간합을 저장할 배열 / 숫자가 저장될 배열

dp = [0] * (n + 1) # 0으로 초기화
# number_array가 n+1개의 원소가 있으므로 마찬가지로 dp도 ㅇㅇ

panel = []

for i in range(m):
    panel.append(list(map(int, input().split())))
    
for i in range(1, n+1):
    # 1부터 인덱스 n번까지
    dp[i] = dp[i-1] + number_array[i]  # dp[0]은 사실 0이라 의미없음
    # dp[i]는 1부터 i까지의 합을 저장
    
for i in panel:
    # panel의 각 원소에 대해
    # panel은 이차원 배열, i는 panel의 각 소배열들을 하나씩 가져옴
    print(dp[i[1]] - dp[i[0]-1]) # 왜 1을 빼는거야? -> 만약 1,3이라고 가졍해보자. i[1] = 3, i[0] = 1이 되는데, 1번째 인덱스도 포함이 되므로 0번째 인덱스까지를 j번째 인덱스까지의 합에서 제외해야 한다.