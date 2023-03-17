import io
import sys

_INPUT = """\
5 1 2
rrefa
"""
sys.stdin = io.StringIO(_INPUT)

n, a, b = map(int, input().split())
s = input()

print(s)
