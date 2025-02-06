import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

# 보드 입력
board = [list(map(int, input().split())) for _ in range(9)]

# 각 행, 열, 3x3 박스별로 사용된 숫자를 비트마스크로 기록
# 예: row[i]에서 n번째 비트(1<<n)가 1이면, 숫자 n이 이미 사용되었음을 의미
row = [0] * 9
col = [0] * 9
box = [0] * 9

# 빈 칸 좌표 저장 리스트
empty = []

# 초기 상태 설정: 보드에 이미 채워진 숫자들에 대해 비트마스크 기록
for i in range(9):
    for j in range(9):
        num = board[i][j]
        if num:  # 0이 아니라면 숫자가 채워진 칸
            bit = 1 << num
            row[i] |= bit
            col[j] |= bit
            box[(i // 3) * 3 + (j // 3)] |= bit
        else:
            empty.append((i, j))

def backtrack(idx):
    # 모든 빈 칸을 채웠으면 정답 출력 후 종료
    if idx == len(empty):
        for r in board:
            print(*r)
        sys.exit(0)

    # MRV(최소 잔여값) 휴리스틱 적용:
    # 남은 빈 칸 중에서 후보의 개수가 가장 적은 칸을 선택하기 위해
    best = idx
    best_count = 10  # 최대 후보는 9개이므로 10으로 초기화
    for i in range(idx, len(empty)):
        x, y = empty[i]
        b = (x // 3) * 3 + (y // 3)
        # 사용 중인 숫자들을 합치고, 1~9에 해당하는 비트(비트 1~9)를 반전하여 가능한 숫자 후보들을 얻음
        possible = ~(row[x] | col[y] | box[b]) & ((1 << 10) - 2)  # (1<<10)-2 == 0b1111111110, 비트 1~9 사용
        count = bin(possible).count('1')
        if count < best_count:
            best_count = count
            best = i
            # 후보가 1개라면 더 이상 볼 필요 없이 바로 결정
            if count == 1:
                break

    # 선택한 빈 칸을 현재 idx 위치로 옮김
    empty[idx], empty[best] = empty[best], empty[idx]
    x, y = empty[idx]
    b = (x // 3) * 3 + (y // 3)
    possible = ~(row[x] | col[y] | box[b]) & ((1 << 10) - 2)

    # 가능한 숫자 후보들을 하나씩 시도
    while possible:
        # possible에서 가장 낮은 비트(즉, 가장 작은 후보)를 추출
        bit = possible & -possible
        num = bit.bit_length() - 1  # bit의 위치(숫자) 추출 (예, 1<<3이면 num==3)
        board[x][y] = num
        # 해당 숫자를 사용했음을 기록
        row[x] |= bit
        col[y] |= bit
        box[b] |= bit

        backtrack(idx + 1)

        # 백트래킹: 해당 칸을 초기 상태로 되돌림
        board[x][y] = 0
        row[x] &= ~bit
        col[y] &= ~bit
        box[b] &= ~bit

        # 이번 후보를 제거하고 다음 후보 시도
        possible -= bit

backtrack(0)
