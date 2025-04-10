# 이것이 취업을 위한 코딩 테스트다 wih python 공부
1. 그리디 알고리즘
   - 연습 문제 풀이 부족한 부분
       - 문자열 뒤집기
       - 만들 수 없는 금액
3. 구현
   - 연습 문제 풀이 부족한 부분
      - 문제 조건 파악
      - 완전 탐색 문제에서의 조합 구현
         - from itertools import combinations
         - itertools 라이브러리의 cobinations 함수 활용
5. DFS/BFS
   - DFS는 선입후출, 후입선출
      - 스택 자료 구조 사용
      - 재귀 호출로 구현
      - 시간 복잡도 O(N)
   - BFS는 선입선출
      - 큐 자료 구조 사용
      - collections 모듈의 deque 라이브러리를 주로 사용함
      - 최단 거리 구할 때 적합함, 일반적으로 DFS보다 조금 더 빠름
      - 시간 복잡도 O(N)
6. 정렬
7. 이진 탐색
8. 다이나믹 프로그래밍
   - 탑다운 구현 방식 : 재귀 호출, 상위 문제를 먼저 호출후 재귀 함수로 해결, 메모이제이션 기법 사용 
   - 바텀업 구현 방식 : 반복문, 하위 문제부터 호출해서 상위 문제를 해결
9. 최단 경로
   - 시작점이 정해져있는 경우 : 다익스트라 알고리즘
   - 시작점이 정해져있지 않는 경우 : 플로이드 워셜 알고리즘
   - 노드와 간선 수가 적으면, 플로이드 워셜 알고리즘으로 구현하는 것이 유리함
   - 노드와 간선 수가 많으면, 다익스트라 알고리즘으로 구현하는 것이 유리함
   - 다익스트라 알고리즘 : 여러 개의 노드가 있을 때, 특정한 노드에서 출발하여 다른 노드로 가는 각각의 최단 경로를 구해주는 알고리즘
       1. 출발 노드를 설정
       2. 최단 거리 테이블을 초기화
       3. 방문하지 않은 노드 중에서 최단 거리가 가장 짧은 노드를 선택
       4. 해당 노드를 거쳐 다른 노드로 가는 비용을 계산 -> 최단 거리 테이블을 갱신
       5. 위 과정에서 3과 4를 반복
   - 플로이드 워셜 알고리즘 구현 난이도 매우 쉬운 편 -> 최단 거리 기록 2차원 리스트와 최단 거리 비교용 삼중 for문만 만들면 쉽게 만들 수 있음
   - 우선 순위 힙을 활용한 다익스트라 알고리즘 구현 방식을 더 신경써서 구현 연습할 것
10. 그래프 이론
    - 서로소 집합 알고리즘
    - 신장 트리
         - 하나의 그래프가 있을 때, 모든 노드를 포함하면서 사이클이 존재하지 않는 부분 그래프
         - 크루스칼 알고리즘
              - 신장 트리 중에서 최소 비용으로 만들 수 있는 신창 트리를 찾는 알고리즘을 '최소 신장 트리 알고리즘'이라고 부름
              - 대표적인 최소 신장 트리 알고리즘으로 크루스칼 알고리즘이 있음
                1. 간선 데이터를 비용에 따라 오름 차순으로 정렬한다
                2. 간선을 하나씩 확인하며 현재의 간선이 사이클이 발생하는지 확인한다.
                   1. 사이클이 발생하지 않는 경우 최소 신장 트리에 포함시킨다.
                   2. 사이클이 발생하는 경우 최소 신장 트리에 포함시키지 않는다.
                3. 모든 간선에 대하여 2번의 과정을 반복한다.
         - 위상 정렬
            - 방향 그래프의 모든 노드를 '방향성에 거스르지 않도록 순서대로 나열하는 것'
            - 진입 차수
                 - 특정 노드로 들어오는 간선의 개수
            - 위상 정렬 알고리즘
                 1. 진입 차수가 0인 노드를 큐에 넣는다.
                 2. 큐가 빌 때까지 다음의 과정을 반복한다.
                      1. 큐에서 원소를 꺼내 해당 노드에서 출발하는 간선을 그래프에서 제거한다.
                      2. 새롭게 진입차수가 0이 된 노드를 큐에 넣는다
