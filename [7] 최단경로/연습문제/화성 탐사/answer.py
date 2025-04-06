import sys

# 문제 접근 : 시작과 도착 지점이 정해져 있음. 최단 경로를 구해야함
# 시작, 도착 지점이 정해져 있는 최단 경로 문제이므로
# 다익스트라 알고리즘을 사용

# 우선순위 큐를 활용해서 최단거리 리스트 업데이트 하자!!
import heapq

sys.stdin = open("input.txt", "r")

# 비용 리스트 초기화 값(무한)
INF = int(1e9)

# 테스트 케이스 수
n = int(sys.stdin.readline().rstrip())

# 그래프 이동 방향 리스트
# 비용이 0인 경우도 있어서 정확한 최단 경로를 구하려면
# (좌, 우)가 아닌 (상, 하, 좌, 우) 모두 체크해줘야함!!!
d = [(0, 1), (0, -1), (1, 0), (-1, 0)]

for _ in range(n):
    # 시작 좌표
    x, y = 0, 0
    # 공간(space) 정보 -> sp * sp 크기의 맵
    sp = int(sys.stdin.readline().rstrip())
    # 최단 거리 비용 그래프 초기화
    cost = [[INF] * sp for _ in range(sp)]

    graph = []
    for _ in range(sp):
        # 각 좌표별 이동 비용 그래프 입력
        graph.append(list(map(int, sys.stdin.readline().rstrip().split())))

    # 우선 순위 큐를 활용한 다익스트라 알고리즘 시작
    q = []
    # 1.비용 2.좌표값을 우선 순위 큐에 push
    heapq.heappush(q, (graph[0][0], (x, y)))
    cost[0][0] = graph[0][0]
    while q:
        # 가장 비용이 적은 좌표 pop
        dist, now = heapq.heappop(q)
        if cost[now[0]][now[1]] < dist:
            continue
        # 좌표 이동 후의 cost 기록
        for dx, dy in d:
            if 0<=now[0]+dx<sp and 0<=now[1]+dy<sp:
                nx = now[0]+dx
                ny = now[1]+dy
                c = dist + graph[nx][ny]
                # 현재 최단거리 비용 그래프의 값보다 작을 경우 덮어쓰기
                if c < cost[nx][ny]:
                    cost[nx][ny]=c
                    # 우선 순위 큐에 비용과 함께 push
                    heapq.heappush(q, (c, (nx, ny)))
    print(cost[sp-1][sp-1])

    # while True:
    #     for dx, dy in d:
    #         cost[x+dx][y+dy] = min(cost[x+dx][y+dy],cost[x][y]+graph[x+dx][y+dy])

    # print(cost)
