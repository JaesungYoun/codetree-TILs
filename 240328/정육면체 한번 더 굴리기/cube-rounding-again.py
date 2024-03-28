from collections import deque
N,M = map(int,input().split())

mat = []
for _ in range(N):
    mat.append(list(map(int,input().split())))

dice = [1,2,3,4,5,6]
def dumbling(dir):
    if dir == 0: # 동
        dice[0], dice[2],dice[3],dice[5] = dice[3], dice[0], dice[5], dice[2]
    elif dir == 1: # 남
        dice[0], dice[1], dice[4], dice[5] = dice[4], dice[0], dice[5], dice[1]
    elif dir == 2: # 서
        dice[0], dice[2], dice[3], dice[5] = dice[2], dice[5], dice[0], dice[3]
    else: # 북
        dice[0], dice[1], dice[4], dice[5] = dice[1], dice[5], dice[0], dice[4]



# 동 남 서 북
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
now_x,now_y = 0,0

score = 0
def move():
    global now_x,now_y,d

    if (0<= now_x + dx[d] < N and 0<= now_y + dy[d] < N):
        now_x = now_x + dx[d]
        now_y = now_y + dy[d]
    else:
        d = (d + 2) % 4
        now_x = now_x + dx[d]
        now_y = now_y + dy[d]

def bfs(x,y):
    visited = [[0 for _ in range(N)] for _ in range(N)]
    q = deque()
    q.append((x,y))
    visited[x][y] = 1
    cnt = 1
    while q:
        x,y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<N and 0<=ny<N and mat[nx][ny] == mat[x][y] and visited[nx][ny] == 0 :
                q.append((nx,ny))
                cnt += 1
                visited[nx][ny] = 1

    return cnt
d = 0
for _ in range(M):
    move()
    dumbling(d)

    sc = bfs(now_x,now_y)

    score += sc * mat[now_x][now_y]
    if mat[now_x][now_y] < dice[5]:
        d = (d+1) % 4
    elif mat[now_x][now_y] > dice[5]:
        d = (d+3) % 4
    else:
        continue

print(score)