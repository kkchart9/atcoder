import io
import sys

_INPUT = """\
6 6 8
..##..
.#..#.
#....#
######
#....#
#....#
"""
sys.stdin = io.StringIO(_INPUT)

from itertools import product

h, w, k = map(int, input().split())
c = []

for i in range(h):
    tmp = list(input())
    c.append(tmp)

ans = 0

for row_bit in product(range(2), repeat=h):
    for col_bit in product(range(2), repeat=w):
        cnt = 0
        for row in range(h):
            for col in range(w):
                if c[row][col] == '#' and (row_bit[row] and col_bit[col]):
                    cnt += 1

        if cnt == k:
            ans += 1

print(ans)


