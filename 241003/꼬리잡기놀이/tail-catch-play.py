n, m, k = map(int, input().split())

mat = [[0 for _ in range(n+1)]]
for _ in range(n):
    mat.append([0] + list(map(int, input().split())))

# 공 방향 순차대로
ball_dx = [0, -1, 0, 1]
ball_dy = [1, 0, -1, 0]

ball_d = 0


# 각 팀별 레일 위치
v = [[] for _ in range(m+1)]
# 각 팀별 꼬리 위치
tail = [0 for _ in range(m+1)]
visited = [[0 for _ in range(n+1)] for _ in range(n+1)]

team_num = [[0 for _ in range(n+1)] for _ in range(n+1)]


def in_range(x,y):
    return 1<=x<n and 1<=y<n


dx = [-1,1,0,0]
dy = [0,0,-1,1]
def dfs(x,y,num):
    visited[x][y] = 1
    team_num[x][y] = num
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if not in_range(nx,ny):
            continue

        if mat[nx][ny] == 0:
            continue
        if visited[nx][ny] == 1:
            continue

        if len(v[num]) == 1 and mat[nx][ny] != 2:
            continue

        v[num].append((nx,ny))
        if mat[nx][ny] == 3:
            tail[num] = len(v[num])
        dfs(nx,ny,num)


def init():
    team_number = 1
    for i in range(1,n+1):
        for j in range(1,n+1):
            if mat[i][j] == 1:
                v[team_number].append((i,j))
                team_number += 1

    for i in range(1,m+1):
        x,y = v[i][0]
        dfs(x,y,i)

def move_all():
    for i in range(1,m+1):
        temp = v[i][-1]
        for j in range(len(v[i])-1, 0, -1):
            v[i][j] = v[i][j-1]
        v[i][0] = temp

    for i in range(1,m+1):
        for j, (x,y) in enumerate(v[i]):
            if j == 0:
                mat[x][y] = 1
            elif j < tail[i] - 1:
                mat[x][y] = 2
            elif j == tail[i] - 1:
                mat[x][y] = 3
            else:
                mat[x][y] = 4
ans = 0

def get_point(x,y):
    global ans
    num = team_num[x][y]
    k = v[num].index((x,y))
    ans += ((k+1)**2)


def throw_ball(turn):
    t = (turn -1) % (4*n) + 1

    if t <= n:
        for i in range(1,n+1):
            if 1<= mat[t][i] and mat[t][i] <= 3:
                get_point(t,i)
                return team_num[t][i]
    elif t <= 2* n:
        t -= n
        for i in range(1,n+1):
            if 1 <= mat[n+1-i][t] <= 3:
                get_point(n+1-i,t)
                return team_num[n+1-i][t]
    elif t <= 3* n:
        t -= (2 * n)
        for i in range(1,n+1):
            if 1 <= mat[n+1-t][n+1-i] <= 3:
                get_point(n+1-t,n+1-i)
                return team_num[n+1+t][n+1-i]
    else:
        t -= (3*n)
        for i in range(1,n+1):
            if 1<= mat[i][n+1-t] <= 3:
                get_point(i,n+1-t)
                return team_num[i][n+1-t]

    return 0

def reverse(got_ball_idx):
    if got_ball_idx == 0:
        return

    idx = got_ball_idx

    new_v = []

    for j in range(tail[idx] -1,-1,-1):
        new_v.append(v[idx][j])

    for j in range(len(v[idx]) -1, tail[idx]-1,-1):
        new_v.append(v[idx][j])

    v[idx] = new_v[:]

    for j, (x, y) in enumerate(v[idx]):
        if j == 0:
            mat[x][y] = 1
        elif j < tail[idx] - 1:
            mat[x][y] = 2
        elif j == tail[idx] -1 :
            mat[x][y] = 3
        else:
            mat[x][y] = 4

init()

for i in range(1,k+1):
    move_all()

    got_ball_idx = throw_ball(i)

    reverse(got_ball_idx)


print(ans)