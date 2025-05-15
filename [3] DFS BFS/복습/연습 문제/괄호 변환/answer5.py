import sys

sys.stdin = open("input.txt", "r")

str_lst = sys.stdin.readline().rstrip()
str_lst = str_lst[1:-1]
def answer(str_lst):
    count=0
    if len(str_lst)==0:
        return ""
    for idx in range(len(str_lst)):
        if str_lst[idx] == "(":
            count+=1
        else:
            count-=1
        if count==0:
            if str_lst[0]=="(":
                return str_lst[:idx+1]+answer(str_lst[idx+1:])
            else:
                v = "(" + answer(str_lst[idx+1:]) + ")"
                u = ""
                for i in str_lst[1:idx]:
                    if i =="(":
                        u+=")"
                    else:
                        u+="("
                return v+u
print(answer(str_lst))
