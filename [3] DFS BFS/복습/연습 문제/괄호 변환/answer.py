import sys

sys.stdin = open("input2.txt", "r")

# (와 )의 개수가 맞으면 '균형 잡힌 문자열'
# (와 )의 짝이 맞는 경우 '올바른 괄호 문자열'
str_list = sys.stdin.readline().rstrip()
str_list = str_list[1:-1]

print(str_list)

def balanced_index(p):
    count = 0
    for i in range(len(p)):
        if p[i] == '(':
            count+=1
        else:
            count-=1
        if count == 0:
            return i
def check_proper(p):
    count = 0
    for i in p:
        if i =='(':
            count+=1
        else:
            if count==0:
                return False
            count-=1
    return True

def solution(p):
    answer = ''
    if p =='':
        return answer
    index = balanced_index(p)
    u = p[:index+1]
    v = p[index+1:]

    if check_proper(u):
        answer = u + solution(v)
    else:
        answer = '('
        answer+=solution(v)
        answer+=')'
        u = list(u[1:-1])
        for i in range(len(u)):
            if u[i]=='(':
                u[i]=')'
            else:
                u[i]='('
        answer+="".join(u)
    return answer

print(solution(str_list))