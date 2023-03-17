import io
import sys

_INPUT = """\
7 14
1 6 3
1 4 1
1 5 2
1 2 7
1 3 5
3 2
3 4
3 6
2 3 5
2 4 1
1 1 5
3 2
3 4
3 6
"""
sys.stdin = io.StringIO(_INPUT)

n, q = map(int, input().split())
_next = [-1] * (n + 1)  # すぐ後ろの電車の番号
_prev = [-1] * (n + 1)  # すぐ前の電車の番号

for i in range(q):
    query = list(map(int, input().split()))
    q = query[0]

    if q == 1:
        x, y = query[1:]
        _next[x] = y
        _prev[y] = x
    elif q == 2:
        x, y = query[1:]
        _next[x] = -1  # xが新しい最後尾
        _prev[y] = -1  # yが新しい先頭

    else:
        x = query[1]
        ans = []

        now = x

        while _prev[now] != -1:
            now = _prev[now]

        while now != -1:
            ans.append(now)
            now = _next[now]

        print(len(ans), *ans)
