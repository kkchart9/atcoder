import io
from re import X
import sys

_INPUT = """\
6
123 223 123 523 200 2000
"""
sys.stdin = io.StringIO(_INPUT)

n = int(input())
a = list(map(int,input().split()))

R = [x % 200 for x in a]
ans = 0
cnt = [0]*200

for r in R:
    ans += cnt[r]
    cnt[r] += 1
    # print(cnt)

print(ans)


# print(R)