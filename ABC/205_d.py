import io
import sys

_INPUT = """\
5 2
1 2
2 3
3 4
4 5
1 3
1 5
"""
sys.stdin = io.StringIO(_INPUT)


n, q = map(int, input().split())
connect = [[] for i in range(n+1)]
visited = [False for _ in range(n+1)]
# 0が赤、1が青
color = [-1] * (n+1)

for i in range(n - 1):
    a, b = map(int, input().split())
    connect[a].append(b)
    connect[b].append(a)

from collections import deque
que = deque()

color[1] = 0
visited[1] = True

que.append(1)

while 0 < len(que):
    now = que.popleft()
    now_color = color[now]


    for to in connect[now]:
        if visited[to] == False:
            visited[to] = True

            if now_color == 0:
                color[to] = 1

            if now_color == 1:
                color[to] = 0

            que.append(to)

for i in range(q):
    c, d = map(int, input().split())
    if color[c] == color[d]:
        print("Town")
    else:
        print("Road")
