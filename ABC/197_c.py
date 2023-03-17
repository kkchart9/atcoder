import io
import sys

_INPUT = """\
3
1 5 7
"""
sys.stdin = io.StringIO(_INPUT)

from itertools import product

n = int(input())
a = list(map(int, input().split()))

def calc(left, right):
    result = 0
    for i in range(left, right):
        result = result | a[i]
    return result

ans = 2**40

for bits in product([0, 1], repeat=n+2):
    if bits[0] == 1 or bits[n+1] == 1:
        continue

    partitions = []


    print(bits)

