import sys

sys.stdin = open("input.txt", "r")

n = int(sys.stdin.readline().rstrip())

array = []
for i in range(n):
    name, score = map(str, sys.stdin.readline().rstrip().split())
    array.append((name, int(score)))

print(array)

array = sorted(array, key=lambda student:student[1])

print(array)

for student in array:
    print(student[0], end=' ')