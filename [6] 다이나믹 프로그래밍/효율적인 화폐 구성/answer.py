import sys

sys.stdin = open("input_2.txt", "r")

# n가지 종류의 화폐가 있음

# 이 화폐들을 개수를 최소한으로 활용해서
# 합이 m원이 되도록 만들고자 함..
# 불가능할 때에는 -1을 출력

n, m = map(int, sys.stdin.readline().rstrip().split())

n_list = []
for _ in range(n):
    n_list.append(int(sys.stdin.readline().rstrip()))

print(n_list)

d = [-1] * (m+1)

for n in n_list:
    if 0<=n<m+1:
        d[n] = 1

for i in range(1, m+1):
    for n in n_list:
        if 0<=i-n<m+1 and d[i-n]!=-1 :
            if d[i]==-1:
                d[i] = d[i-n] + 1
            else:
                d[i] = min(d[i], d[i-n]+1)

print(d)
print(d[m])


