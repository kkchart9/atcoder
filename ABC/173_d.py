import io
import sys

_INPUT = """\
4
2 2 1 3
"""
sys.stdin = io.StringIO(_INPUT)


import heapq
n = int(input())
a = list(map(int, input().split()))
A = sorted(a, reverse=True)

ans = 0
q = []
heapq.heappush(q, -A[0])

for i in range(1, n):
    tmp = heapq.heappop(q)
    tmp *= -1
    ans += tmp
    heapq.heappush(q, -A[i])
    heapq.heappush(q, -A[i])

print(ans)


