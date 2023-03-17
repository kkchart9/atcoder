import io
import sys

_INPUT = """\
4
1 2
4 2
3 1
"""
sys.stdin = io.StringIO(_INPUT)


n = int(input())
connect = [[] for _ in range(n+1)]
visited = [False for _ in range(n+1)]

for i in range(n-1):
    a, b = map(int, input().split())
    connect[a].append(b)
    connect[b].append(a)

from collections import deque
que = deque()

que.append(1)

while que:
    now = que.popleft()

    for to in connect[now]:
        if visited[to] == False:
            visited[to] = True

            que.append(to)

        print(to)

print(connect)
print(visited)