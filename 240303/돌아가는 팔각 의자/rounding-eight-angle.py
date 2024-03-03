from collections import deque

chairs = []
chairs.append(deque([-1]))

for _ in range(4):
    chairs.append(deque(list(input())))



k = int(input())

rotation = []
for _ in range(k):
    num,d = map(int,input().split())
    rotation.append([num,d])


def rotate(num,d):
    if d == 1:
        chairs[num].appendleft(chairs[num].pop())
    else:
        chairs[num].append(chairs[num].popleft())


for num,d in rotation:

    temp = num
    cnt_left = 0
    cnt_right = 0

    for i in range(temp,1,-1):
        if chairs[i-1][2] != chairs[i][6]:
            cnt_left += 1
        else:
            break

    temp = num
    for i in range(temp,4,1):
        if chairs[i+1][6] != chairs[i][2]:
            cnt_right +=1
        else:
            break

    rotate(num,d)

    left_d = -(d)
    right_d = -(d)

    for i in range(num-1,num-cnt_left-1,-1):
        rotate(i,left_d)
        left_d *= -1
    for i in range(num+1,num+cnt_right+1,1):
        rotate(i,right_d)
        right_d *= -1

result = 0
for index, i in enumerate(chairs[1:]):
    if i[0] == '1':
        if index == 0:
            result += 1
        elif index == 1:
            result += 2
        elif index == 2:
            result += 4
        elif index == 3:
            result += 8

print(result)