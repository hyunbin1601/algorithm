# https://www.acmicpc.net/problem/2805


import sys
input = sys.stdin.readline

n, m = map(int, input().split())

trees = [int(x) for x in input().split()]  # input().split() returns a list of strings, n개 정수를 입력받아 리스트로 저장

# 적어도 m 미터의 나무를 가져가야 한다
# 절단기에 설정할 수 있는 높이의 최댓값을 구하는 문제

def binary_search(n, m, trees):
    # 만약 start, end 변수가 전역변수일 경우, global 키워드를 사용하여 전역변수임을 명시하고 변수값을 변경해야함
    start, end = 1, max(trees) # max(trees)는 trees 리스트의 최댓값을 반환

    while start <= end:
        mid = (start + end) // 2 # //는 몫을 나타내는 연산자
        total = 0  # 가져갈 수 있는 나무의 길이, 반복 시 초기화
        # 우리가 구해야 하는 값은 절단기에 설정할 최댓값을 구해야 함
        for tree in trees:
            if tree > mid:
                total += tree - mid # total에 잘라진 나무의 길이를 더함
        if total < m:
            end = mid - 1
        else:
            start = mid + 1
     # start의 값이 end 값보다 커지면 반복문 탈출       
    return end   # 구해질 end가 최댓값이 될 것임
# 시간복잡도는 O(nlogn) 이다 -> 왜냐하면 이진탐색을 사용했기 때문이다

print(binary_search(n, m, trees))  # 절단기에 설정할 수 있는 높이의 최댓값을 출력

