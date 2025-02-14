import sys
# input 1 : 7
# input 2 : 9
# input 3 : 8
# input 4 : 14
# input 5 : 17
sys.stdin = open("input_5.txt", "r")
# aabbaccc  >>  총 길이 : 7, 자를 문자열 길이 : 7//2 = 3까지만 체크
# 문자열 길이가 1이면, 2a2ba3c >> 길이 7
# 문자열 길이가 2이면, aabbaccc >> 길이 8
# 문자열 길이가 3이면, aabbaccc >> 길이 8
s = str(input())
answer = 0
str_len = len(s)
chk_len = str_len // 2
# print(s)

# print(str_len)
# print(chk_len)
results = []


# 내가 놓쳤던 부분
# 문자열 압축 count가 한 자리 수가 아닐 경우도 생각 했어야 했음 ex) 12a >> 길이 3, 18b >> 길이 3
# len(str(count))
for i in range(1, chk_len + 1):
    count = 1
    result = 0
    for j in range(0, str_len - i, i):
        if s[j:j + i] == s[j + i:j + 2 * i]:
            count += 1
            if j + i >= str_len - i:
                result += (i+len(str(count)))
        else:
            if count > 1:
                if j + i >= str_len - i:
                    result += (i + len(str(count))) + len(s[j+i:])
                else:
                    result += (i + len(str(count)))
            else:
                if j + i >= str_len - i:
                    result += i + len(s[j+i:])
                else:
                    result += i
            count = 1
    results.append(result)

print(min(results))
