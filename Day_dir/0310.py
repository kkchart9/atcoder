import io
import sys

_INPUT = """\
3
2 3 5
3 4 1
"""
sys.stdin = io.StringIO(_INPUT)

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))


