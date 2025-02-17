# 반복문으로 구현한 팩토리얼 함수
def factorial_iterative(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
# 재귀 함수로 구현한 팩토리얼 함수
def factorial_recursive(n):
    if n <= 1:
        return 1
    return n * factorial_recursive(n-1)

# factorial with iterative
print('factorial with iterative', factorial_iterative(5))

## 재귀함수로 구현했을 때, 코드가 더 간결하다는 장점이 있음
# factorial with recursive func
factorial_recursive(5)
print('factorial with recursive', factorial_recursive(5))