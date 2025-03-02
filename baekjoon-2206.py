import sys

input = sys.stdin.readline

n, m = map(int, input().split())
a = [list(map(int, input().strip())) for _ in range(n)]

def bfs():
    q = [(0, 0, 1)]
    visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]
    visited[0][0][1] = 1

    while q:
        x, y, z = q.pop(0)

        if x == n - 1 and y == m - 1:
            return visited[x][y][z]

        for dx, dy in (1, 0), (-1, 0), (0, 1), (0, -1):
            nx, ny = x + dx, y + dy

            if 0 <= nx < n and 0 <= ny < m:
                if not a[nx][ny] and not visited[nx][ny][z]:
                    visited[nx][ny][z] = visited[x][y][z] + 1
                    q.append((nx, ny, z))

                if z and a[nx][ny] and not visited[nx][ny][0]:
                    visited[nx][ny][0] = visited[x][y][z] + 1
                    q.append((nx, ny, 0))

    return -1