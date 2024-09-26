n, m, h, k = map(int, input().split())

trees = [[0 for _ in range(n)] for _ in range(n)]
# 각 칸에 있는 도망자 정보를 관리합니다.
# 도망자의 방향만 저장하면 충분합니다.
hiders = [
    [[] for _ in range(n)]
    for _ in range(n)
]

seeker_next_dir = [[0 for _ in range(n)] for _ in range(n)]
seeker_rev_dir = [[0 for _ in range(n)] for _ in range(n)]
for _ in range(m):
    x, y, d = map(int, input().split())
    hiders[x - 1][y - 1].append(d)

for _ in range(h):
    x, y = map(int, input().split())
    trees[x - 1][y - 1] = 1

seeker_pos = (n // 2, n // 2)


def initialize_seeker_dir():
    dxs, dys = [-1, 0, 1, 0], [0, 1, 0, -1]

    curr_x, curr_y = n // 2, n // 2
    move_dir, move_num = 0, 1

    while curr_x or curr_y:
        for _ in range(move_num):
            seeker_next_dir[curr_x][curr_y] = move_dir
            curr_x, curr_y = curr_x + dxs[move_dir], curr_y + dys[move_dir]

            if move_dir < 2:
                seeker_rev_dir[curr_x][curr_y] = move_dir + 2
            else:
                seeker_rev_dir[curr_x][curr_y] = move_dir - 2

            if not curr_x and not curr_y:
                break

        # 방향 체인지
        move_dir = (move_dir + 1) % 4

        if move_dir == 0 or move_dir == 2:
            move_num += 1

forward_facing = True


def in_range(x, y):
    return 0 <= x < n and 0 <= y < n


def can_move(x1,y1):
    x2,y2 = seeker_pos
    return abs(x1-x2) + abs(y1-y2) <= 3

def hider_move(x,y,move_dir):
    dxh,dyh = [0,0,1,-1], [-1,1,0,0]

    nx = x + dxh[move_dir]
    ny = y + dyh[move_dir]

    if not in_range(nx,ny):
        if move_dir < 2:
            move_dir = 1 - move_dir
        else:
            move_dir = 5 - move_dir

        nx,ny = x + dxh[move_dir], dyh[move_dir]

    if (nx,ny) != seeker_pos:
        next_hiders[nx][ny].append(move_dir)

    else:
        next_hiders[x][y].append(move_dir)

next_hiders = [
    [[] for _ in range(n)]
    for _ in range(n)
]

def hider_move_all():
    for i in range(n):
        for j in range(n):
            next_hiders[i][j] = []

    for i in range(n):
        for j in range(n):
            if can_move(i,j):
                for move_dir in hiders[i][j]:
                    hider_move(i,j, move_dir)

            else:
                for move_dir in hiders[i][j]:
                    next_hiders[i][j].append(move_dir)
    for i in range(n):
        for j in range(n):
            hiders[i][j] = next_hiders[i][j]


def check_facing():
    global forward_facing

    if seeker_pos == (0,0) and forward_facing:
        forward_facing = False

    if seeker_pos == (n//2, n//2) and not forward_facing:
        forward_facing = True

def get_seeker_dir():
    x,y = seeker_pos

    move_dir = 0
    if forward_facing:
        move_dir = seeker_next_dir[x][y]
    else:
        move_dir = seeker_rev_dir[x][y]
    return move_dir


def seeker_move():
    global seeker_pos
    x,y = seeker_pos

    dx,dy = [-1,0,1,0],[0,1,0,-1]

    move_dir = get_seeker_dir()

    # 술래를 한 칸 움직여줍니다.
    seeker_pos = (x + dx[move_dir], y + dy[move_dir])

    # 끝에 도달했다면 방향을 바꿔줘야 합니다.
    check_facing()

ans = 0
def get_score(t):
    global ans

    dx,dy = [-1,0,1,0],[0,1,0,-1]
    x,y = seeker_pos

    d = get_seeker_dir()

    for dist in range(3):
        nx,ny = x + dist * dx[d], y + dist * dy[d]

        if in_range(nx,ny ) and not trees[nx][ny]:
            ans += t * len(hiders[nx][ny])

            hiders[nx][ny] = []


def simulate(t):
    # 도망자가 움직입니다.
    hider_move_all()

    # 술래가 움직입니다.
    seeker_move()

    # 점수를 얻습니다.
    get_score(t)


# 술래잡기 시작 전에
# 구현상의 편의를 위해
# 술래 경로 정보를 미리 계산합니다.
initialize_seeker_dir()

# k번에 걸쳐 술래잡기를 진행합니다.
for t in range(1, k + 1):
    simulate(t)

print(ans)