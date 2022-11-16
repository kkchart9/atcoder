import io
import sys

_INPUT = """\
6
2 4 4 9 4 9
"""
sys.stdin = io.StringIO(_INPUT)

n = int(input())
A = list(map(int, input().split()))

ans = -10**15

for i in range(n):
    a_min = A[i]
    for j in range(i, n):
        a_min = min(a_min, A[j])
        # print(a_min*(j-i+1))
        ans = max(ans, a_min*(j-i+1))

print(ans)