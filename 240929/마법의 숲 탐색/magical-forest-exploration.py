from collections import deque
r,c,k = map(int,input().split())

MAX_L = 70
mat = [[0 for _ in range(MAX_L)] for _ in range(MAX_L+3)]
# 북 동 남 서 (-> 시계방향)
dx = [-1,0,1,0]
dy = [0,1,0,-1]
isExit = [[0 for _ in range(MAX_L)] for _ in range(MAX_L+3)]

def resetMat():
    for i in range(r + 3):
        for j in range(c):
            mat[i][j] = 0
            isExit[i][j] = 0

def in_range(x,y):
    return 3 <= x < r+3 and 0<= y < c

# x,y 로 이동할 수 있는지에 대해 체크하는 함수
def canMove(x,y):
    flag = x < r + 2 and 1 <= y < c-1
    flag = flag and mat[x+1][y] == 0
    flag = flag and mat[x][y-1] == 0
    flag = flag and mat[x][y+1] == 0
    flag = flag and mat[x-1][y-1] == 0
    flag = flag and mat[x-1][y+1] == 0
    flag = flag and mat[x][y] == 0
    return flag


def bfs(x,y):
    max_x = 0
    q = deque()
    q.append((x,y))
    visit = [[0 for _ in range(c)] for _ in range(r+3)]
    while q:
        x,y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if in_range(nx,ny) and not visit[nx][ny] and ((mat[nx][ny] == mat[x][y]) or (mat[nx][ny] != 0 and isExit[x][y])):
                q.append((nx,ny))
                visit[nx][ny] = True
                max_x = max(max_x,nx)
    return max_x

# 아래로 이동 (골렘 출구 방향 d 변화)
def down(x,y,d,id):
    global ans
    if canMove(x+1,y):
        down(x+1,y,d,id)

    # 서쪽으로 회전 및 이동
    elif canMove(x+1,y-1):
        down(x+1,y-1,(d+3) % 4, id)
    # 동쪽으로 회전 및 이동
    elif canMove(x+1,y+1):
        down(x+1,y+1, (d+1) % 4, id)
    else:

        if not in_range(x-1,y-1) or not in_range(x+1,y+1):
            resetMat()
        else:
            mat[x][y] = id
            for i in range(4):
                mat[x+dx[i]][y+dy[i]] = id

            isExit[x+dx[d]][y+dy[d]] = 1

            ans += bfs(x,y) - 2







ans = 0
for id in range(1,k+1):
    ci, d = map(int,input().split())
    down(0,ci-1,d,id)
print(ans)