import io
import sys

_INPUT = """\
BBW
"""
sys.stdin = io.StringIO(_INPUT)

s = list(input())
cnt = 0

for i in range(len(s) - 1):
    if s[i] == "B" and s[i+1] == "W":
        s[i], s[i+1] = s[i+1], s[i]
        cnt += 1

print(cnt)


