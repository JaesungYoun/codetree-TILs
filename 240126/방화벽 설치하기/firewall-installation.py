from collections import deque
N,M = map(int,input().split())



mat = []
visited = [[0 for _ in range(M)] for _ in range(N)]
for _ in range(N):
    mat.append(list(map(int,input().split())))


dx = [-1,1,0,0]
dy = [0,0,-1,1]
def bfs():
    global answer
    tmp_mat = [i[:] for i in mat]
    temp = []
    queue = deque()
    for x in range(N):
        for y in range(M):
            if mat[x][y] == 2:
                queue.append((x,y))
                temp.append((x,y))
    while queue:
        x,y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<= nx < N and 0 <= ny < M and mat[nx][ny] == 0:
                queue.append((nx,ny))
                mat[nx][ny] = 2

    cnt = 0
    for i in range(N):
        cnt += mat[i].count(0)
    answer = max(answer,cnt)
    for x in range(N):
        for y in range(M):
            if mat[x][y] == 2 and (x,y) not in temp:
                mat[x][y] = 0








def backtracking(depth):
    if depth == 3:
        bfs()
        return

    for i in range(N):
        for j in range(M):
            if mat[i][j] == 0:
                mat[i][j] = 1
                backtracking(depth+1)
                mat[i][j] = 0

answer = 0
backtracking(0)
print(answer)