import io
import sys

_INPUT = """\
7 999999999
3 1 4 1 5 9 2
1 2 3 4 5 6 7
"""
sys.stdin = io.StringIO(_INPUT)

n, k = map(int, input().split())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

num = 0

for i in range(n):
    num += abs(a[i] - b[i])



