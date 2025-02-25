# 약한 부분
  - sorted 함수의 key 인자에서 정렬 단위를 우선순위 순서대로 여러개로 지정해줄수 있음
  - 조건문 여러개 안만들고, 매우 짧게 만들 수 있으니까 기억해두자
  - 붙이면 내림차순, +면 오름차순
    - std_list.sort(key=lambda std:(-std[1], std[2], -std[3], std[0]))
    - std_list = sorted(std_list, key=lambda std:(-std[1], std[2], -std[3],std[0]))
