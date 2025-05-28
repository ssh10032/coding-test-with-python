import sys

sys.stdin = open("input.txt", "r")

n = int(sys.stdin.readline().rstrip())

print(n)

score_list = []

for _ in range(n):
    name, score = map(str, sys.stdin.readline().rstrip().split())
    score_list.append((name, int(score)))

print(score_list)

# lambda 입력 형식
# 원본이 될 데이터:원본데이터로부터 참조해야할 데이터
result = sorted(score_list, key = lambda score_list:score_list[1])
score_list.sort(key=lambda score_list:score_list[1])

print(score_list)

print(result)

for i in score_list:
    print(i[0], end=' ')