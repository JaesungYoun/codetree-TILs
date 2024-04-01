M,T = map(int,input().split())

px,py = map(int,input().split())
px -= 1
py -= 1

mat = [[[] for _ in range(4)] for _ in range(4)]
for _ in range(M):
    x,y,d = map(int,input().split())
    mat[x-1][y-1].append(d-1)


dx = [-1, -1, 0, 1, 1, 1,0,-1]
dy = [0,-1,-1,-1,0,1,1,1]
p_dx = [-1,0,1,0]
p_dy = [0,-1,0,1]

def monster_copy():
    for i in range(4):
        for j in range(4):
            if mat[i][j]:
                for m in range(len(mat[i][j])):
                    temp.append((i,j,mat[i][j][m]))
def monster_move():

    tmp = [[[] for _ in range(4)] for _ in range(4)]
    for x in range(4):
        for y in range(4):
            while mat[x][y]:
                d = mat[x][y].pop()

                for i in range(8):
                    nx = x + dx[(d+i) % 8]
                    ny = y + dy[(d+i) % 8]

                    if 0<= nx < 4 and 0<= ny < 4 and not(px==nx and py==ny) and dead[nx][ny] == 0:
                        tmp[nx][ny].append((d+i) % 8)
                        break
                else:
                    tmp[x][y].append(d)
    return tmp

def packman_move(cnt,x,y,total,visit):
    global max_eat,px,py,eat

    if cnt == 3:
        if max_eat < total:
            max_eat = total
            px = x
            py = y
            eat = visit[:]
        return

    for i in range(4):
        nx = x + p_dx[i]
        ny = y + p_dy[i]
        if 0 <= nx < 4 and 0 <= ny < 4 :
            if (nx,ny) not in visit:
                visit.append((nx,ny))
                packman_move(cnt+1,nx,ny,total+len(mat[nx][ny]),visit)
                visit.pop()
            else:
                packman_move(cnt+1,nx,ny,total,visit)



# 시체 관리 배열
dead = [[0 for _ in range(4)] for _ in range(4)]

for _ in range(T):

    temp = []
    #1. 몬스터 복제
    monster_copy()

    #2. 몬스터 이동
    mat = monster_move()

    #3. 팩맨 이동
    visit = []
    max_eat = -1
    eat = []
    packman_move(0,px,py,0,visit)
    for x,y in eat:

        mat[x][y] = []
        dead[x][y] = 3
    #4. 시체 소멸
    for x in range(4):
        for y in range(4):
            if dead[x][y]:
                dead[x][y] -= 1

    #.5 몬스터 복제 완성

    for tx,ty,td in temp:
        mat[tx][ty].append(td)

result = 0
for i in range(4):
    for j in range(4):
        result += len(mat[i][j])
print(result)