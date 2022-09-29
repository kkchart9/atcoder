import io
import sys

_INPUT = """\
4
1 2
1 3
1 4
"""
sys.stdin = io.StringIO(_INPUT)

N = int(input())
# dist = [list(map(int,input().split())) for _ in range(N-1)]
# print(dist)

g = [[] for _ in range(N)]
for _ in range(N - 1):
    a, b = map(int,input().split())
    g[a - 1].append(b - 1)
    g[b - 1].append(a - 1)

print(g)

# def dfs(a,b):
#     for i in dist[]