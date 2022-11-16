import io
from re import X
import sys

_INPUT = """\
4 330
0 1 10 100
1 0 20 200
10 20 0 300
100 200 300 0
"""
sys.stdin = io.StringIO(_INPUT)

N,K=map(int, input().split())

time=[]

for i in range(N):
    T=list(map(int, input().split()))
    time.append(T)

ans=0

import itertools
for root in itertools.permutations(range(1,N)):
    now_time=0
    now_time+=time[0][root[0]]
    now_city=root[0]

    for i in range(1,N-1):
        to_city=root[i]
        now_time+=time[now_city][to_city]
        now_city=to_city

    now_time+=time[now_city][0]
    if now_time==K:
        ans+=1

print(ans)