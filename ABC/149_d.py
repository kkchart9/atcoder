import io
import sys

_INPUT = """\
5 2
8 7 6
rsrpr
"""
sys.stdin = io.StringIO(_INPUT)

n, k = map(int, input().split())
r, s, p = map(int, input().split())
t = list(input())

hands = []
ans = 0

# 貪欲法　地道に一個一個できればよし