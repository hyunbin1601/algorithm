import sys
input = sys.stdin.readline

n, m = map(int, input().split())  # 랜선의 개수와 필요한 랜선의 개수 입력
line = [int(input()) for _ in range(n)]
line.sort() # 함수 호출 및 오름차순 정렬

# 배열의 시작점과 끝점을 설정
def binary_search():
    start = 1   # 자를 랜선의 최소 길이를 의미함, 자를 랜선의 최소 길이는 1부터 시작함
    end = line[-1]
    while start <= end:
        mid = (start + end) // 2   # 중간값 설정
        count = 0
        for i in line:
            count += i // mid
        if count >= m:
            start = mid + 1
        else:
            end = mid - 1
    return end

print(binary_search())