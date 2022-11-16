import io
import sys

_INPUT = """\
100000 99999
"""
sys.stdin = io.StringIO(_INPUT)

import math

a,b = map(int,input().split())
def lcm(x,y):
    return (x*y)//math.gcd(x,y)

print(lcm(a,b))

