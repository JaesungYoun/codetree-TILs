N,M = map(int,input().split())

mat = []
for _ in range(N):
    mat.append(list(map(int,input().split())))


house = []
chicken = []
for i in range(N):
    for j in range(N):
        if mat[i][j] == 1:
            house.append((i,j))
        elif mat[i][j] == 2:
            chicken.append((i,j))

min_val = 1e9
temp = []
def dfs(cnt,idx):
    global min_val
    if cnt == M:
        dist = 0
        for i in house:
            tmp_val = 1e9
            for t in temp:
                tmp_val = min(abs(i[0] - t[0]) + abs(i[1]-t[1]),tmp_val)
            dist += tmp_val
        min_val = min(min_val,dist)
        return
            
    for i in range(idx,len(chicken)):
        temp.append(chicken[i])
        dfs(cnt + 1, i + 1)   
        temp.pop()
        

dfs(0,0)
print(min_val)