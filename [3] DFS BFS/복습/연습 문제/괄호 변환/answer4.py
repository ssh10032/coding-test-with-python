import sys
# (와 )의 개수가 같다면 균형 잡힌 문자열
# () 괄호의 짝도 모두 맞을 경우 올바른 문자열
# sys.stdin = open("input.txt", "r")
sys.stdin = open("input3.txt", "r")

str_lst = sys.stdin.readline().rstrip()
str_lst = str_lst[1:-1]

# 균형 잡힌 문자열 > 올바른 문자열 변환 과정
#1 입력이 빈 문자열인 경우, 빈 문자열 반환
#2 문자열 w를 "균형 잡힌 괄호 문자열" u, v로 분리함
# u는 "균형잡힌 문자열", 더 이상 분리할 수 없어야함
# v는 빈문자열이 될수 있음
#3 수행한 결과 문자열을 u에 이어 붙인 후 반환
#3-1 문자열 u가 "올바른 문자열"이라면 문자열 v열에 대해 1단계부터 수행
#4 문자열 u가 올바른 괄호 문자열이 아니라면 아래 과정 수행
#4-1 빈 문자열에 첫번째 문자로 "("를 붙임
#4-2 문쟈열 v에 대해 1단계부터 재귀적으로 수행한 결과 문자열을 이어붙임
#4-3 )를 다시 붙임
#4-4 u의 첫번째와 마지막 문자를 제거, 나머지 문자열의 괄호 방향을 뒤집어서 뒤에 붙임
#4-5 생성된 문자열을 반환
print(str_lst)

def seperate(str_lst):
    count=0
    for i in range(len(str_lst)):
        if str_lst[i]=='(':
            count+=1
        else:
            count-=1
        if count==0:
            u = str_lst[:i+1]
            v = str_lst[i+1:]
            return u, v
    return str_lst, ''

def dfs(str_lst):
    if len(str_lst)==0:
        return ""
    u, v = seperate(str_lst)
    if u[0]==')':
        temp = '(' + dfs(v) + ')'
        for i in u[1:-1]:
            if i == '(':
                temp+=')'
            else:
                temp+='('
    else:
        temp = u + dfs(v)
    return temp

print(dfs(str_lst))


