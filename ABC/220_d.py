import io
import sys

_INPUT = """\
3
2 7 6
"""
sys.stdin = io.StringIO(_INPUT)

n = int(input())
a = list(map(int, input().split()))


