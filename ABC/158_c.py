import io
import sys

_INPUT = """\
a
6
2 2 a
2 1 b
1
2 2 c
1
1
"""
sys.stdin = io.StringIO(_INPUT)

from collections import deque

s = input()
q = int(input())
state = True

for i in range(len(s)):
    s_deque = deque([s[i]])

for i in range(q):
    query = list(input().split())
    T = int(query[0])
    if T == 1:
        if state:
            state = False
        else:
            state = True

    if T == 2:
        F = int(query[1])
        C = query[2]

        if state:
            if F == 1:
                s_deque.appendleft(C)
            else:
                s_deque.append(C)

        else:
            if F == 1:
                s_deque.append(C)
            else:
                s_deque.appendleft(C)

ans = ''.join(s_deque)

if state:
    print(ans)
else:
    print(ans[::-1])



