from collections import deque

N, M = map(int, input().split())

mat = []
for _ in range(N):
    mat.append(list(map(int, input().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs():
    global answer
    tmp_mat = [i[:] for i in mat]

    queue = deque()
    for x in range(N):
        for y in range(M):
            if tmp_mat[x][y] == 2:
                queue.append((x, y))

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < M and tmp_mat[nx][ny] == 0:
                queue.append((nx, ny))
                tmp_mat[nx][ny] = 2

    cnt = 0
    for i in range(N):
        cnt += tmp_mat[i].count(0)
    answer = max(answer, cnt)

def backtracking(depth):
    if depth == 3:
        bfs()
        return
    for i in range(N):
        for j in range(M):
            if mat[i][j] == 0:
                mat[i][j] = 1
                backtracking(depth + 1)
                mat[i][j] = 0



answer = 0
backtracking(0)
print(answer)