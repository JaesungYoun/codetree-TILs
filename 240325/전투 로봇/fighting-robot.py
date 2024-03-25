from collections import deque
N = int(input())

mat = []
for _ in range(N):
    mat.append(list(map(int,input().split())))


dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y,level):
    q = deque()
    q.append((x,y))
    visited[x][y] = 1
    candi = []
    while q:
        x,y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<N and 0<=ny<N and mat[nx][ny] <= level and visited[nx][ny] == 0:
                q.append((nx,ny))
                visited[nx][ny] = visited[x][y] + 1
                if 0 <  mat[nx][ny] < level:
                    candi.append((nx, ny,visited[nx][ny] - 1))

    candi = sorted(candi, key = lambda x : (x[2],x[0],x[1]))

    if candi:
        return candi[0]
    else:
        return False



r_x,r_y = -1,-1 # 로봇 위치
for x in range(N):
    for y in range(N):
        if mat[x][y] == 9:
            r_x,r_y = x,y
            break

level = 2
mat[r_x][r_y] = 0
cnt = 0
time = 0
while 1:
    visited = [[0 for _ in range(N)] for _ in range(N)]

    candi = bfs(r_x,r_y,level)
    if not candi:
        break

    m_x,m_y,dist = candi
    time += dist
    mat[m_x][m_y] = 0
    r_x,r_y = m_x,m_y

    cnt += 1
    if cnt == level:
        cnt = 0
        level += 1
print(time)