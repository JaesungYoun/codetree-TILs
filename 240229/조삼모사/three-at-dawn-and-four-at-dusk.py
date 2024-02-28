n = int(input())

mat = []
for _ in range(n):
    mat.append(list(map(int,input().split())))


visited = [0 for _ in range(n)]

def dfs(cnt,idx):
    global answer
    if cnt == n//2:
        morning = 0
        night = 0


        for i in range(n):
            if visited[i]:
                for j in range(i+1,n):
                    if visited[j]:
                        morning += mat[i][j]
                        morning += mat[j][i]
            if not visited[i]:
                for j in range(i+1,n):
                    if not visited[j]:
                        night += mat[i][j]
                        night += mat[j][i]

        answer = min(answer,abs(morning - night))
        if answer == 0:
            return

        return


    for i in range(idx,n):
        if visited[i]:
            continue
        visited[i] = 1
        dfs(cnt+1,i+1)
        visited[i] = 0

answer = 1e9
dfs(0,0)
print(answer)