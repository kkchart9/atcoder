import io
import sys

_INPUT = """\
10
square869120
square869120
square869120
square869120
square869120
square869120
square869120
square869120
square869120
square869120
"""
sys.stdin = io.StringIO(_INPUT)

n = int(input())

li = set()

for i in range(n):
    s = input()
    if s not in li:
        print(i+1)
    li.add(s)

