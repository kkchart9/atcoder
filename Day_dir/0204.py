import io
import sys

_INPUT = """\
3
3 4 5
4
4 5 6 8
15
"""
sys.stdin = io.StringIO(_INPUT)

n = int(input())
a = list(map(int, input().split()))

m = int(input())
b = list(map(int, input().split()))
x = int(input())

dp = [False] * (x+1)
no = [True] * (x+1)

for i in b:
    no[i] = False


dp[0] = True

for i in range(x):
    if dp[i]:
        for A in a:
            if i+A <= x and no[i+A]:
                dp[i+A] = True


if dp[-1]:
    print('Yes')
else:
    print('No')
