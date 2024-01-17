n = int(input())

dp = [0]

answer = 0
task = []
for _ in range(n):
    t,p = map(int,input().split())
    task.append([t,p])



def dfs(day,income):
    global answer

    if day > n:
        return
    elif day == n:
        answer = max(answer,income)
        return

    # 아래 2가지에 대해 모두 dfs해서 가장 큰 수익을 찾아야한다.
    dfs(day+1,income) # 해당 날짜에 일을 시작 안했을 때
    dfs(day+task[day][0],income + task[day][1]) # 해당 날짜에 일을 시작했을 때

dfs(0,0)
print(answer)