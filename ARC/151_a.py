import io
import sys

_INPUT = """\
5
00100
10011
"""
sys.stdin = io.StringIO(_INPUT)

from itertools import product

n = int(input())
s = input()
t = input()

for i in product([0, 1], repeat=n):

    print(str(i))
