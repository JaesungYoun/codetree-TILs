from collections import deque
N,M,K = map(int,input().split())
dx, dy = [-1, -1, 0, 1, 1, 1, 0, -1], [0, 1, 1, 1, 0, -1, -1, -1]

mat = []
for _ in range(N):
    mat.append(list(map(int,input().split())))


land = [[5 for _ in range(N)] for _ in range(N)]



virus = [[deque() for _ in range(N)] for _ in range(N)]
for _ in range(M):
    x,y,age = map(int,input().split())
    virus[x-1][y-1].append(age)


def first(x,y,dead):

    new_virus = deque()
    virus[x][y].sort()
    for i in range(len(virus[x][y])):
        
        age = virus[x][y][i]
        if age <= land[x][y]:
            land[x][y] -= age
            new_virus.append(age+1)
        else:
            dead += (virus[x][y][i] // 2)

    virus[x][y] = new_virus
    land[x][y] += dead



def third(x,y):
    for i in range(len(virus[x][y])):
        if virus[x][y][i] % 5 == 0:
            for d in range(8):
                nx = x + dx[d]
                ny = y + dy[d]

                if 0<=nx<N and 0<=ny<N:
                    virus[nx][ny].appendleft(1)


for _ in range(K):

    for x in range(N):
        for y in range(N):
            if len(virus[x][y]) > 0:
                first(x,y,0)


    for x in range(N):
        for y in range(N):
            if len(virus[x][y]) > 0:
                third(x,y)

    for x in range(N):
        for y in range(N):
            land[x][y] += mat[x][y]

cnt = 0
for x in range(N):
    for y in range(N):
        cnt += len(virus[x][y])

print(cnt)