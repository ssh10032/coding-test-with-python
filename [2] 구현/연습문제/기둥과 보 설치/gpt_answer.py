import sys

# 부족한 점 : 길다고 쫄지 말 것
# 구조물을 지을 수 있는지 타당성 체크
# 문제 조건만 잘 따지면
# 어렵지 않게 만들 수 있음
def can_build_pillar(x, y, structure):
    return y==0 or (x, y-1,0) in structure or (x-1, y, 1) in structure or (x, y, 1) in structure
def can_build_beam(x, y, structure):
    return (x, y-1, 0) in structure or (x+1, y-1, 0) in structure or ((x-1, y, 1) in structure and (x+1, y, 1) in structure)
def check_valid(structure):
    for x, y, a in structure:
        if a==0 and not can_build_pillar(x, y, structure):
            return False
        if a==1 and not can_build_beam(x, y, structure):
            return False
    return True

sys.stdin = open("input.txt", "r")

n, m = map(int, input().split())

build_frame = [list(map(int, input().split(','))) for _ in range(m)]

structure = set()

# 구조물 추가/제거
# 구조물이 추가/제거되었을 때의 타당성 검증 후
# 명령 수행
for x, y, a, b in build_frame:
    if b == 1:
        structure.add((x, y, a))
        if not check_valid(structure):
            structure.remove((x, y, a))
    else:
        structure.remove((x, y, a))
        if not check_valid(structure):
            structure.add((x, y, a))

print(sorted(structure, key=lambda x : (x[0], x[1], x[2])))
