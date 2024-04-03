from collections import deque

N, M, P, C, D = map(int, input().split())

rx, ry = map(int, input().split())
rx -= 1
ry -= 1

mat = [[0 for _ in range(N)] for _ in range(N)]
for _ in range(P):
    santa_num, x, y = map(int, input().split())
    mat[x - 1][y - 1] = santa_num

mat[rx][ry] = -1  # 루돌프
drx = [1,1,1,0,0,-1,-1,-1]
dry = [1,0,-1,1,-1,1,0,-1]
dsx = [-1, 0, 1, 0]
dsy = [0, 1, 0, -1]


def rudolph_move():
    global rx, ry


    candidate = []
    d = -1
    dist = 1e9
    temp_x, temp_y = rx, ry
    for sx in range(N-1,-1,-1):
        for sy in range(N-1,-1,-1):
            if mat[sx][sy] > 0:
                for i in range(8):
                    nx = rx + drx[i]
                    ny = ry + dry[i]

                    if 0 <= nx < N and 0 <= ny < N:
                        if dist > (sx - nx) ** 2 + (sy - ny) ** 2:
                            dist = (sx - nx) ** 2 + (sy - ny) ** 2
                            temp_x, temp_y = nx, ny
                            d = i
    if d != -1:
        if mat[temp_x][temp_y] > 0:
            collision(0, mat[temp_x][temp_y], temp_x, temp_y, d)
            mat[rx][ry] = 0
            rx, ry = temp_x, temp_y
            mat[rx][ry] = -1
        else:
            mat[rx][ry] = 0
            rx, ry = temp_x, temp_y
            mat[rx][ry] = -1


def santa_move():
    santa_pos = []


    for num in range(1, P + 1):

        if _end[num] == 1:  # 탈락한 산타 제외
            continue
        for x in range(N):
            for y in range(N):
                if mat[x][y] == num:
                    santa_pos.append((num,x, y))
                    break

    for num, x, y in santa_pos:
        if dead[x][y] != 0 :
            continue
        temp_x, temp_y = x, y
        d = -1  # 가장 가까운방향
        dist = (rx - x) ** 2 + (ry - y) ** 2
        for i in range(4):
            nx = x + dsx[i]
            ny = y + dsy[i]

            if 0 <= nx < N and 0 <= ny < N and mat[nx][ny] <= 0:
                if dist > (rx - nx) ** 2 + (ry - ny) ** 2:
                    d = i
                    dist = (rx - nx) ** 2 + (ry - ny) ** 2
                    temp_x, temp_y = nx, ny

        if d != -1:
            if temp_x == rx and temp_y == ry:
                mat[x][y] = 0
                collision(1, num , temp_x, temp_y, d)
            else:
                mat[x][y] = 0
                mat[temp_x][temp_y] = num

_end = [0] * (P + 1)
score = [0] * (P + 1)

def collision(div, santa_num, cx, cy, d):
    if div == 0:
        score[santa_num] += C

        for _ in range(C):
            sx = cx + drx[d]
            sy = cy + dry[d]
            if not (0 <= sx < N and 0 <= sy < N):
                mat[cx][cy] = 0
                _end[santa_num] = 1  # 탈락
                return
            if mat[sx][sy] > 0:
                interaction(div, sx, sy, d)
            if not (cx == rx and cy == ry):
                mat[cx][cy] = 0
            dead[sx][sy] = 2
            mat[sx][sy] = santa_num
            cx, cy = sx, sy

    else:
        score[santa_num] += D
        for _ in range(D):
            sx = cx + dsx[(d + 2) % 4]
            sy = cy + dsy[(d + 2) % 4]
            if not (0 <= sx < N and 0 <= sy < N):
                mat[cx][cy] = 0
                _end[santa_num] = 1  # 탈락
                return
            if mat[sx][sy] > 0:
                interaction(div, sx, sy, (d + 2) % 4)

            if not (cx == rx and cy == ry):
                mat[cx][cy] = 0
            mat[sx][sy] = santa_num
            dead[sx][sy] = 2
            cx,cy = sx,sy

def interaction(div, sx, sy, d):

    while 1:
        if div == 0:
            nx = sx + drx[d]
            ny = sy + dry[d]
        else:
            nx = sx + dsx[d]
            ny = sy + dsy[d]

        if 0 <= nx < N and 0 <= ny < N:
            if mat[nx][ny] == 0:
                mat[nx][ny] = mat[sx][sy]
                if dead[sx][sy] > 0:
                    dead[nx][ny] = dead[sx][sy]
                    dead[sx][sy]= 0
                break
            else:
                mat[nx][ny] = mat[sx][sy]
                if dead[sx][sy] > 0:
                    dead[nx][ny] = dead[sx][sy]
                    dead[sx][sy] = 0
                sx, sy = nx, ny

        else:
            if dead[sx][sy] > 0:
                dead[sx][sy] = 0
            _end[mat[sx][sy]] = 1
            return

dead = [[0 for _ in range(N)] for _ in range(N)]


def end_game():
    for i in range(1, P + 1):
        if _end[i] == 0:
            return False
    return True

for _ in range(M):

    if end_game():
        break

    rudolph_move()

    santa_move()

    for i in range(N):
        for j in range(N):
            if dead[i][j] > 0:
                dead[i][j] -= 1
    for i in range(1, P + 1):
        if _end[i] == 0:
            score[i] += 1

print(*score[1:])