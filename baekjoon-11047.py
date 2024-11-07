import sys
input = sys.stdin.readline

n, k = map(int,input().split())

coin = []

for _ in range(n):
    coin.append(int(input()))
    
coin.sort(reverse=True)  # coin 배열의 요소들을 내림차순으로 배열함

def greedy(coin, k):
    count = 0
    for i in coin:
        count += k // i  # //는 나누기 연산의 몫을 반환
        # 만약 i의 값이 
        k %= i # 나머지 연산자, k를 i로 나눈 나머지를 k에 저장
    return count

print(greedy(coin, k))