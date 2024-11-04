# https://www.acmicpc.net/problem/24060

import sys

input = sys.stdin.readline

n , k = map(int, input().split())
array = [int(x) for x in input().split()]
cnt = 0
result = -1 # 초기화

# 배열 a를 오름차순 정렬 시, 새로운 배열에 오름차순 식으로 저장한다고 가정한다.
# 이 때, k번째 저장된 값을 구하는 문제
# 만약 k의 값이 총 저장횟수보다 크다면 -1을 출력한다.
# cnt == k가 되는 순간, 해당 값을 출력한다.
# merge_sort(A[p..r]) { # A[p..r]을 오름차순 정렬한다.
#     if (p < r) then {
#         q <- ⌊(p + r) / 2⌋;       # q는 p, r의 중간 지점
#         merge_sort(A, p, q);      # 전반부 정렬
#         merge_sort(A, q + 1, r);  # 후반부 정렬
#         merge(A, p, q, r);        # 병합
#     }
# }

# # A[p..q]와 A[q+1..r]을 병합하여 A[p..r]을 오름차순 정렬된 상태로 만든다.
# # A[p..q]와 A[q+1..r]은 이미 오름차순으로 정렬되어 있다.
# merge(A[], p, q, r) {
#     i <- p; j <- q + 1; t <- 1;
#     while (i ≤ q and j ≤ r) {
#         if (A[i] ≤ A[j])
#         then tmp[t++] <- A[i++]; # tmp[t] <- A[i]; t++; i++;
#         else tmp[t++] <- A[j++]; # tmp[t] <- A[j]; t++; j++;
#     }
#     while (i ≤ q)  # 왼쪽 배열 부분이 남은 경우
#         tmp[t++] <- A[i++];
#     while (j ≤ r)  # 오른쪽 배열 부분이 남은 경우
#         tmp[t++] <- A[j++];
#     i <- p; t <- 1;
#     while (i ≤ r)  # 결과를 A[p..r]에 저장
#         A[i++] <- tmp[t++]; 
# }

def merge_sort(array):
    global k, cnt, result
    if len(array) <= 1:
        return array
    mid = len(array) // 2
    left = merge_sort(array[:mid])
    right = merge_sort(array[mid:])
    
    return merge(left, right)
        
def merge(left, right):
    global k, cnt, result
    sorted_array = []
    i = 0
    j = 0
    while i<len(left) and j < len(right):
        if left[i] <= right[j]:
            sorted_array.append(left[i])
            i += 1
        else:
            sorted_array.append(right[j])
            j += 1   
        cnt += 1
        if cnt == k:
            result = sorted_array[-1]
            
    while i < len(left):
            sorted_array.append(left[i])
            i += 1
            cnt += 1
            if cnt == k:
                result = sorted_array[-1]
    while j < len(right):
            sorted_array.append(right[j])
            j += 1
            cnt += 1
            if cnt == k:
                result = sorted_array[-1]
    return sorted_array
    
    

merge_sort(array) 
print(result)
        
        
            
    
    