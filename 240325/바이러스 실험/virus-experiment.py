import heapq

N,M,K = map(int,input().split())
dx, dy = [-1, -1, 0, 1, 1, 1, 0, -1], [0, 1, 1, 1, 0, -1, -1, -1]

mat = []
for _ in range(N):
    mat.append(list(map(int,input().split())))


land = [[5 for _ in range(N)] for _ in range(N)]



virus = [[[] for _ in range(N)] for _ in range(N)]
for _ in range(M):
    x,y,age = map(int,input().split())
    heapq.heappush(virus[x-1][y-1],age)


def first(x,y,dead):

    new_virus = []
    for i in range(len(virus[x][y])):
        age = virus[x][y][i]
        if age <= land[x][y]:
            land[x][y] -= age
            new_virus.append(age+1)
        else:
            dead += (virus[x][y][i] // 2)

    virus[x][y] = new_virus
    heapq.heapify(virus[x][y])
    return dead


def second(x,y,dead,soil):
    soil += dead
    return soil


def third(x,y):
    for i in range(len(virus[x][y])):
        if virus[x][y][i] % 5 == 0:
            for d in range(8):
                nx = x + dx[d]
                ny = y + dy[d]

                if 0<=nx<N and 0<=ny<N:
                    heapq.heappush(virus[nx][ny],1)


for _ in range(K):

    for x in range(len(virus)):
        for y in range(len(virus[x])):
            if virus[x][y]:
                dead = first(x,y,0)

                land[x][y] = second(x,y,dead,land[x][y])

    for x in range(len(virus)):
        for y in range(len(virus[x])):
            if virus[x][y]:
                third(x,y)

    for x in range(len(land)):
        for y in range(len(land[x])):
            land[x][y] += mat[x][y]

cnt = 0
for x in range(len(virus)):
    for y in range(len(virus[x])):
        cnt += len(virus[x][y])

print(cnt)