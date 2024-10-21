def binary(A, p, s, e):  # p는 찾고자 하는 값
    if s > e:
        return -1
    mid = (s + e) // 2  # //는 몫을 구하는 연산자
    if A[mid] == p:
        return mid
    elif A[mid] > p:
        return binary(A, p, s, mid-1)
    else:
        return binary(A, p, mid+1, e)
    
## 정렬된 배열에서 특정 수의 개수 구하기 -> bisect 이용
from bisect import bisect_left, bisect_right
def count_by_range(a, left_value, right_value):
    right_index = bisect_right(a, right_value)
    left_index = bisect_left(a, left_value)
    return right_index - left_index  # 값이 left value, right value인 데이터의 개수 반환

count = count_by_range(a, x, x) # a라는 배열에서 x, x라는 범위에 있는 데이터의 개수 반환