import sys

sys.stdin = open("input.txt", "r")

# 못생긴 수 = 2, 3, 5만을 소인수(약수)로 가지는 수를 말함
# 1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15, ...
# n 번째 못생긴 수를 찾는 프로그램을 작성
n = int(sys.stdin.readline().rstrip())

d = []
num_list = [2, 3, 5]
d.append(1)
d.append(2)
d.append(3)
d.append(5)
print(n)


# 이렇게 구현하면 작은 크기 순으로 정렬되지 않는 문제가 있음
for i in d:
    for num in num_list:
        if i * num in d:
            pass
        else:
            d.append(i*num)
    if len(d) > 100:
        break

d.sort()
print(d)