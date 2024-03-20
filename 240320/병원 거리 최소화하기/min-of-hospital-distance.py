n,m = map(int,input().split())

people = []
hospital = []
mat = []
for _ in range(n):
    mat.append(list(map(int,input().split())))


for i in range(n):
    for j in range(n):
        if mat[i][j] == 1: # 사람인 경우
            people.append((i,j))
        if mat[i][j] == 2:
            hospital.append((i,j))

min_dist = 1e9
arr = []
def dfs(depth,idx):
    global min_dist
    if depth == m:
        dist = 0
        for px,py in people:
            temp = 1e9
            for hx,hy in arr:
                temp = min(abs(px - hx) + abs(py-hy),temp)
            dist += temp
        min_dist = min(min_dist,dist)
        return

    for i in range(idx,len(hospital)):
        arr.append(hospital[i])
        dfs(depth+1,idx)
        arr.pop()
dfs(0,0)
print(min_dist)