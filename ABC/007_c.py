import io
import sys

_INPUT = """\
7 8
2 2
4 5
########
#......#
#.######
#..#...#
#..##..#
##.....#
########
"""
sys.stdin = io.StringIO(_INPUT)

r, c = map(int, input().split())
sy, sx = map(int, input().split())
gy, gx = map(int, input().split())

tizu = []
dist = [[10**4 for i in range(c)] for j in range(r)]
sx,sy,gx,gy = sx-1,sy-1,gx-1,gy-1

for i in range(r):
    c = list(input())
    tizu.append(c)

from collections import deque
que = deque()
que.append([sx, sy])

d = [[1, 0], [-1, 0], [0, 1], [0, -1]]

while que:
    x, y = que.popleft()

    for i, j in d:
        if x + i >= r or x + i < 0 or y + j >= c or y + j < 0:
            continue

        if tizu[x+i][y+j] == "#":
            continue

        if dist[x+i][y+j] != 10**4:
            continue

        dist[x+i][y+j] = dist[x][y] + 1

        que.append([x+i, y+j])

print(dist[gx][gy])
