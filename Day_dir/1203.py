import io
import sys

_INPUT = """\
30
"""
sys.stdin = io.StringIO(_INPUT)

def is_prime(n):
    if n == 1:
        return True
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)

    divisors.sort()
    return divisors



k = int(input())
li = make_divisors(k)
ans = 1

for i in range(len(li)):
    ans *= li[i]
    print(ans)
    # if ans % k == 0:
    #     print(ans)
    #     exit()
    # print(ans)




