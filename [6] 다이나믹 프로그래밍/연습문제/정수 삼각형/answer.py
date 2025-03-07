import sys

sys.stdin = open("input.txt", "r")

n = int(sys.stdin.readline().rstrip())

# 생각해보니 d 배열을 따로 만들 필요가 없었음
# test 배열을 그대로 사용해도 문제 될게 없음 >> 메모리 절약
# print(n)
d = []
test = []
for _ in range(n):
    n_list = list(map(int, sys.stdin.readline().rstrip().split()))
    test.append(n_list)
    # print(len(n_list))
    d.append([0] * len(n_list))

d[0][0] = test[0][0]
# 만약에 배열 행이 0만 있으면 1행을 이런 방식으로 초기화하는 건 에러가 날 수 있음
# 예외적으로 처리하는걸 최대한 줄이고
# 같은 코드 내에서 일괄적으로 처리할 수 있으면
# 최대한 포함시키는 방향으로 생각하자.
d[1][0] = d[0][0] + test[1][0]
d[1][1] = d[0][0] + test[1][1]

for r in range(2, n):
    for c in range(len(d[r])):
        if c == 0:
            d[r][c] = test[r][c] + d[r-1][c]
        elif c == len(d[r])-1:
            d[r][c] = test[r][c] + d[r-1][c-1]
        else:
            d[r][c] = test[r][c] + max(d[r-1][c-1], d[r-1][c])

# print(test)
# print(d)

print(max(d[-1]))