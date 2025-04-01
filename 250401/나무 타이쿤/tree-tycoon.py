from collections import deque

# 격자 크기, 리브로수를 키우는 총 년 수 m
n, m = map(int,input().split())

# 리브로수 배열
mat = []
for _ in range(n):
    mat.append(list(map(int,input().split())))

# 영양제 위치 배열
supple = [[0 for _ in range(n)] for _ in range(n)]

# 영양제 위치 초기화
supple[n-1][0] = 1
supple[n-2][0] = 1
supple[n-1][1] = 1
supple[n-2][1] = 1


rule = []
for _ in range(m):
    d,p = map(int,input().split())
    rule.append((d,p))

# 특수 영양제 이동 방향
dx = [0,-1,-1,-1,0,1,1,1]
dy = [1,1,0,-1,-1,-1,0,1]


def moveSupple(supple, d, p):

    to_move = []
    for x in range(n):
        for y in range(n):
            if supple[x][y] == 1: # 특수영양제가 있는 칸의 경우
               nx = (x + p * dx[d]) % n
               ny = (y + p * dy[d]) % n
               to_move.append((nx,ny))
               supple[x][y] = 0

    # 이동
    for nx,ny in to_move:
        supple[nx][ny] = 1



def doSupple(mat):
    for x in range(n):
        for y in range(n):
            if supple[x][y] == 1:
                mat[x][y] += 1 # 리브로수 높이 증가 or 높이 1 리브로수 생성

def grow(mat):
    for x in range(n):
        for y in range(n):
            cnt = 0
            if supple[x][y] == 1:
                for d in range(1,8,2):
                    crossX = x + dx[d]
                    crossY = y + dy[d]

                    if 0<=crossX<n and 0<=crossY<n and mat[crossX][crossY] > 0:
                        cnt += 1

                # 대각선에 있는 높이 1 이상의 리브로수 수 만큼 성장
                mat[x][y] += cnt

def buySupple(mat, supple):
    buy = []
    disappear = []
    for x in range(n):
        for y in range(n):
            if supple[x][y] == 0:
                if mat[x][y] >= 2:
                    mat[x][y] -= 2
                    buy.append((x,y))

            else:
                disappear.append((x,y))

    for x,y in disappear:
        supple[x][y] = 0

    for x,y in buy:
        supple[x][y] = 1


for i in range(m):
    d,p = rule[i]
    #1. 특수 영양제 이동
    moveSupple(supple, d-1, p)

    #2. 특수 영양제 투입
    doSupple(mat)

    #3. 대각선으로 인접한 방향에 높이가 1이상인 리브로수가 있는 만큼 높이를 더 성장
    grow(mat)

    #4. 특수 영양제를 투입한 리브로수를 제외하고 높이가 2 인상인 리브로수의 높이 2를 베어서 잘라낸 리브로수로 특수영양제를 사고 올려두기
    buySupple(mat, supple)

answer = 0
for i in range(n):
    for j in range(n):
        answer += mat[i][j]

print(answer)











