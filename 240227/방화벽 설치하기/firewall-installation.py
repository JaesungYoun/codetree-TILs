from collections import deque

n,m = map(int,input().split())

mat = []
for _ in range(n):
    mat.append(list(map(int,input().split())))

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs():
    global answer
    tmp_mat = [i[:] for i in mat]

    queue = deque()
    for x in range(n):
        for y in range(m):
            if tmp_mat[x][y] == 2:
                queue.append((x,y))

    while queue:
        x,y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<n and 0<=ny<m and tmp_mat[nx][ny] == 0:
                tmp_mat[nx][ny] = 2
                queue.append((nx,ny))


    cnt = 0
    for i in tmp_mat:
        cnt += i.count(0)

    answer = max(answer,cnt)
    return


def dfs(cnt):
    if cnt == 3:
        bfs()
        return

    for i in range(n):
        for j in range(m):
            if mat[i][j] == 0: # 빈자리일 때
                mat[i][j] = 1 #방화벽 세우기
                dfs(cnt + 1)
                mat[i][j] = 0

answer = 0
dfs(0)
print(answer)