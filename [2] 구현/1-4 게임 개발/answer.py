import sys

sys.stdin = open("input.txt", "r")

n, m = map(int, input().split())

# 가본 지역을 표시하기 위한 0으로 구성된 행렬 생성
d = [[0] * m for _ in range(n)]

# 방향 북 : 0, 동 : 1, 남 : 2, 서 : 3
# 맵에서 1은 바다, 0은 육지
# 1. 현재 위치, 방향을 기준으로 왼쪽 방향부터 차례대로 갈 곳을 결정
# 2-1. 바로 왼쪽에 가보지 않은 칸이 존재하면, 왼쪽 방향 회전 후 한 칸 전진
# 2-2. 왼쪽 방향에 가보지 않은 칸이 존해하지 않으면, 왼쪽 방향으로 회전만 하고 1단계로 돌아감
# 3. 만약 네 방향 모두 가본 칸이거나, 바다인 경우, 바라보는 방향은 유지한 채로 한 칸 뒤로 후진. 1단계로 돌아감
# 뒤쪽 방향이 바다인 칸이라 뒤로 갈 수 없는 경우, 움직임을 멈춘다

x, y, direction = map(int, input().split())
# 초기 위치 방문 표시
d[x][y] = 1

# 전체 맵 행렬 생성
array = []
for i in range(n):
    array.append(list(map(int, input().split())))

# 방향 설정 북 동 남 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 방향 전환 함수
def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

count = 1
turn_time = 0
while True:
    # 왼쪽으로 회전
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]

    # 회전한 이후 정면에 가보지 않은 칸이 존재할 경우
    if d[nx][ny]==0 and array[nx][ny]==0:
        d[nx][ny]=1
        x = nx
        y = ny
        count+=1
        turn_time=0
        continue
    # 회전한 이후 정면에 가보지 않은 칸이 없거나 바다인 경우
    else:
        turn_time+=1
    # 네 방향 모두 갈 수 없는 경우
    if turn_time==4:
        nx = x - dx[direction]
        ny = y - dy[direction]

        # 뒤로 갈 수 있다면 이동
        if array[nx][ny]==0:
            x = nx
            y = ny
        # 뒤가 바다로 막혀 있는 경우
        else:
            break
        turn_time=0

# 정답 출력
print(count)