import io
from re import X
import sys

_INPUT = """\
3
2 3 3
1 3 3
1 1 1
"""
sys.stdin = io.StringIO(_INPUT)

from collections import Counter

n = int(input())

a = list(map(int,input().split()))
b = list(map(int,input().split()))
c = list(map(int,input().split()))

ans = 0
cntA = Counter(a)

for x in c:
    y = x - 1
    k = b[y]
    ans += cntA[k]

print(ans)
