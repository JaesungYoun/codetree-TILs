from collections import deque

R, C, K = map(int, input().split())
gol = [list(map(int, input().split()))+[i+1] for i in range(K)]
maps = [[0] * C for _ in range(R)]
dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1] # 북동남서

def check(x, y, num):
    if num == 1:
        dx1, dy1 = [1,2,1], [-1,0,1]
        for d in range(3):
            nx, ny = x+dx1[d], y+dy1[d]
            if nx < 0:
                continue
            if not(0<=nx<R and 0<=ny<C) or maps[nx][ny] != 0:
                return False
    elif num == 2:
        dx1, dy1 = [-1,0,1,1,2], [-1,-2,-1,-2,-1]
        for d in range(5):
            nx, ny = x + dx1[d], y + dy1[d]
            if nx < 0:
                continue
            if not(0 <= nx < R and 0 <= ny < C) or maps[nx][ny] != 0:
                return False
    else:
        dx1, dy1 = [-1,0,1,1,2], [1,2,1,2,1]
        for d in range(5):
            nx, ny = x + dx1[d], y + dy1[d]
            if nx <0: continue
            if not(0 <= nx < R and 0 <= ny < C) or maps[nx][ny] != 0:
                return False
    return True

def move(x, y, n):
    far = 0
    q = deque()
    q.append((x, y, n))
    visited = [[False]*C for _ in range(R)]
    while q:
        cx, cy, cn = q.popleft()
        visited[cx][cy] = True
        far = max(far, cx+1)
        if far == R:
            break
        if maps[cx][cy] < 0: # 출구라면
            for d in range(4):
                nx, ny = cx + dx[d], cy + dy[d]
                if 0 <= nx < R and 0 <= ny < C and not visited[nx][ny] and maps[nx][ny] != 0:
                    q.append((nx, ny, maps[nx][ny]))
        else:
            for d in range(4):
                nx, ny = cx+dx[d], cy+dy[d]
                if 0<=nx<R and 0<=ny<C and not visited[nx][ny] and maps[nx][ny] in [cn, -cn]:
                    q.append((nx, ny, maps[nx][ny]))
    return far

# main
res = 0
for gy, gd, gn in gol:
    gx, gy = -2, gy-1
    # 1. 최대한 아래로 이동
    while True:
        if check(gx, gy, 1): # 바로 아래가
            gx += 1
        elif check(gx, gy, 2): # 왼쪽이 비어있다면, 출구 반시계 이동
            gy -= 1
            gx += 1
            gd = gd-1 if gd-1 >= 0 else gd-1+4
        elif check(gx, gy, 3): # 오른쪽이 비어있다면, 출구 시계 이동
            gy += 1
            gx += 1
            gd = gd+1 if gd+1 < 4 else gd+1-4
        else:
            break
    # +) 혹시 삐져나왔나 체크
    if gx < 1:
        maps = [[0] * C for _ in range(R)]
        continue
    # 2. 도착했으면 맵에 표시
    maps[gx][gy] = gn
    for d in range(4):
        nx, ny = gx+dx[d], gy+dy[d]
        maps[nx][ny] = gn
    maps[gx+dx[gd]][gy+dy[gd]] = -gn

    # 3. 정령 이동
    res += move(gx, gy, gn)

print(res)
