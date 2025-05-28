import sys

sys.stdin = open("input.txt", "r")

n, k = map(int, sys.stdin.readline().rstrip().split())

list1 = list(map(int, sys.stdin.readline().rstrip().split()))
list2 = list(map(int, sys.stdin.readline().rstrip().split()))

print(list1)
print(list2)

list1.sort()
list2.sort()

print(list1)
print(list2)

sum1 = sum(list1[k:])
sum2 = sum(list2[-k:])

print(sum1)
print(sum2)

print(sum1+sum2)