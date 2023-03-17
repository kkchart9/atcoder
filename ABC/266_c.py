import io
import sys

_INPUT = """\
0 0
1 0
1 1
0 1
"""
sys.stdin = io.StringIO(_INPUT)


a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))
d = list(map(int, input().split()))


def vec(x, y):
    return (x[0] - y[0], x[1] - y[0])

def tri_in(x, y, z, p):
    xy = vec(y, x)
    yz = vec(z, y)
    zx = vec(x, z)

    ap = vec(p, a)
    bp = vec(p, b)
    cp = vec(p, c)

    




