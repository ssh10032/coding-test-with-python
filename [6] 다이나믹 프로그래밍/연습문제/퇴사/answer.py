import sys
# 1 : 45
# 2 : 55
# 3 : 20
# 4 : 90
sys.stdin = open("input_4.txt", "r")

# 상담원이 퇴사전에 최대한 상담을 많이 해서 돈 많이 벌려고함
# N+1에 퇴사할 예정
# N일까지 최대한 많이 상담을 하려고함
n = int(sys.stdin.readline().rstrip())

# 상담을 완료하는 시간 T, 상담을 했을 때 받을 수 있는 금액 P
q = []
for idx in range(n):
    q.append(list(map(int, sys.stdin.readline().rstrip().split())))
d = [0] * n
# print(q)
# print(d)

for idx in range(n):
    if idx+q[idx][0]<n:
        d[idx] = max(d[idx], q[idx][1])
        mx = 0
        for s in range(idx, n):
            if s>=idx+q[idx][0] and s+q[s][0]<=n:
                d[s] = max(d[s], d[idx]+q[s][1])

print(d)
print(max(d))