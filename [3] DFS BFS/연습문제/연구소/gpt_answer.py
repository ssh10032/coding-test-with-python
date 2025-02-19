import sys
import itertools
import copy

# input 1 answer: 27
# input 2 answer: 9
# input 3 answer: 3
sys.stdin = open("input_3.txt", "r")

n, m = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(n)]

# 방향 벡터
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 빈 칸과 바이러스 위치 저장
# 빈 칸 중에 3개를 골라 벽으로 세워야 한다는 것
empty_spaces = []
virus_positions = []

for i in range(n):
    for j in range(m):
        if lab[i][j] == 0:
            empty_spaces.append((i, j))
        elif lab[i][j] == 2:
            virus_positions.append((i, j))

# 바이러스 확산(DFS)
# stack : FILO(선입후출)
def spread_virus(grid):
    stack = virus_positions[:]
    while stack:
        x, y = stack.pop()
        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            if 0 <= nx < n and 0<= ny < m and grid[nx][ny]==0:
                grid[nx][ny]=2
                stack.append((nx, ny))

# 안전 영역 크기 계산
def get_safe_area(grid):
    safe_count = sum(row.count(0) for row in grid)
    return safe_count

max_safe_area = 0

### 내가 부족했던 부분 : 벽을 세우는 것도 DFS나 BFS를 사용해서 구현해야된다고 생각함
### 바이러스 퍼지는 것, 벽 세우는 것
# 두개를 구현해야하는데
# 바이러는 dfs, 벽은 단순 조합이었음
#### 문제를 너무 어렵게 생각하고 접근하지 않아도 됨 ####

# 3개의 벽을 세우는 방식 구현
# itertools의 combination 라이브러리 사용
# 빈 공간(0)에서 3개를 뽑는 조합 사용
for walls in itertools.combinations(empty_spaces, 3):
    # 연구소 랩 복사본 생성
    temp_lab = copy.deepcopy(lab)

    # 벽 세우기
    for x, y in walls:
        temp_lab[x][y] = 1

    # 바이러스 확산
    spread_virus(temp_lab)

    # 안전 영역 계산
    safe_area = get_safe_area(temp_lab)
    max_safe_area = max(max_safe_area, safe_area)

print(max_safe_area)


