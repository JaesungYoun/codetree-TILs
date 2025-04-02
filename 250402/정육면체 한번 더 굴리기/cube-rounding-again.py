from collections import deque
n,m = map(int,input().split())

mat = []
for _ in range(n):
    mat.append(list(map(int,input().split())))

# 동 남 서 북
dx = [0,1,0,-1]
dy = [1,0,-1,0]
d = 0 # 초기방향
x,y = 0,0 # 초기 위치
answer = 0 # 점수
def bfs(mat,x,y,bottom):
    global answer
    q = deque()
    q.append((x,y))
    visited = [[0 for _ in range(n)] for _ in range(n)]
    visited[x][y] = 1
    answer += mat[x][y]
    temp = mat[x][y]
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<n and 0<=ny<n and visited[nx][ny] == 0 and mat[nx][ny] == temp:
                answer += mat[nx][ny]
                q.append((nx,ny))
                visited[nx][ny] = 1

up,front,right = 1,2,3

for i in range(m):
    nx,ny = x+dx[d],y+dy[d]
    if not (0<=nx<n and 0<=ny<n):
        d = (d+2) % 4
        nx,ny = x+dx[d],y+dy[d]

    if d == 0:
        up,front,right = 7-right, front, up
    elif d == 1:
        up,front,right = 7-front, up, right
    elif d == 2:
        up,front,right = right, front, 7-up
    elif d == 3:
        up,front,right = front,7-up,right

    bottom = 7-up
    bfs(mat,nx,ny,bottom)
    if bottom > mat[nx][ny]:
        d = (d+1) % 4
    elif bottom < mat[nx][ny]:
        d = (d+3) % 4
    else:
        d = d

    x,y = nx,ny

print(answer)