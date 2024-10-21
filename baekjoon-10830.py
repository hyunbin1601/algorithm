import sys
input = sys.stdin.readline

n, b = map(int, input().split())

def matrix_pow(matrix, b):
    if b == 1:
        for i in range(n):
            for j in range(n):
                matrix[i][j] %= 1000
        return matrix
    elif b % 2 == 0:
        temp = matrix_pow(matrix, b // 2)
        result = [[0] * n for _ in range(n)]  # 0으로 초기화된 n x n 행렬 생성
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    result[i][j] += temp[i][k] * temp[k][j]  # 행렬의 곱셈 연산, result[i][j]에 temp[i][k] * temp[k][j]의 값을 더함
                result[i][j] %= 1000   # 1000으로 나눈 나머지를 저장, 1000보다 클 경우 저장됨
        return result # 2로 나누어 떨어지는 경우, 제곱수를 반으로 나누어 계산, 재귀적으로 호출
    else:
        temp = matrix_pow(matrix, b-1) # b-1을 왜 호출하는가? -> b가 홀수일 경우, b-1로 호출하여 짝수로 만들어준다
        result = [[0] * n for _ in range(n)]   # 0으로 초기화된 n x n 행렬 생성
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    result[i][j] += temp[i][k] * matrix[k][j]  # 행렬의 곱셈 연산, result[i][j]에 temp[i][k] * matrix[k][j]의 값을 더함
                result[i][j] %= 1000
        return result
    
matrix = [list(map(int, input().split())) for _ in range(n)]  # n개만큼의 list를 생성함
answer = matrix_pow(matrix, b)
# 출력값이 행렬로 나오게 됨 -> 이를 출력하기 위해서는 for문을 이용하여 출력해야 함
for i in range(n):
    for j in range(n):
        print(answer[i][j], end=' ')  # answer[0][0] answer[0][1] 이렇게 출력함
    print()  # 한 줄 출력 후 개행을 해줌 -> print()만 있으면 개행(줄바꿈)이 됨

    
# 행렬의 거듭제곱을 계산하는 문제를 해결하기 위한 분할정복 알고리즘
# temp = matrix_pow(matrix, b-1)인 이유? -> b가 홀수일 경우, b-1로 호출해서 짝수로 만들어줘야 하기 때문...! 짝수 지수로 만들어야 절반으로 나누어 재귀 호출할 수 있으므로 계산이 더욱 효율적이게 됨
# temp로 재귀 호출을 통해 최종 반환된 행렬을 저장함, 중복 계산을 피하기 위한 임시값

# 시간복잡도 -> b를 절반으로 나누어 재귀 호출하므로, 재귀 호출의 깊이는 O(lob b)가 된다
# 행렬 곱셈 -> 각 재귀 호출에서 행렬 곱셈을 수행하는데, 행렬 곱셈의 시간 복잡도는 O(n^3) 이다. 왜냐하면 행렬의 곱셈 연산은 3개의 중첩된 반복문을 사용하기 때문에(n * n * n) 시간복잡도는 O(n^3)
# !아래는 행렬 곱셈임! #
# for i in range(n):
#     for j in range(n):
#         C[i][j] = 0
#         for k in range(n):
#             C[i][j] += A[i][k] * B[k][j]