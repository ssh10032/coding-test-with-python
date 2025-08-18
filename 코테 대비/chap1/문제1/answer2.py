import sys

sys.stdin = open("input.txt", "r")

n = int(sys.stdin.readline().rstrip())

def find_prime_list_under_number(number):
    prime_list = []
    for n in range(2, number+1):
        for i in prime_list:
            if n%i==0:
                break
        else:
            prime_list.append(n)
    return prime_list

print(find_prime_list_under_number(n))