import sys
input = sys.stdin.readline

# 특정 문자열 s, a이 주어졌을 때,s의 l번째 문자부터 r번째 문자 사이에 a가 몇 번 나타나는지 구하는 프로그램을 작성 

s = input().rstrip() # 오른쪽 공백 제거
q = int(input()) # 질문 개수
# i, r이 주어지는데, s의 i번째 문자부터 r번째 문자 사이에 a가 몇개 나타나는지 각 줄마다 출력하기
# 알파벳 소문자의 개수는 26개
# 누적 합 문제

dp = [[0] * 26 for _ in range(len(s)+1)] # 0으로 초기화
for i in range(1, len(s) + 1):  # 인덱스 1번부터 인덱스 len(s)번까지 dp 설정 
    for j in range(26):
        dp[i][j] = dp[i-1][j] + (s[i-1] == chr(j+97)) # 소문자만 나올 수 있다고함
        # dp[i][j]는 1부터 i까지의 문자열에서 j번째 알파벳이 나타난 횟수를 저장함
# print(dp)

for _ in range(q):
    a, l, r = input().split() # 공백을 기준으로 각 변수에 값이 할당됨
    l = int(l)
    r = int(r)
    # l, r 구간에 문자열 a가 얼마나 나타나는지 출력
    # chr -> 정수를 유니코드 문자로
    # ord -> 유니코드 문자를 유니코드 정수로
    print(dp[r+1][ord(a)-97] - dp[l][ord(a)-97]) # r+1번째까지의 a의 개수 - l번째까지의 a의 개수를 출력함
    # 왜 r+1번째를....? -> 현재 dp에는 문자열 길이보다 1개 더 큰 배열이 저장되어 있음.
    # 그렇기에 +1 인덱스로 계산해야함
    # print(dp[r+1][ord(a)-97])에서 ord(a)-97은 아스키코드로 변환한 후 a의 아스키 코드인 97을 빼주는 것 그러면 소문자 기준 0번째 알파벳부터 시작하게 됨
    # dp는 주어진 문자열 기준 i번째까지의 문자열에서 계산하는것
    # 이는 주어진 입력값이 0번째 인덱스 기준으로 주어지기 때문에 +1을 해야하는 것임! 주의!

    
    
