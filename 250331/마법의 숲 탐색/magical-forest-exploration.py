from collections import deque

MAX_L = 70


R, C, K = map(int, input().split())
answer = 0

mat = [[0 for _ in range(MAX_L)] for _ in range(MAX_L+3)]
isExit = [[0 for _ in range(MAX_L)] for _ in range(MAX_L+3)]

# 북, 동, 남, 서
dx = [-1,0,1,0]
dy = [0,1,0,-1]


# x-1,y
# x,y
def canMove(x,y):
    flag = x+1 < R+3 and 0<=y-1 and y+1<C
    flag = flag and mat[x-1][y-1] == 0
    flag = flag and mat[x-2][y] == 0
    flag = flag and mat[x][y-1] == 0
    flag = flag and mat[x][y] == 0
    flag = flag and mat[x+1][y] == 0
    flag = flag and mat[x][y+1] == 0
    flag = flag and mat[x-1][y+1] == 0
    flag = flag and mat[x-1][y] == 0
    return flag

def resetMap():
    for i in range(R+3):
        for j in range(C):
            mat[i][j] = 0
            isExit[i][j] = 0


def in_range(x,y):
    return 3<=x<R+3 and 0<=y<C


def down(x,y,d,id):
    while 1:
        if canMove(x+1,y):
            x += 1
        elif canMove(x+1,y-1):
            x += 1
            y -= 1
            d = (d+3) % 4
        elif canMove(x+1,y+1):
            x += 1
            y += 1
            d = (d+1) % 4

        else:
            if not (in_range(x-1, y-1) and in_range(x+1,y+1)):
                resetMap()
            else:
                mat[x][y] = id
                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]
                    mat[nx][ny] = id

                ex = x + dx[d]
                ey = y + dy[d]
                isExit[ex][ey] = 1
                global answer

                answer += bfs(x,y) - 3 + 1
            break


def bfs(x,y):
    result = x
    q = deque()
    q.append((x,y))
    visited = [[0 for _ in range(C)] for _ in range(R+3)]
    visited[x][y] = 1
    while q:
        x,y = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if in_range(nx,ny) and visited[nx][ny] == 0 and (mat[nx][ny] == mat[x][y]) or (mat[nx][ny] != 0 and isExit[x][y] == 1):
                q.append((nx,ny))
                visited[nx][ny] = 1
                result = max(result,nx)

    return result

for id in range(1,K+1):
    c,d = map(int,input().split())
    c = c - 1

    down(1,c,d,id)

print(answer)