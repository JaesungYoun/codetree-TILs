from collections import deque, defaultdict

n,m,k = map(int,input().split())


rooms = []
aircons = []
for i in range(n):
    mat = list(map(int,input().split()))
    for j in range(n):
        if mat[j] == 1:
            rooms.append((i,j))
        elif mat[j] >= 2:
            aircons.append((i,j,mat[j]-2))


wall = [[[0 for _ in range(4)] for _ in range(n)] for _ in range(n)]

for _ in range(m):
    x,y,s = map(int,input().split())
    x-=1
    y-=1
    if s == 1:
        wall[x][y-1][2] = 1
        wall[x][y][0] = 1
    else:
        wall[x-1][y][3] = 1
        wall[x][y][1] = 1


# 좌상우하
dx = [0,-1,0,1]
dy = [-1,0,1,0]
coolness = [[0 for _ in range(n)] for _ in range(n)]

def bfs(x,y,d,power):
    temp = [[0 for _ in range(n)] for _ in range(n)]
    direction_dict = defaultdict(list)
    # 방향에 따른
    direction_dict[0] = [(1,-1),(0,-1),(-1,-1)]
    direction_dict[1] = [(-1,-1),(-1,0),(-1,1)]
    direction_dict[2] = [(1,1),(0,1),(-1,1)]
    direction_dict[3] = [(1,-1),(1,0),(1,1)]



    spread_dir_list = direction_dict[d]
    queue = deque()
    queue.append((x,y,power))
    temp[x][y] = power
    coolness[x][y] += power
    while queue:
        x,y,power = queue.popleft()

        for s_dx,s_dy in spread_dir_list:
            nx = x + s_dx
            ny = y + s_dy
            if 0<=nx<n and 0<=ny<n and temp[nx][ny] == 0 and power > 1:
                if d == 0 or d ==2:
                    if s_dx != 0 and s_dy != 0:
                        if s_dx > 0:
                            if (wall[x][y][(d+3)%4] == 0) and wall[nx][ny][(d+2)%4] == 0:
                                queue.append((nx,ny,power-1))
                                temp[nx][ny] = power-1
                                coolness[nx][ny] += power-1
                        else:
                            if wall[x][y][(d+1)%4] == 0 and wall[nx][ny][(d+2)%4] == 0:
                                queue.append((nx, ny, power - 1))
                                temp[nx][ny] = power - 1
                                coolness[nx][ny] += power - 1
                    else:
                        if wall[nx][ny][(d+2)%4] == 0:
                            queue.append((nx,ny,power-1))
                            temp[nx][ny] = power-1
                            coolness[nx][ny] += power-1
                else:
                    if s_dx != 0 and s_dy != 0:
                        if s_dy > 0:
                            if (wall[x][y][(d+3)%4] == 0) and wall[nx][ny][(d+2)%4] == 0:
                                queue.append((nx,ny,power-1))
                                temp[nx][ny] = power-1
                                coolness[nx][ny] += power-1
                        else:
                            if wall[x][y][(d+1)%4] == 0 and wall[nx][ny][(d+2)%4] == 0:
                                queue.append((nx, ny, power - 1))
                                temp[nx][ny] = power - 1
                                coolness[nx][ny] += power - 1
                    else:
                        if wall[nx][ny][(d + 2) % 4] == 0:
                            queue.append((nx, ny, power-1))
                            temp[nx][ny] = power-1
                            coolness[nx][ny] += power-1
def spread(ax,ay,d):

    power = 5
    nx = ax + dx[d]
    ny = ay + dy[d]

    bfs(nx,ny,d,power)


def mixing():
    difference = []
    for x in range(n):
        for y in range(n):
            for d in range(4):
                nx = x + dx[d]
                ny = y + dy[d]
                if not (0<=nx<n and 0<=ny<n) or coolness[x][y] <= coolness[nx][ny]:
                    continue
                if wall[x][y][d] == 1:
                    continue
                diff = (coolness[x][y] - coolness[nx][ny]) // 4
                if diff > 0:
                    difference.append((x,y,-diff))
                    difference.append((nx,ny,diff))
    for i,j,diff in difference:
        coolness[i][j] += diff


def reduce():

    for i in range(n-1):
        coolness[0][i] -= 1
    for i in range(1,n):
        coolness[n-1][i] -= 1

    for i in range(1,n):
        coolness[i][0] -= 1

    for i in range(n-1):
        coolness[i][n-1] -= 1

    for i in range(n):
        for j in range(n):
            coolness[i][j] = max(0, coolness[i][j])

time = 0
while 1:
    flag = True
    time += 1

    if time > 100:
        print(-1)
        break

    # 1. 시원한 공기 이동
    for ax,ay,d in aircons:
        spread(ax,ay,d)

    # 2. 시원한 공기들이 섞임
    mixing()

    # 3. 외벽에 있는 칸에 대해서만 시원함이 1씩 감소
    reduce()
    for rx, ry in rooms:
        if coolness[rx][ry] < k:
            flag = False
            break
    if flag:
        print(time)
        break