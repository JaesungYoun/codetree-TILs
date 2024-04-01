N,K = map(int,input().split())

mill = list(map(int,input().split()))
temp = [0 for _ in range(N)]
def rotate(flours,row_num,col_num):
    for i,(x,y) in enumerate(flours):
        flours[i] = (y, row_num - x + 1)

def roll_up():

    # 말아올려진 후 , 각숫자들의 위치 구함
    flours = [(0,0)] * N

    flours[0] = (1,1)
    flours[1] = (2,1)
    row_num, col_num = 2,1
    s_index = 2

    while s_index + row_num <= N:
        rotate(flours,row_num,col_num)

        for i in range(1, row_num + 1):
            flours[s_index] = (col_num + 1, i)
            s_index += 1

        if row_num == col_num + 1:
            col_num += 1
        else:
            row_num += 1

    # 바닥에 있는 것 위치 잡기
    temp = 1
    while s_index < N:
        flours[s_index] = (row_num, col_num + temp)
        s_index += 1
        temp += 1

    return flours

# 두 위치가 인접한 곳인지를 판단합니다.
def adjacency(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2) == 1


def arrange(flours):
    for i in range(N):
        temp[i] = 0

    extended_flours = [
        (y, -x, i)
        for  i, (x,y) in enumerate(flours)
    ]

    extended_flours.sort()

    for i, (_,_,prev_index) in enumerate(extended_flours):
        temp[i] = mill[prev_index]

    for i in range(N):
        mill[i] = temp[i]


def press(flours):
    for i in range(N):
        temp[i] = mill[i]

    # 모든 곳에서 동시에 일어나게 하기위해 temp 배열 사용
    for i in range(N):
        for j in range(i+1,N):
            (x1,y1) = flours[i]
            (x2,y2) = flours[j]
            if adjacency(x1,y1,x2,y2):
                if mill[i] > mill[j]:
                    temp[i] -= (mill[i] - mill[j]) // 5
                    temp[j] += (mill[i] - mill[j]) // 5
                else:
                    temp[i] += (mill[j] - mill[i]) // 5
                    temp[j] -= (mill[j] - mill[i]) // 5

    # 꾹 눌러준 결과를 원래 배열에담음
    for i in range(N):
        mill[i] = temp[i]

    # 행이 높은 순서대로 펴줌
    arrange(flours)

def fold():
    flours = [(0,0)] * N

    # 한 번 접은 후 위치
    for i in range(N//2):
        flours[i] = (1, N//2 - i)
    for i in range(N//2 , N):
        flours[i] = (2, i - (N // 2) + 1)

    # 두 번 접은 후의 위치
    for i, (x,y) in enumerate(flours):
        if y <= N // 4:
            flours[i] = (3-x, N//4-y+1)
        else:
            flours[i] = (x+2,y-N//4)
    return flours


def end():
    return max(mill) - min(mill) <= K


time = 0
while not end():

    # 1.밀가루 양이 가장 작은 위치에 밀가루 1만큼 더 넣어줍니다.(가장 작은 위치가 여러 개라면 모두 넣기)
    min_val = min(mill)
    for i in range(len(mill)):
        if mill[i] == min_val:
            mill[i] += 1

    # 2. 도우를 말아줍니다.
    flours = roll_up()

    # 3. 도우를 꾹 눌러줍니다.
    press(flours)

    # 4. 도우를 두번 반으로 접음
    flours = fold()

    # 5. 도우를 한 번더 꾹 누름
    press(flours)

    time += 1

print(time)