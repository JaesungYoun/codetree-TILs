n,m,h = map(int,input().split())


mat = [[0 for _ in range(n)] for _ in range(h)]
for _ in range(m):
    a,b = map(int,input().split())
    mat[a-1][b-1] = 1


if m == 0:
    print(0)
    exit(0)

def check():
    for i in range(n): # 한 명씩 이동
        now = i # 현재 사다리 열 위치
        for j in range(h): # 사다리행
            if mat[j][now] == 1:
                now += 1
            elif now > 0 and mat[j][now-1] == 1:
                now -= 1
        if i != now:
            return False
    return True

def dfs(cnt,x,y):
    global ans
    if check():
        ans = min(ans,cnt)
        return
    if cnt == 3:
        return


    for i in range(x,h):
        if i == x:
            now = y
        else:
            now = 0
        for j in range(now,n-1):
            if mat[i][j] == 0 and mat[i][j+1] == 0 and mat[i][j-1] == 0:
                mat[i][j] = 1
                dfs(cnt+1,i,j+2)
                mat[i][j] = 0

ans = 4
dfs(0,0,0)
if ans < 4:
    print(ans)
else:
    print(-1)