import sys

sys.stdin = open("input.txt", "r")

def cal_max(num_list, m, k):
    m_count = 0
    result = 0
    a = num_list[0]
    b = num_list[1]
    while True:
        for i in range(k):
            print(a)
            result+=a
            m_count+=1
            if m_count==m:
                return result
        result+=b
        print(b)
        m_count+=1
        if m_count==m:
            return result

# m번 더하여 가장 큰 수를 만듬, 같은 숫자는 연속 k번 초과해서 못더함
n, m, k = map(int, sys.stdin.readline().rstrip().split())

num_list = list(map(int, sys.stdin.readline().rstrip().split()))

num_list.sort(reverse=True)

print(num_list)


print(cal_max(num_list, m, k))