import io
import sys

_INPUT = """\
20
URDDLLUUURRRDDDDLLLL
"""
sys.stdin = io.StringIO(_INPUT)


n = int(input())
s = list(input())

from collections import defaultdict
li_t = defaultdict(list)
li_y = defaultdict(list)

# di = dict(R=0, L=0, U=0, D=0)
tate, yoko = 0, 0
li_t[0].append(0)

for i in range(n):
    if s[i] == "R":
        tate, yoko = tate+1, yoko
    elif s[i] == "L":
        tate, yoko = tate-1, yoko
    elif s[i] == "U":
        tate, yoko = tate, yoko+1
    elif s[i] == "D":
        tate, yoko = tate, yoko-1



    # li[tate].append(yoko)

print('No')


