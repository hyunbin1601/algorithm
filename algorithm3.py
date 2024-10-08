import sys
input = sys.stdin.readline

n, k = map(int, input().split())
arr = []
arr = input().split()
arr = [int(x) for x in arr]
arr2 = []
for i in range(k):
    num1, num2 = map(int, input().split())
    arr2.append(sum(arr[num1-1:num2]))

for i in range(len(arr2)):
    print(arr2[i])