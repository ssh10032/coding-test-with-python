import sys

sys.stdin = open("input.txt", "r")

n, k = map(int, sys.stdin.readline().rstrip().split())

list1 = list(map(int, sys.stdin.readline().rstrip().split()))
list2 = list(map(int, sys.stdin.readline().rstrip().split()))

list1.sort()
list2.sort(reverse=True)

for i in range(k):
    if list1[i]<list2[i]:
        list1[i], list2[i] = list2[i], list1[i]
    else:
        break

print(sum(list1))