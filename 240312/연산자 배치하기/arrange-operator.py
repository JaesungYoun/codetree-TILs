n = int(input())

nums = list(map(int,input().split()))
oper = (list(map(int,input().split())))

def dfs(idx,total,add,sub,mul):
    global min_val, max_val

    if idx == n:
        min_val = min(total,min_val)
        max_val = max(total,max_val)
        return

    if add > 0 :
        dfs(idx+1,total+nums[idx], add -1, sub, mul)
    if sub > 0 :
        dfs(idx+1,total-nums[idx], add, sub-1, mul)
    if mul > 0 :
        dfs(idx + 1, total * nums[idx], add, sub, mul-1)



min_val = 1e9
max_val = -1e9
dfs(1,nums[0],oper[0],oper[1],oper[2])
print(min_val,max_val)