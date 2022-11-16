import io
import sys

_INPUT = """\
4
0 1
0 2
0 3
1 1
"""
sys.stdin = io.StringIO(_INPUT)

import itertools

n = int(input())

points = []

for i in range(n):
    x,y = map(int,input().split())
    points.append([x,y])

# c = itertools.combinations(points, 3)

for i in itertools.combinations(points, 3):
    x1 = i[0][0]
    y1 = i[0][1]
    x2 = i[1][0]
    y2 = i[1][1]
    x3 = i[2][0]
    y3 = i[2][1]
    if (x2-x1)*(y3-y1) == (y2-y1)*(x3-x1):
        print('Yes')
        exit()

print('No')

# for i in range(n):
#     for j in range(i+1,n):
#         for k in range(j+1,n):

#             print(i,j,k)

# print(points)
