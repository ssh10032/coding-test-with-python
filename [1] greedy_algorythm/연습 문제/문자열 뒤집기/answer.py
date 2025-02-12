import sys

sys.stdin = open("input.txt", "r")

str_list = str(input())

print(str_list)

zero_count = 0
one_count = 0

first_string = str_list[0]
if first_string == '0':
    one_count += 1
else:
    zero_count += 1

for i in range(len(str_list)-1):
    if str_list[i] != str_list[i+1]:
        if str_list[i+1]=='1':
            zero_count+=1
        else:
            one_count+=1

# print(one_count)
# print(zero_count)

print(min(one_count, zero_count))


