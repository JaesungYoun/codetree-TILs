from collections import deque
M,T = map(int,input().split())
p_x,p_y = map(int,input().split())

mat = [[deque() for _ in range(4)] for _ in range(4)]
for _ in range(M):
    x,y,d = map(int,input().split())
    mat[x-1][y-1].append(d-1)

p_x -= 1
p_y -= 1


# 팩맨 이동 방향
p_dx = [-1,0,1,0]
p_dy = [0,-1,0,1]
# 몬스터의 이동 방향에 대한 x, y 변화량 (상, 상우, 우, 하우, 하, 하좌, 좌, 상좌 순서)
m_dx = [-1, -1, 0, 1, 1, 1,0,-1]
m_dy = [0,-1,-1,-1,0,1,1,1]

def monster_copy():
    for x in range(4):
        for y in range(4):
            if mat[x][y]:
                for m in range(len(mat[x][y])):
                    temp.append((x,y,mat[x][y][m]))

def monster_move():
    tmp = [[[] for _ in range(4)] for _ in range(4)]

    for x in range(4):
        for y in range(4):
            while mat[x][y]:
                d = mat[x][y].pop()
                for i in range(8):
                    nx = x + m_dx[(d+i) % 8]
                    ny = y + m_dy[(d+i) % 8]

                    if 0 <= nx < 4 and 0<= ny <4 and dead[nx][ny] == 0 and not(nx == p_x and ny == p_y):
                        tmp[nx][ny].append((d+i) % 8)
                        break

                else:
                    tmp[x][y].append(d)
    return tmp





from collections import deque

# 팩맨의 이동 방향에 대한 x, y 변화량 (상, 좌, 하, 우 순서)
p_dx = [-1, 0, 1, 0]
p_dy = [0, -1, 0, 1]

def dfs(cnt,x,y,total,visit):
    global max_eat,eat
    global p_x,p_y

    if cnt == 3:
        if max_eat < total:
            max_eat = total
            p_x = x
            p_y = y
            eat = visit[:]

        return

    for i in range(4):
        nx = x + p_dx[i]
        ny = y + p_dy[i]
        if 0<=nx<4 and 0<=ny<4:
            if (nx,ny) not in visit:
                visit.append((nx,ny))
                dfs(cnt+1,nx,ny,total+len(mat[nx][ny]),visit)
                visit.pop()
            else:
                dfs(cnt+1,nx,ny,total,visit)

dead = [[0 for _ in range(4)] for _ in range(4)]

for _ in range(T):

    eat = []
    visit = []
    max_eat = -1
    temp = [] # 복제한 몬스터 담을 배열
    # 1. 몬스터 복제
    monster_copy()

# 2. 몬스터 이동
    mat = monster_move()
    # 3. 팩맨 이동
    dfs(0, p_x, p_y, 0, visit)
    for x, y in eat:
        if mat[x][y]:
            mat[x][y] = []
            dead[x][y] = 3
    # 4. 몬스터 시체 소멸

    for x in range(4):
        for y in range(4):
            if dead[x][y]:
                dead[x][y] -= 1


    # 5. 몬스터 복제 완성
    for t_x,t_y,t_d in temp:
        mat[t_x][t_y].append(t_d)


result = 0
for x in range(4):
    for y in range(4):
        result += len(mat[x][y])
print(result)