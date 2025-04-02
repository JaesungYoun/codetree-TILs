from collections import deque
N,M,K = map(int,input().split())

room = [] # 사무실
aircon = [[] for _ in range(4)] # 에어컨
result = [[0 for _ in range(N)] for _ in range(N)]
for i in range(N):
    mat = list(map(int,input().split()))
    for j in range(N):
        if mat[j] == 1:
            room.append((i,j))
        elif mat[j] >= 2:
            aircon[mat[j] - 2].append((i,j))


# 상하좌우
wall = [[[0 for _ in range(4)] for _ in range(N)] for _ in range(N)]
for _ in range(M):
    x,y,s = map(int,input().split())
    x -= 1
    y -= 1

    if s == 1:
        wall[x][y-1][3] = 1 # 왼쪽칸의 오른쪽 벽
        wall[x][y][2] = 1 # 현재 칸의 왼쪽벽
    else:
        wall[x-1][y][1] = 1 # 위쪽칸의 아래벽
        wall[x][y][0] = 1 # 현재칸의 위쪽벽


cool = [[0 for _ in range(N)] for _ in range(N)]

def in_range(x,y):
    if 0<= x < N and 0 <= y < N:
        return True
    return False

def cooling(x,y,d):
    temp = [[0 for _ in range(N)] for _ in range(N)]

    start = 5 # 초기값 5


    if d == 0: # 에어컨 방향이 왼쪽
        queue = deque()
        
        temp[x][y-1] = start
        queue.append((x,y-1,start))
        while queue:
            x,y,cool = queue.popleft()

            if in_range(x,y-1) and wall[x][y-1][3] == 0:
                temp[x][y-1] = cool - 1
                if cool -1 > 1:
                    queue.append((x,y-1,cool-1))
            if in_range(x-1,y) and in_range(x-1,y-1) and wall[x-1][y][1] == 0 and wall[x-1][y-1][3] == 0:
                temp[x-1][y-1] = cool - 1
                if cool - 1 > 1:
                    queue.append((x-1,y-1,cool-1))
            if in_range(x+1,y) and in_range(x+1,y-1) and wall[x+1][y][0] == 0 and wall[x+1][y-1][3] == 0:
                temp[x+1][y-1] = cool - 1
                if cool - 1 > 1:
                    queue.append((x+1,y-1,cool-1))

        for i in range(N):
            for j in range(N):
                result[i][j] += temp[i][j]


    elif d == 1: # 북쪽 방향
        queue = deque()
        
        temp[x-1][y] = start
        queue.append((x-1,y,start))

        while queue:
            x,y,cool = queue.popleft()

            if in_range(x-1,y) and wall[x-1][y][1] == 0:
                temp[x-1][y] = cool - 1
                if cool - 1 > 1:
                    queue.append((x-1,y,cool-1))
            if in_range(x,y-1) and in_range(x-1,y-1) and wall[x][y-1][3] == 0 and wall[x-1][y-1][1] == 0:
                temp[x-1][y-1] = cool -1
                if cool - 1 > 1:
                    queue.append((x-1,y-1,cool-1))
            if in_range(x,y+1) and in_range(x-1,y+1) and wall[x][y+1][2] == 0 and wall[x-1][y+1][1] == 0:
                temp[x-1][y+1] = cool -1
                if cool - 1 > 1:
                    queue.append((x-1,y+1,cool-1))
        for i in range(N):
            for j in range(N):
                result[i][j] += temp[i][j]

    elif d == 2: # 에어컨 방향이 오른쪽
        queue = deque()
        
        temp[x][y+1] = start
        queue.append((x,y+1,start))
        while queue:
            x,y,cool = queue.popleft()
            if in_range(x,y+1) and wall[x][y+1][2] == 0:
                temp[x][y+1] = cool - 1
                if cool - 1 > 1:
                    queue.append((x,y+1,cool-1))
            if in_range(x-1,y) and in_range(x-1,y+1) and wall[x-1][y][1] == 0 and wall[x-1][y+1][2] == 0:
                temp[x-1][y+1] = cool - 1
                if cool - 1 > 1:
                    queue.append((x-1,y+1,cool-1))
            if in_range(x+1,y) and in_range(x+1,y+1) and wall[x+1][y][0] == 0 and wall[x+1][y+1][2] == 0:
                temp[x+1][y+1] = cool -1
                if cool - 1 > 1:
                    queue.append((x+1,y+1,cool-1))
        for i in range(N):
            for j in range(N):
                result[i][j] += temp[i][j]

    else: # 에어컨 방향이 남쪽
        queue = deque()
        
        temp[x+1][y] = start
        queue.append((x+1,y,start))

        while queue:
            x,y,cool = queue.popleft()

            if in_range(x+1,y) and wall[x+1][y][0] == 0:
                temp[x+1][y] = cool - 1
                if cool - 1 > 1:
                    queue.append((x+1,y,cool-1))
            if in_range(x,y-1) and in_range(x+1,y-1) and wall[x][y-1][3] == 0 and wall[x+1][y-1][0] == 0:
                temp[x+1][y-1] = cool - 1
                if cool - 1 > 1:
                    queue.append((x+1,y-1,cool-1))
            if in_range(x,y+1) and in_range(x+1,y+1) and wall[x][y+1][2] == 0 and wall[x+1][y+1][0] == 0:
                temp[x+1][y+1] = cool - 1
                if cool - 1 > 1:
                    queue.append((x+1,y+1,cool-1))

        for i in range(N):
            for j in range(N):
                result[i][j] += temp[i][j]


dx = [-1,1,0,0]
dy = [0,0,-1,1]
def mixing():
    difference = []
    for x in range(N):
        for y in range(N):
            for d in range(4):
                nx = x + dx[d]
                ny = y + dy[d]
                if not in_range(nx,ny) or result[x][y] <= result[nx][ny]:
                    continue
                if wall[x][y][d] == 1:
                    continue
                diff = (result[x][y] - result[nx][ny]) // 4
                if diff > 0:
                    difference.append((x,y,-diff))
                    difference.append((nx,ny,diff))
    for i,j,diff in difference:
        result[i][j] += diff



def reduce():

    for i in range(N-1):
        result[0][i] -= 1
    for i in range(1,N):
        result[N-1][i] -= 1

    for i in range(1,N):
        result[i][0] -= 1

    for i in range(N-1):
        result[i][N-1] -= 1

    for i in range(N):
        for j in range(N):
            result[i][j] = max(0, result[i][j])

time = 0

while 1:
    flag = True
    time += 1
    if time > 100:
        print(-1)
        exit(0)

    # 1. 시원한 공기 이동
    for i in range(4):
        if aircon[i]:
            for ax, ay in aircon[i]:
                cooling(ax,ay,i)

    # 2. 시원한 공기들이 섞임
    mixing()

    # 3. 외벽에 있는 칸에 대해서만 시원함이 1씩 감소
    reduce()
    for rx, ry in room:
        if result[rx][ry] < K:
            flag = False
            break
    if flag:
        print(time)
        break

