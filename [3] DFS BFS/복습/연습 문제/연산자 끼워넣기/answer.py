import sys
import itertools

sys.stdin = open("input.txt", "r")

n = int(sys.stdin.readline().rstrip())

n_list = list(map(int, sys.stdin.readline().rstrip().split()))

# (+, -, x, %)
opr = ['+', '-', '*', '/']
opr_list = list(map(int, sys.stdin.readline().rstrip().split()))
oprs = []
for i in range(4):
    for _ in range(0, opr_list[i]):
        oprs.append(opr[i])

print(n)
print(n_list)
print(opr_list)
print(oprs)
# print(comb_list)

for operator in itertools.combinations(oprs, len(oprs)):
    for i in operator:
        if i =='+':

        elif i == '-':

        elif i =='*':

        else: