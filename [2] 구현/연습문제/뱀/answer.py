import sys

sys.stdin = open("input_2.txt", "r")
# 뱀 게임
# 뱀이 돌아다니다가 벽 or 자신의 몸에 부딪히면 게임이 끝남
# 뱀의 초기 위치는 (0,0), 초기 방향은 오른쪽, 초기 길이는 1
dx = 0
dy = 1
# 먼저 뱀은 몸 길이를 늘려 머리를 다음 칸에 위치 시킴
# 이동한 칸에 사과가 있으면, 그 칸의 사과는 없어지고 꼬리는 움직이지 않음
# 이동한 칸에 사과가 없으면, 몸 길이를 줄여서 꼬리가 위치한 칸을 비워줌. 몸길이는 변하지 않음
# 0은 빈칸, 1은 사과, 2는 뱀
c_time = 0
x, y = 0, 0
board_len = int(input())
print(board_len)
board = [[0] * board_len for _ in range(board_len)]
# 뱀의 초기 위치
board[x][y] = 2
apple_num = int(input())
for _ in range(apple_num):
    a_x, a_y = map(int, input().split())
    board[a_x][a_y] = 1

hebi_dir_num = int(input())
hebi_dir = {}
# 뱀의 방향 전환 정보 : (시간, 방향)
# L : 왼쪽으로 90도 회전, D : 오른쪽으로 90도 회전
for _ in range(hebi_dir_num):
    time, direction = map(str, input().split())
    hebi_dir[int(time)] = direction

while True:
    if c_time in hebi_dir:
        print(c_time)
        print(hebi_dir[c_time])
        if hebi_dir[c_time] == 'L':
            if dx ==0 and dy ==1:
                dx, dy = -1, 0
            elif dx==0 and dy==-1:
                dx, dy = 1, 0
            elif dx == -1 and dy == 0:
                dx, dy = 0, -1
            elif dx == 1 and dy == 0:
                dx, dy = 0, 1
        else:
            if dx ==0 and dy ==1:
                dx, dy = 1, 0
            elif dx==0 and dy==-1:
                dx, dy = -1, 0
            elif dx == -1 and dy == 0:
                dx, dy = 0, 1
            elif dx == 1 and dy == 0:
                dx, dy = 0, -1
    else :
        print(c_time)

    c_time += 1
    for i in range(board_len):
        print(board[i])
    print(' ')
    if (x+dx) >= board_len or (y+dy) >= board_len or (x+dx) < 0 or (y+dy)<0:
        print('out of range')
        break
    if board[x+dx][y+dy]==1:
        x = x + dx
        y = y + dy
        board[x][y] = 2
    elif board[x+dx][y+dy]==0:
        board[x][y] = 0
        x = x+dx
        y = y+dy
        board[x][y]=2
    else:
        print('hebi body')
        break

print(board)
print(hebi_dir)
print(c_time)