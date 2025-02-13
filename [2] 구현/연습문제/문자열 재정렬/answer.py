import sys

# sys.stdin = open("input.txt", "r")
sys.stdin = open("input_2.txt", "r")

# 입력값 : 알파벳 + 숫자로 이루어진 문자열
# 출력값 : 알파벳 오름차순 정렬 + 숫자합 문자열
# 예시 : K1KA5CB7 -> ABCKK13
# 예시2 : AJKDLSI412K4JSJ9D -> ADDIJJJKKLSS20

input_list = str(input())

str_list = ''
n_sum = 0

for i in input_list:
    print(i)
    if i.isalpha():
        str_list +=i
    else:
        n_sum+=int(i)
str_list = ''.join(sorted(str_list))

print(str_list + str(n_sum))