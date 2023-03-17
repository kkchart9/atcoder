import io
import sys

_INPUT = """\
1234 56789 314159265
"""
sys.stdin = io.StringIO(_INPUT)

a, b, x = map(int, input().split())

def price(n):
    N_str = str(n)
    d = len(N_str)
    return a*n+b*d

if x < price(1):
    print(0)
    exit()

left = 1
right = 10**10

while 1 < right-left:
    n = (left+right) // 2
    if price(n) <= x:
        left = n
    else:
        right = n


if 10**9 < left:
    left = 10**9


print(left)

