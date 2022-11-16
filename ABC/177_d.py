import io
import sys

_INPUT = """\
5 3
1 2
3 4
5 1
"""
sys.stdin = io.StringIO(_INPUT)

n, m = map(int, input().split())


