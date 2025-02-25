import sys

sys.stdin = open("input.txt", "r")

n = int(input())
usr_lst = list(map(int, input().split()))
clear_list = []


def check_failure(n, usr_list):
    clear_list = [[idx+1, 0] for idx in range(n)]
    for usr in usr_list:
        if usr <= n:
            clear_list[usr-1][1] = clear_list[usr-1][1] + 1
    print(clear_list)
    for idx in range(len(clear_list)):
        total_player = sum(1 for usr in usr_list if usr>=clear_list[idx][0] )
        clear_list[idx][1] = clear_list[idx][1]/total_player
    clear_list = sorted(clear_list, key=lambda x:x[1], reverse=True)
    return clear_list

clear_list = check_failure(n, usr_lst)
for i in range(len(clear_list)):
    print(clear_list[i][0], end=' ')
