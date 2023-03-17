import io
import sys

_INPUT = """\
3 12
6 1 5
"""
sys.stdin = io.StringIO(_INPUT)

n, m = map(int, input().split())
a = list(map(int, input().split()))

import math

def prime_check(N):
  b = min(N-1, int(math.sqrt(1 * N)))
  for i in range(2,b+1):
    if (N % i == 0):
      return False
  return True

prime = []

for i in range(1, m+1):
    if prime_check(i):
        prime.append(i)

ans = []

for i in prime:
    cnt = 0
    for j in a:
        num = math.gcd(i, j)

        if num == 1:
            cnt += 1

    if cnt == n:
        ans.append(i)

print(len(ans))

for i in ans:
    print(i)