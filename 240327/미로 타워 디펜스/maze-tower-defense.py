from collections import deque

N, M = map(int, input().split())

mat = []  # 구슬 정보
for _ in range(N):
    mat.append(list(map(int, input().split())))

flag = False
for i in range(N):
    for j in range(N):
        if mat[i][j] > 0:
            flag = True

if flag == False:
    print(0)
    exit()


info = []  # 방향,거리 정보
for _ in range(M):
    d, s = map(int, input().split())
    info.append([d, s])

numbers = []
now_x, now_y = N // 2, N // 2  # 넘버링을 하기 위한 변수 (이동하면서 모든 칸에 번호 부여)
numbers.append((now_x,now_y))

def numbering(cnt, dx, dy):
    global now_x, now_y, numbers
    for i in range(cnt + 1):
        now_x = now_x + dx
        now_y = now_y + dy
        if now_x < 0 or now_y < 0:
            return

        numbers.append((now_x,now_y))

# 넘버링
for i in range(N):
    if i % 2 == 0:
        numbering(i, 0, -1)  # 왼쪽으로
        numbering(i, 1, 0)  # 아래로
    elif i % 2 == 1:
        numbering(i, 0, 1)  # 오른쪽으로
        numbering(i, -1, 0)  # 위로


# 방향
dx = [0,1,0,-1]
dy = [1,0,-1,0]


shark_x, shark_y = N // 2, N // 2  # 마법사 상어 위치
answer = 0

def destroy(d, s):  # 구슬을 파괴하는 함수
    global mat,answer
    for i in range(1, s + 1):  # 거리가 s 이하인 위치의 구슬 모두 파괴
        des_x = shark_x + (i * dx[d])
        des_y = shark_y + (i * dy[d])
        if 0 <= des_x < N and 0 <= des_y < N:
            answer += mat[des_x][des_y]
            mat[des_x][des_y] = 0  # 구슬 파괴
            

def find_number_by_num(n):
    for i in range(N):
        for j in range(N):
            if n == numbers[i][j]:
                return (i, j)

def check_explode():

    cnt = 1
    arr = [] # 4개 이상 연속하는 구슬의 위치를 담아놓을 리스트

    start_x,start_y= numbers[1]
    temp = mat[start_x][start_y]
    temp_arr = [(start_x,start_y)]
    for x,y in numbers[2:]:
        if temp != mat[x][y]:
            cnt = 1
            temp_arr = [(x,y)]
        elif temp == mat[x][y] and temp !=0 :
            cnt += 1
            temp_arr.append((x,y))
        if cnt >= 4:
            arr.extend(temp_arr)
            temp_arr = []
        temp = mat[x][y]

    if arr:
        return arr
    else:
        return False

def move(mat):  # 이동하는 함수
    move_pos = deque()
    for x,y in numbers:
        if x == N//2 and y == N//2:
            continue
        if mat[x][y] == 0:
            move_pos.append((x, y))
        elif mat[x][y] > 0 and move_pos:
            mx, my = move_pos.popleft()
            mat[mx][my], mat[x][y] = mat[x][y], 0
            move_pos.append((x, y))


def grouping(mat):  # 그룹핑 하는 함수
    temp = [[0 for _ in range(N)] for _ in range(N)]
    count = 0
    num = - 1
    nums = []

    for x, y in numbers:
        if x == N // 2 and y == N // 2:
            continue
        if num == -1:
            num = mat[x][y]
            count = 1
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
        for x, y in numbers:
            if x == N // 2 and y == N // 2:
                continue
            mat[x][y] = nums[idx]
            idx += 1
            if idx >= len(nums):
                break


# 폭발한 구슬 세기
scores = [0,0,0,0]

for m in range(M):  # 블리자드 마법 M번 시전
    d, s = info[m][0], info[m][1]
    destroy(d, s)  # 1. 구슬 파괴

    # 2. 빈 칸을 구슬로 채우기
    move(mat)

    # 3. 4개 이상 연속이면 폭발
    while 1:
        arr = check_explode()
        if arr == False:  # 폭발할 구슬이 없으면 반복문 종료
            break
        for x, y in arr:
            scores[mat[x][y]] += 1
            mat[x][y] = 0
        move(mat)

    # 4. 그룹핑
    grouping(mat)


for i in range(len(scores)):
    answer += i * scores[i]

print(answer)