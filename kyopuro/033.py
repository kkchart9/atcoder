import io
import sys

_INPUT = """\
3 6
"""
sys.stdin = io.StringIO(_INPUT)

h, w = map(int, input().split())

if h % 2:
    h_cnt = h // 2 + 1
else:
    h_cnt = h // 2

if w % 2:
    w_cnt = w // 2 + 1
else:
    w_cnt = w // 2

if h == 1 or w == 1:
    print(h*w)
else:
    print(h_cnt * w_cnt)
