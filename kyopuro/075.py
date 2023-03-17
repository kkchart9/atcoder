import io
import sys

_INPUT = """\
54
"""
sys.stdin = io.StringIO(_INPUT)

n = int(input())

def prime_factorize(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a

li = set()
cnt = 0

for i in prime_factorize(n):
    if i in li:
        cnt += 1
    li.add(i)

print(cnt)