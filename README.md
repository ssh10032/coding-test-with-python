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
4. DFS/BFS
   - DFS는 선입후출, 후입선출
      - 스택 자료 구조 사용
      - 재귀 호출로 구현
      - 시간 복잡도 O(N)
   - BFS는 선입선출
      - 큐 자료 구조 사용
      - collections 모듈의 deque 라이브러리를 주로 사용함
      - 최단 거리 구할 때 적합함, 일반적으로 DFS보다 조금 더 빠름
      - 시간 복잡도 O(N)
