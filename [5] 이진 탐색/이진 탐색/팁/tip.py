import sys

# 입력 데이터 개수가 많은 문제에서 input() 함수를 사용하면
# 동작 속도가 느려서 시간 초과가 날 수도 있음!!

# 입력 데이터가 많은 문제는
# sys 라이브러리으 readline() 함수를 사용하면 시간 초과를 피할 수 있음
input_data = sys.stdin.readline().rstrip()

print(input_data)