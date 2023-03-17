import io
import sys

_INPUT = """\
5 5
1 2
2 3
3 4
4 5
5 1
"""
sys.stdin = io.StringIO(_INPUT)

n, m = map(int, input().split())
from collections import defaultdict
from collections import deque
li = defaultdict(list)
connect =

for i in range(m):
    v, t = map(int, input().split())
    li[v].append(t)
    li[t].append(v)


que = deque()
que.append(1)

if n == m:
    print('No')
    exit()

for i in range(1, n+1):
    flag = [False] * n
    flag[i-1] = True
    if li[i]:
        que.append(li[i][0])
        flag[i-1] = True
    while que:
        num = que.popleft()
        flag[num-1] = True
        for to in li[num]:
            if flag[to-1] == False:
                flag[to-1] = True
                que.append(to)

    if False not in flag:
        print('Yes')
        exit()



print('No')










