from collections import deque
N,L,R = map(int,input().split())


mat = []
for _ in range(N):
    mat.append(list(map(int,input().split())))


dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y):
    q = deque()
    q.append((x,y))
    temp = []
    temp.append((x,y))
    visited[x][y] = 1
    _sum = mat[x][y]
    while q:
        x,y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<N and 0<=ny<N and visited[nx][ny] == 0 and L<=abs(mat[x][y] - mat[nx][ny]) <=R:
                q.append((nx,ny))
                visited[nx][ny] = 1
                temp.append((nx,ny))
                _sum += mat[nx][ny]

    if len(temp) != 1:
        groups.append(temp)







flag = False
cnt = 0
while 1:
    groups = []
    visited = [[0 for _ in range(N)] for _ in range(N)]
    for x in range(N):
        for y in range(N):
            if visited[x][y] == 0:
                bfs(x,y)

    if not groups:
        break
    cnt += 1
    for i in range(len(groups)):
        _sum = 0
        for j in groups[i]:
            _sum += mat[j[0]][j[1]]

        for j in groups[i]:
            mat[j[0]][j[1]] = _sum//len(groups[i])



print(cnt)