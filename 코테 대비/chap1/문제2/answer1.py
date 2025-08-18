import sys

sys.stdin = open("input.txt", "r")

input = str(sys.stdin.readline().rstrip())

def find_count_to_turn_out_to_all_zero_or_all_one(string):
    count_to_all_zero = 0
    count_to_all_one = 0

    if string[0]=='0':
        count_to_all_one += 1
    elif string[0]=='1':
        count_to_all_zero +=1

    for i in range(len(string)-1):
        if string[i]!=string[i+1]:
            if string[i+1]=='0':
                count_to_all_one+=1
            if string[i+1]=='1':
                count_to_all_zero+=1
    return min(count_to_all_zero, count_to_all_one)

print(find_count_to_turn_out_to_all_zero_or_all_one(input))