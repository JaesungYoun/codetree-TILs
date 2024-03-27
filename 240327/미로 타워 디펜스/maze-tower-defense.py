N,M = map(int,input().split())
from collections import deque
mat = []
for _ in range(N):
    mat.append(list(map(int,input().split())))

dx = [0,1,0,-1]
dy = [1,0,-1,0]

flag = False
for i in range(N):
    for j in range(N):
        if mat[i][j] > 0:
            flag = True

if flag == False:
    print(0)
    exit()


attack_info = []
for _ in range(M):
    d,p = map(int,input().split())
    attack_info.append([d,p])



number = [[0 for _ in range(N)] for _ in range(N)]
now_x,now_y = N//2, N//2
num = 1

result = 0
numbers = []

def numbering(cnt,d):
    global now_x, now_y
    for _ in range(cnt+1):
        now_x += dx[d]
        now_y += dy[d]
        if now_x < 0 or now_y < 0:
            return

        numbers.append((now_x,now_y))



for i in range(N):
    if i % 2 == 0:
        numbering(i,2)
        numbering(i,1)
    elif i % 2 == 1:
        numbering(i,0)
        numbering(i,3)


tower_x, tower_y = N//2,N//2

def move(mat):

    move_pos = deque()
    for x,y in numbers:
        if x == N//2 and y == N//2:
            continue
        if mat[x][y] == 0:
            move_pos.append((x,y))

        elif mat[x][y] > 0 and move_pos:
            mx,my = move_pos.popleft()
            mat[mx][my], mat[x][y] = mat[x][y], 0
            move_pos.append((x,y))


def deleteMonsterIf4():

    while 1:
        arr = []  # 4개 이상 연속하는 몬스터 위치 담는 리스트
        start_x, start_y = numbers[0]
        temp = mat[start_x][start_y]
        tmp_arr = [(start_x, start_y)]
        cnt = 1
        for x,y in numbers[1:]:
            if mat[x][y] == temp and temp != 0 :
                tmp_arr.append((x,y))
                cnt += 1
            elif mat[x][y] != temp:
                tmp_arr = [(x,y)]
                cnt = 1
            if cnt >= 4:
                arr.extend(temp_arr)
                temp_arr = []
            temp = mat[x][y]

        if arr:
            return arr
        else:
            break


def grouping(mat):
    temp = [[0 for _ in range(N)] for _ in range(N)]
    count = 0
    num = -1
    nums = []

    for x,y in numbers:
        if x == N//2 and y == N//2:
            continue
        if num == -1:
            num = mat[x][y]
            count += 1
        else:
            if num == mat[x][y]:
                count += 1
            else:
                nums.append(count)
                nums.append(num)
                num = mat[x][y]
                count = 1
    if nums:
        idx = 0
        for x,y in numbers:
            if x == N // 2 and y == N // 2:
                continue
            mat[x][y] = nums[idx]
            idx += 1
            if idx >= len(nums):
                break


scores = [0,0,0,0]

for m in range(M):
    d,p = attack_info[m]


    # 1. 공격

    temp = []
    for i in range(1,p+1):
        nx = tower_x + (i * dx[d])
        ny = tower_y + (i * dy[d])

        if 0<=nx<N and 0<=ny<N:
            result += mat[nx][ny]
            mat[nx][ny] = 0
            temp.append((nx,ny))

    # 2. 비어있는 공간만큼 몬스터는 앞으로 이동하여 빈 공간 채우기
    move(mat)

    # 3. 4번이상 나오는 몬스터 있을 경우 삭제
    isMonster4 = deleteMonsterIf4()

    if isMonster4:
        for x,y in isMonster4:
            scores[mat[x][y]] += 1
            mat[x][y] = 0

        move(mat)

    # 4. 그룹핑

    grouping(mat)

answer = 0
for i in range(len(scores)):
    answer += i * scores[i]
print(answer)