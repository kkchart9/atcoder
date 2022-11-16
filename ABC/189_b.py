import io
import sys

_INPUT = """\
3 1000000
1000 100
1000 100
1000 100
"""
sys.stdin = io.StringIO(_INPUT)

n,x = map(int,input().split())
alcohol = 0

for i in range(n):
    a,b = map(int,input().split())
    alcohol+= a*b

    if 100*x < alcohol:
        print(i+1)
        exit()

print(-1)