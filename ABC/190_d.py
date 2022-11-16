import io
import sys

_INPUT = """\
963761198400
"""
sys.stdin = io.StringIO(_INPUT)

n = int(input())

ans = 0

i = 1

while i*i <= 2*n:
    if 2*n%i == 0:
        x = i
        y = 2*n//i
        if x % 2 != y % 2:
            ans += 2
    i += 1

print(ans)
