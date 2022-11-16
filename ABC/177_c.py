import io
from re import X
import sys

_INPUT = """\
3
1 2 3
"""
sys.stdin = io.StringIO(_INPUT)

N = int(input())

A = list(map(int, input().split()))

mod = 10**9 + 7

ans = 0

A_sum = sum(A)

for i in range(N):
    A_sum -= A[i]
    ans += A_sum * A[i]

print(ans % mod)


