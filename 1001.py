import io
import sys

_INPUT = """\
6
1 2 4 6 7 271
"""
sys.stdin = io.StringIO(_INPUT)


N = int(input())
A = set(map(int,input().split()))

l = 0
r = N+1

while r-l>1:
    m = (l+r)//2
    # m巻まで読めるか？
    c = len(set(range(1,m+1)) & A)
    print(set(range(1,m+1)) & A,m)
    if c+(N-c)//2 >= m: l = m
    else: r = m

# print(l)

