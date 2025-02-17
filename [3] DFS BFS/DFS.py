def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')
    for i in graph[v]:
        if not visited[i]:
            # 재귀 호출
            dfs(graph, i, visited)

# 그래프의 각 노드가 연결된 정보를 리스트 자료형으로 표현(2차원 리스트)
graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

# 노드가 방문된 정보를 리스트 자료형으로 표현
visited = [False] * 9

# 정의된 DFS 함수 호출
dfs(graph, 1, visited)