import io
import sys

_INPUT = """\
4 5
2 4
1 2
2 3
1 3
3 4
"""
sys.stdin = io.StringIO(_INPUT)

# n, m = map(int, input().split())
# connect = [[] for _ in range(n+1)]
# dist = [10**6] * (n+1)
# dp = [0] * (n+1)
# MOD = 10 ** 9 + 7
#
# for i in range(m):
#     a, b = map(int, input().split())
#     connect[a].append(b)
#     connect[b].append(a)
#
# from collections import deque
# que = deque()
#
# que.append(1)
#
# dp[1] = 1
# dist[1] = 1
#
# while 0 < len(que):
#     now = que.popleft()
#     cur_cost = dist[now]
#     next_cost = cur_cost + 1
#
#     for to in connect[now]:
#         if next_cost < dist[to]:
#             que.append(to)
#             dist[to] = next_cost
#
#         if next_cost == dist[to]:
#             dp[to] += dp[now]
#             dp[to] %= MOD
#
# print(dp[-1])


n, m = map(int, input().split())
connect = [[] for _ in range(n+1)]
dist = [10**6] * (n+1)
dp = [0] * (n+1)
MOD = 10 ** 9 + 7

for i in range(m):
    a, b = map(int, input().split())
    connect[a].append(b)
    connect[b].append(a)


from collections import deque
que = deque()

dp[1] = 1
dist[1] = 1
que.append(1)

while que:
    now = que.popleft()
    curr_cost = dist[now]
    next_cost = curr_cost + 1

    for to in connect[now]:
        if next_cost < dist[to]:
            que.append(to)
            dist[to] = next_cost

        if next_cost == dist[to]:
            dp[to] += dp[now]
            dp[to] %= MOD


print(dp[-1])
