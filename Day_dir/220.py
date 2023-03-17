import io
import sys

_INPUT = """\
9
1 0 1 1 1 1 1 1 0
"""
sys.stdin = io.StringIO(_INPUT)


n = int(input())
d = list(map(int, input().split()))

li = [0] * (n + 1)
cnt = 0

for i in range(n):
    cnt += d[i]
    li[i+1] = cnt

ans = 0
for i in range(n):
    if 7+i <= n:
        num = li[7+i] - li[i]
        if num <= 5:
            ans += 1
    else:
        num = li[i+1] - li[i-6]
        print(num, li[i+1])
        if num <= 5:
            ans += 1


# print(ans)
print(li)

