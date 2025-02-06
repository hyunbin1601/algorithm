import sys

input = sys.stdin.readline

# 행렬의 곱셈
# https://www.acmicpc.net/problem/2740

def matrix_multiplication(n, m, a, k, b):
    result = [[0] * k for _ in range(n)]
    
    for i in range(n):
        for j in range(k):
            for l in range(m):
                result[i][j] += a[i][l] * b[l][j]
    
    return result   

def main():
    n, m = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(n)]
    m, k = map(int, input().split())
    b = [list(map(int, input().split())) for _ in range(m)]
    
    result = matrix_multiplication(n, m, a, k, b)
    
    for i in range(n):
        for j in range(k):
            print(result[i][j], end=" ")
        print()
        
if __name__ == "__main__":
    main()