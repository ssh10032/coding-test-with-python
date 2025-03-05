import sys

sys.stdin = open("input.txt", "r")

line = int(sys.stdin.readline().rstrip())

# n * m 크기의 행렬이 있음
# 각 칸은 특징한 크기의 금이 들어있음
# 맨 처음에는 첫번째 열의 어느 행어서든 출발 가능
# 이후에, m번에 걸쳐서 매번 오른쪽 위, 오른쪽, 오른쪽 아래 3가지 중 한가지 위치로 이동해야함
# 결과적으로 채굴자가 얻을 수 있는 금의 최대 크기를 출력하는 프로그램을 작성하시오.
# 1 3 3 2
# 2 1 4 1
# 0 6 4 7

# 1 3 1 5
# 2 2 4 1
# 5 0 2 3
# 0 6 1 2

dy = [-1, 0, 1]
for _ in range(line):
    n, m = map(int, sys.stdin.readline().rstrip().split())
    # golds = [gold for gold in list(map(int, sys.stdin.readline().rstrip().split()))]
    g_list = list(map(int, sys.stdin.readline().rstrip().split()))
    golds = []

    for idx in range(0, n*m, m):
        golds.append(g_list[idx:idx+m])

    d = [[0] * m for i in range(n)]

    for idx in range(n):
        d[idx][0] = golds[idx][0]

    for column in range(1, m):
        for row in range(n):
            for y in range(len(dy)):
                if 0<=row + dy[y]<n:
                    d[row][column] = max(d[row][column], golds[row][column]+d[row+dy[y]][column-1])
    mx = 0
    for row in range(n):
        mx = max(mx, d[row][m-1])
    print(mx)
