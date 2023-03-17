import io
import sys

_INPUT = """\
4 5
3 2 4 1
"""
sys.stdin = io.StringIO(_INPUT)

n, k = map(int, input().split())
a = [0] + list(map(int, input().split()))

visited = [False] * (n+1)
now = 1
cnt = 0

for i in range(k):
    if visited[now]:
        cnt = i
        break
    else:
        visited[now] = True

    now = a[now]

print(now, cnt)
print(visited)

# 途中




