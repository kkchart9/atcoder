import io
import sys

_INPUT = """\
869121
"""
sys.stdin = io.StringIO(_INPUT)

N = int(input())
mod = 10**9+7

A_all = pow(10, N, mod)
A_0 = pow(9, N, mod)
A_9 = pow(9, N, mod)
A_0_9 = pow(8, N, mod)

ans = A_all-(A_0+A_9-A_0_9)

ans %= mod

print(ans)

