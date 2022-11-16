import io
import sys

_INPUT = """\
5 20
19 10
19 19
7 6
7 3
13 15
"""
sys.stdin = io.StringIO(_INPUT)

from itertools import product

N, X = map(int, input().split())

li = []

for i in range(N):
    w, r = map(int, input().split())
    li.append([w, r])

ans = 0

for i in product(range(2), repeat=N):
    sum_li = 0
    sum_weight = 0
    for j in zip(li, i):
        if j[1] == 1:
            sum_li += j[0][0]
            sum_weight += j[0][1]


    if sum_li < X:
        ans = max(ans, sum_weight)


print(ans)

