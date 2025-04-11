import sys
input = sys.stdin.readline

n = int(input().strip())
students = list(map(int, input().split()))

stack = []
expected = 1

for student in students:
    if student == expected:
        expected += 1
        while stack and stack[-1] == expected:
            stack.pop()
            expected += 1
    else:
        stack.append(student)

if expected == n + 1:
    print("Nice")
else:
    print("Sad")

        