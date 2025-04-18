import sys

sys.stdin = open("input.txt", "r")

# 전체 지도의 크기
n, m = map(int, sys.stdin.readline().rstrip().split())

# 시작 좌표 (a, b)와 방향 d
# 방향
# 0 : 북
# 1 : 동
# 2 : 남
# 3 : 서
# a가 행, b가 열임
a, b, d = map(int, sys.stdin.readline().rstrip().split())
field = []
visited = [[0] * m for _ in range(n)]
visited[a][b]=1
for _ in range(n):
    # 0 : 육지
    # 1 : 바다
    field.append(list(map(int, sys.stdin.readline().rstrip().split())))

#### 문제 조건 ####
#1 현재 위치에서 현재 방향을 기준으로 왼쪽 방향(반시계 방향으로 90도)부터 차례대로 갈 곳을 정함
#2 캐릭터의 바로 왼쪽 방향에 아직 가보지 않은 칸이 존재한다면, 왼쪽 방향으로 회전한다음 한칸 전진
# 왼쪽 방향에 가보지 않은 칸이 없다면, 왼쪽 방향으로 회전만 수행하고 1단계로 돌아감
#3 네 방향이 모두 가본 칸이거나 바다로 되어 있는 칸인 경우에는, 바라보는 방향을 유지한채로 한칸 뒤로 가고
# 1단계로 돌아감. 뒤쪽 방향이 바다인 칸이라 뒤로 못가는 경우 움직임을 멈춤.

directions = [0, 3, 2, 1]

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
c_idx = 0
for i in range(len(directions)):
    if d == directions[i]:
        c_idx = i
print("c_idx is", c_idx)
result = 0

# 내 접근 잘못된 부분 : 방향 전환을 for문으로 하는게 잘못됨?
while True:
    for i in range(1, len(directions)+1):
        n_idx = (c_idx+i)%4
        na = a + dx[n_idx]
        nb = b+ dy[n_idx]
        # print("na is ", na)
        # print("nb is ", nb)

        if field[na][nb]==0 and visited[na][nb]==0:
            print("na is ", na)
            print("nb is ", nb)
            a = na
            b = nb
            c_idx=n_idx
            visited[na][nb]=1
            result+=1
            print(1)
            break
        else:
            print(2)
        if i==4:
            if field[a-dx[c_idx]][b-dy[c_idx]]==1:
                print(3)
                break
            else:
                print(4)
                a -= dx[c_idx]
                b -= dy[c_idx]

    print("for break")

print("result", result)
print("end")