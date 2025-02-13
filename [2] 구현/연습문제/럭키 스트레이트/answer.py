import sys
# sys.stdin = open("input.txt", "r")
sys.stdin = open("input_2.txt", "r")

# 럭키 스트레이트 : 왼쪽 자릿수 합과 오른쪽 자릿수 합이 같으면 LUCKY 출력
#              : 왼쪽 자릿수 합과 오른쪽 자릿수 합이 다르면 READY 출력
input_number = str(input())

number_len = len(input_number)

# 길이가 4이면, 왼쪽은 [0, 1] 오른쪽은 [2, 3]
left_number = input_number[:number_len//2]
right_number = input_number[number_len//2:]

left_sum = 0
right_sum = 0

for x, y in zip(left_number, right_number):
    left_sum+=int(x)
    right_sum+=int(y)

if left_sum == right_sum:
    print("LUCKY")
else:
    print("READY")