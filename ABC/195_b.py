import io
import sys

_INPUT = """\
100 200 2
"""
sys.stdin = io.StringIO(_INPUT)

a, b, w = map(int, input().split())

w = w * 1000

min_ans = 10 ** 15
max_ans = -10**15

for i in range(1, 10**6+10):
    if a*i <= w <= b*i:
        min_ans = min(min_ans, i)
        max_ans = max(max_ans, i)

if min_ans == 10**15:
    print("UNSATISFIABLE")
else:
    print(min_ans, max_ans)
