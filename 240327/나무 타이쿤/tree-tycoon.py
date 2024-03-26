N,M = map(int,input().split())

mat = []
for _ in range(N):
    mat.append(list(map(int,input().split())))


move_list = []
for _ in range(M):
    d,p = map(int,input().split())
    move_list.append([d-1,p])


move_x = [N-1,N-1,N-2,N-2]
move_y = [0,1,0,1]

# 대각선
ddx = [-1,1,1,-1]
ddy = [1,-1,1,-1]

# 모든 방향
dx = [0,-1,-1,-1,0,1,1,1]
dy = [1,1,0,-1,-1,-1,0,1]

def move(move_x,move_y,d,p):

    for i in range(len(move_x)):
        move_x[i] = (move_x[i] + p * dx[d]) % N
        move_y[i] = (move_y[i] + p * dy[d]) % N


for t in range(M):
    d,p = move_list[t]
    # 1. 특수 영양제 이동
    move(move_x,move_y,d,p)

    # 2. 특수 영양제 투입
    for i in range(len(move_x)):
        x,y = move_x[i],move_y[i]
        mat[x][y] += 1

    # 3. 대각선에 있는 높이 1 이상의 리브로수의 개수만큼 높이 증가
    temp = []
    cnt_all = []
    for i in range(len(move_x)):
        x,y = move_x[i],move_y[i]
        cnt = 0

        for j in range(4):
            nx = x + ddx[j]
            ny = y + ddy[j]

            if 0<=nx<N and 0<=ny<N and mat[nx][ny] > 0:
                cnt += 1
        temp.append((x,y))
        cnt_all.append(cnt)

    for c in range(len(cnt_all)):
        mat[move_x[c]][move_y[c]] += cnt_all[c]

    # 4. 영양제 투입 리브로수를 제외하고 높이가 2 이상인 리브로수를 높이 2를 베어냄

    move_x = []
    move_y = []

    for x in range(N):
        for y in range(N):
            if (x,y) not in temp and mat[x][y] >= 2:
                mat[x][y] -= 2
                move_x.append(x)
                move_y.append(y)

result = 0
for i in range(N):
    for j in range(N):
        if mat[i][j] > 0 :
            result += mat[i][j]

print(result)