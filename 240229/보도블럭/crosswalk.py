n,L = map(int,input().split())

mat = []

for _ in range(n):
    mat.append(list(map(int,input().split())))


def check(road):
    for i in range(1,n):
        if abs(road[i] - road[i-1]) > 1 :
            return False;

        if road[i] < road[i-1] :
            for j in range(L):
                if i + j >= n or road[i] != road[i+j] or slope[i+j]:
                    return False
                if road[i] == road[i+j]:
                    slope[i+j] = True

        elif road[i] > road[i-1]:
            for j in range(L):
                if i - j - 1 < 0 or road[i-1] != road[i-j-1] or slope[i-j-1]:
                    return False
                if road[i-j-1] == road[i-1]:
                    slope[i-j-1] = True
    return True


cnt = 0

for i in mat:
    slope = [False] * n
    if check(i):
        cnt += 1

for j in range(n):
    slope = [False] * n
    if check([mat[i][j] for i in range(n)]):
        cnt += 1

print(cnt)