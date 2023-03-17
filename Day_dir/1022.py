import io
from re import X
import sys

_INPUT = """\
4 5
1 2 3 1
1 3 2 4 1 4
1 2 2 3 3 4
1 1 2 2 3 4
1 2 2 3 3 3
1 4 1 4 1 1
"""
sys.stdin = io.StringIO(_INPUT)

import numpy as np

n, q = map(int, input().split())
A = list(map(int, input().split()))

for i in range(n):
    query = list(map(int, input().split()))
    ind = [i-1 for i in query]
    a = np.array(A[ind[0]:ind[1]+1])
    b = np.array(A[ind[2]:ind[3]+1])
    c = np.array(a[ind[4]:ind[5]+1])

    s = a ^ b




