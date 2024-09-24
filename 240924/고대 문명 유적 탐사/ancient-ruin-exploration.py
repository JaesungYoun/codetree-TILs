from collections import deque


N_large = 5
N_small = 3

class Board:
    def __init__(self):
        self.a = [[0 for _ in range(N_large)] for _ in range(N_large)]


    def in_range(self,x,y):
        return 0<=x<N_large and 0<=y<N_large

    def rotate(self, sx, sy, cnt):
        result = Board()
        result.a = [row[:] for row in self.a]
        for _ in range(cnt):
            tmp = result.a[sx+0][sy+2]
            result.a[sx+0][sy+2] = result.a[sx+0][sy+0]
            result.a[sx+0][sy+0] = result.a[sx+2][sy+0]
            result.a[sx+2][sy+0] = result.a[sx+2][sy+2]
            result.a[sx+2][sy+2] = tmp
            tmp = result.a[sx+1][sy+2]
            result.a[sx+1][sy+2] = result.a[sx+0][sy+1]
            result.a[sx+0][sy+1] = result.a[sx+1][sy+0]
            result.a[sx+1][sy+0] = result.a[sx+2][sy+1]
            result.a[sx+2][sy+1] = tmp

        return result


    def cal_score(self):
        score = 0
        visit = [[False for _ in range(N_large)] for _ in range(N_large)]
        dx, dy = [-1,1,0,0], [0,0,-1,1]

        for i in range(N_large):
            for j in range(N_large):
                if not visit[i][j]:
                    q = deque()
                    trace = deque()
                    q.append((i,j))
                    trace.append((i,j))
                    visit[i][j] = True
                    while q:
                        x,y = q.popleft()
                        for d in range(4):
                            nx = x + dx[d]
                            ny = y + dy[d]
                            if self.in_range(nx,ny) and self.a[nx][ny] == self.a[x][y]  and not visit[nx][ny]:
                                q.append((nx,ny))
                                trace.append((nx,ny))
                                visit[nx][ny] = True

                    if len(trace) >= 3:
                        score += len(trace)
                        while trace:
                            tx,ty = trace.popleft()
                            self.a[tx][ty] = 0

        return score

    def fill(self,que):
        for j in range(N_large):
            for i in range(N_large-1, -1, -1):
                if self.a[i][j] == 0:
                    self.a[i][j] = que.popleft()


def main():
    # 입력을 받습니다.
    K, M = map(int, input().split())
    board = Board()
    for i in range(N_large):
        board.a[i] = list(map(int, input().split()))
    q = deque()
    for t in list(map(int, input().split())):
        q.append(t)

    # 최대 K번의 탐사과정을 거칩니다.
    for _ in range(K):
        maxScore = 0
        maxScoreBoard = None
        # 회전 목표에 맞는 결과를 maxScoreBoard에 저장합니다.
        # (1) 유물 1차 획득 가치를 최대화
        # (2) 회전한 각도가 가장 작은 방법을 선택
        # (3) 회전 중심 좌표의 열이 가장 작은 구간을, 그리고 열이 같다면 행이 가장 작은 구간을 선택
        for cnt in range(1, 4):
            for sy in range(N_large - N_small + 1):
                for sx in range(N_large - N_small + 1):
                    rotated = board.rotate(sx,sy, cnt)
                    score = rotated.cal_score()
                    if maxScore < score:
                        maxScore = score
                        maxScoreBoard = rotated
        # 회전을 통해 더 이상 유물을 획득할 수 없는 경우 탐사를 종료합니다.
        if maxScoreBoard is None:
            break
        board = maxScoreBoard
        # 유물의 연쇄 획득을 위해 유물 조각을 채우고 유물을 획득하는 과정을 더이상 획득할 수 있는 유물이 없을때까지 반복합니다.
        while True:
            board.fill(q)
            newScore = board.cal_score()
            if newScore == 0:
                break
            maxScore += newScore

        print(maxScore, end=" ")

if __name__ == '__main__':
    main()