import io
import sys

_INPUT = """\
10000 10
1 2 4 8 16 32 64 128 256 512
"""
sys.stdin = io.StringIO(_INPUT)

n,k = map(int,input().split())
a = list(map(int,input().split()))

ans = 0
cnt = 0
a.sort()
li = []
for i in range(1,k+1):
  num = a[-i]*2
  if n - num < 0:
    if n - num//2 < 0:
      break
    else:
      cnt += num//2
  else:
    n = n - num
    cnt += num//2


print(cnt)