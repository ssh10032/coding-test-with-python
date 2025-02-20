import sys

sys.stdin = open("input_3.txt")
# input.txt
# "(()())()"	"(()())()"
# input_2.txt
# ")("	"()"
# input_3.txt
# "()))((()"	"()(())()"


# (와 )의 개수가 같은 경우 : 균형 잡힌 괄호 문자열
# (와 ) 괄호의 짝이 모두 맞을 경우 : 올바른 괄호 문자열

# 균형 잡힌 문자열 -> 올바른 괄호 문자열 변환
#1 입력이 빈 문자열인 경우, 빈 문자열 반환
#2 문자열 w를 두 균형잡힌 괄호 문자열 u, v로 분리
#단, u는 균형잡힌 문자열로 더이상 분리할수 없어야하며, v는 빈 문자열이 될 수 있음
#3 문자열 u가 올바른 괄호 문자열이라면 문자열 v에 대해 1단계부터 다시 수행
    #3-1 수행한 결과 문자열을 u에 이어붙인 후 반환
#4 문자열 u가 올바른 괄호 문자열이 아니면, 아래 과정 수행
    #4-1 빈 문자열에 첫 번째 문자로 '('를 붙임
    #4-2 문자열 v에 대해 1단계부터 재귀적으로 수행한 결과 문자열을 이어붙임
    #4-3 )를 다시 붙임
    #4-4 u의 첫 번째와 마지막 문자를 제거하고, 나머지 문자열의 괄호 방향을 뒤집어서 뒤에 붙임.
    #4-5 생성된 문자열 반환

# 이렇게 조건이 세세하게 적혀있는 경우에는
# 쫄지 말고 조건 대로 만들면 됨
# 재귀 호출하라고 직접 언급했음 >> DFS로 풀라는 소리

def check_balance(target_str):
    if target_str[0]!='(':
        return False

    stack_list = []
    for i in range(len(target_str)):
        if target_str[i] == '(':
            stack_list.append('')
        else:
            if len(stack_list)==0:
                return False
            else:
                stack_list.pop()
    return len(stack_list)==0

def spr_str(target_str):
    stk_str = target_str[0]
    stack_list = []
    u_idx = 0
    for i in range(len(target_str)):
        if target_str[i] == stk_str:
            if i!=0 and len(stack_list)==0:
                u_idx = i
                break
            stack_list.append('')
        else:
            if len(stack_list)==0:
                u_idx = i
                break
            else:
                stack_list.pop()
                if len(stack_list)==0:
                    u_idx = i
                    break
    return target_str[:u_idx+1], target_str[u_idx+1:]


str_list = str(input())

print(str_list)

def dfs(str_list):
    if len(str_list) == 0:
        return ''
    u, v = spr_str(str_list)
    if check_balance(u):
        return u + dfs(v)
    else:
        str_pls = '(' + dfs(v) + ')'
        u_pls = u[1:-1]
        u_refact = ''
        for i in u_pls:
            if i == '(':
                u_refact+=')'
            else:
                u_refact += '('
        return str_pls + u_refact

print(dfs(str_list))

