import io
import sys

_INPUT = """\
7 8
2 2
4 5
########
#......#
#.######
#..#...#
#..##..#
##.....#
########
"""
sys.stdin = io.StringIO(_INPUT)

from collections import deque

R,C = map(int,input().split())
sx,sy = map(int,input().split())
gx,gy = map(int,input().split())

tizu = [list(input()) for _ in range(R)]

sx,sy,gx,gy = sx-1,sy-1,gx-1,gy-1

dist = [[10**4 for i in range(C)] for j in range(R)]

for r in range(R):
    for c in range(C):
        if tizu[r][c] == "#":
            dist[r][c] = -1

dist[sx][sy] = 0

que = deque()
que.append([sx,sy])

d = [[1,0],[-1,0],[0,1],[0,-1]]


# 幅優先探索
while que:
    x,y = que.popleft()
    
    for i,j in d:
        if x+i >= R or x+i < 0 or y+j >= C or y+j < 0:
            continue
        
        if tizu[x+i][y+j] == "#":
            continue

        if dist[x+i][y+j] != 10**4:
            continue

        dist[x+i][y+j] = dist[x][y] + 1

        que.append([x+i, y+j])
    # print(que)

# print(dist)
print(dist[gx][gy])


#
# from collections import defaultdict
# li = defaultdict(list)
# n, m = map(int, input().split())
#
# for _ in range(m):
#     a, b = map(int, input().split())
#     a -= 1
#     b -= 1
#     li[a].append(b)
#     li[b].append(a)
#
#
# from collections import deque
#
# INF = 1 << 60
# MOD = 10 ** 9 + 7
# dist = [INF] * n
# dp = [0] * n
# dist[0] = 0
# dp[0] = 1
#
# que = deque((0,))
#
# while que:
#     now = que.popleft()
#     curr_cost = dist[now]
#     next_cost = curr_cost + 1
#     for v in li[now]:
#         if next_cost < dist[v]:
#             que.append(v)
#             dist[v] = next_cost
#         if next_cost == dist[v]:
#             dp[v] += dp[now]
#             dp[v] %= MOD
#         print(dp, v+1)
#     print('----------------', que)
#
# print(que)

