import io
import sys

_INPUT = """\
4 4
1 9 3 5
"""
sys.stdin = io.StringIO(_INPUT)

import heapq

n, m = map(int, input().split())
a = list(map(int, input().split()))

a_min = []

for i in range(n):
    a_min.append(-1 * a[i])

heapq.heapify(a_min)

for i in range(m):
    x = heapq.heappop(a_min)
    x = x / 2
    x = int(x)
    heapq.heappush(a_min, x)

print((-1) * sum(a_min))
