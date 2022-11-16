import io
from re import X
import sys

_INPUT = """\
100000
"""
sys.stdin = io.StringIO(_INPUT)

n = int(input())

li = set()

for i in range(2, 10**5+10):
    for j in range(2, 100):
        if i**j <= n:
            li.add(i**j)
        else:
            break

print(n - len(li))
# print(100)
