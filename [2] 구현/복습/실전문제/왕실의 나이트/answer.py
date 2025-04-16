import sys

sys.stdin = open("input.txt", "r")

start = str(sys.stdin.readline().rstrip())
row = int(start[1])
col = int(ord(start[0])-ord('a')+1)

print(row)
print(col)
# 8 * 8 평면
# 나이트는 L자 형태로만 이동 가능
# 정원 밖으로는 나갈수 없음
# 이동하는 경우
#1 수평으로 두 칸 이동한 뒤에 수직으로 한 칸 이동하기
#2 수직으로 두 칸 이동한 뒤에 수평으로 한 칸 이동하기

# 행 위치 1~8로 표현
# 열 위치 a~h로 표현

move_type = [(1, 2), (-1, 2), (1, -2), (-1, -2), (2, 1), (-2, 1), (2, -1), (-2, -1)]

result = 0

for i in move_type:
    if 0<row+i[0]<=8 and 0<col+i[1]<=8:
        result+=1

print(result)