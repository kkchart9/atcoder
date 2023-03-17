import io
import sys

_INPUT = """\
1500 2000 1600 3 2
"""
sys.stdin = io.StringIO(_INPUT)

a, b, c, x, y = map(int, input().split())

n = min(x, y)
sur = max(x, y) - n


