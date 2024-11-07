import sys
input = sys.stdin.readline

city = int(input())  # 도시의 개수
distance = list(map(int, input().split())) # 도로의 길이
price = list(map(int, input().split())) # 리터당 가격



def greedy(distance, price):
    min_price = price[0]  # 최소 가격 
    result = 0

    for i in range(city-1):  # 도로의 길이 배열을 탐색함
        if price[i] < min_price:
            min_price = price[i]
        result += min_price * distance[i]
    return result

print(greedy(distance, price))