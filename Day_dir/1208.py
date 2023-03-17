import io
import sys

_INPUT = """\
4
90 180 45 195
"""
sys.stdin = io.StringIO(_INPUT)

n = int(input())
a = list(map(int, input().split()))

li = []
li.append(360)
cnt = 0

for i in range(n):
    cnt += a[i]
    tmp = cnt // 360
    if tmp:
        ans = cnt - tmp*360
        li.append(ans)
    else:
        li.append(cnt)

li.sort()
num = 0
for i in range(1, len(li)):
    num = max(li[-i] - li[-i-1], num)
print(num)


