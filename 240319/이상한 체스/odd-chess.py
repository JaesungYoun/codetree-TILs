n,m = map(int,input().split())

dx = [-1,0,1,0]
dy = [0,1,0,-1]
direction = [ # cctv 번호에 따른 회전 방향
        [],
        [[0], [1], [2], [3]], # 1번 CCTV
        [[0, 2], [1, 3]], # 2번 CCTV
        [[0, 1], [1, 2], [2, 3], [3, 0]], # 3번 CCTV
        [[0, 1, 2], [1, 2, 3], [2, 3, 0], [3, 0, 1]], # 4번 CCTV
        [[0, 1, 2, 3]] # 5번 CCTV
    ]


chess = []
for _ in range(n):
    chess.append(list(map(int,input().split())))


def check(x,y,direction,arr):
    for d in direction:
        nx = x
        ny = y
        while 1:
            nx += dx[d]
            ny += dy[d]
            if 0<=nx<n and 0<=ny<m and chess[nx][ny] != 6:
                if arr[nx][ny] == 0:
                    arr[nx][ny] = '#'
            else:
                break


def dfs(depth,arr):
    global ans
    if depth == len(cctv):
        ans = min(ans,count(arr))
        return

    #temp = [i[:] for i in arr]
    x,y,cctv_num = cctv[depth]
    for i in direction[cctv_num]:
        temp = [i[:] for i in arr]
        check(x,y,i,temp)
        dfs(depth+1,temp)


ans = 1e9
def count(arr):
    cnt = 0
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 0:
                cnt += 1

    return cnt

cctv = []
for i in range(n):
    for j in range(m):
        if 1 <= chess[i][j] <= 5:
            cctv.append([i,j,chess[i][j]])

dfs(0,chess)
print(ans)