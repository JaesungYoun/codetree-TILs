from collections import deque








def bfs(x,y,d):
    visited[x][y] = 1
    q = deque()
    q.append((x,y,d))

    while q:
        flag = False
        x,y,d = q.popleft()

        origin_d = d
        for _ in range(4):
            d = (d + 3) % 4

            nx = x + dx[d]
            ny = y + dy[d]

            if 0<=nx<N and 0<=ny<M and visited[nx][ny] == 0 and mat[nx][ny] != 1:
                visited[nx][ny] = 1
                q.append((nx,ny,d))
                flag = True
                break
        else: # 후진
            d = (origin_d + 2) % 4

            back_x = x + dx[d]
            back_y = y + dy[d]
            if 0<=back_x<N and 0<=back_y<M and visited[back_x][back_y] == 0 and mat[back_x][back_y] != 1:
                visited[back_x][back_y] = 1
                q.append((back_x,back_y,d))
                flag = True

        if flag:
            continue
        if not flag:
            return
    return



dx = [-1,0,1,0]
dy = [0,1,0,-1]

N,M = map(int,input().split())

x,y,d = map(int,input().split())

mat = []
for _ in range(N):
    mat.append(list(map(int,input().split())))



visited = [[0 for _ in range(M)] for _ in range(N)]
bfs(x,y,d)
area = 0

for i in range(N):
    for j in range(M):
        if visited[i][j] == 1:
            area += 1

print(area)