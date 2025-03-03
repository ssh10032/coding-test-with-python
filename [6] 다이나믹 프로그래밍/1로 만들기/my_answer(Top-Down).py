import sys
# answer
# input 1: 1
sys.stdin = open("input.txt", "r")

n = int(sys.stdin.readline().rstrip())
d = [-1] * (n+1)

def recursive_dynamic(n):
    if d[n]!=-1:
        return d[n]
    if n == 1:
        return 0
    else:
        result = 1 + recursive_dynamic(n - 1)
        if n%5==0:
            result = min(result, 1 + recursive_dynamic(n//5))
        if n%3==0:
            result = min(result, 1 + recursive_dynamic(n//3))
        if n%2==0:
            result = min(result, 1 + recursive_dynamic(n//2))
        d[n] = result
    return d[n]




# 정수 X가 주어질 때 적용할 수 있는 연산 4가지
#1 X가 5로 나누어떨어지면, 5로 나눔
#2 3으로 나누어떨어지면, 3으로 나눔
#3 2로 나누어떨어지면, 2로 나눔
#4 X에서 1을 뺌
print(n)
print(recursive_dynamic(n))