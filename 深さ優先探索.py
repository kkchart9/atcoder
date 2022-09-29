import io
import sys

_INPUT = """\
4 4
...s
....
....
.g..
"""
sys.stdin = io.StringIO(_INPUT)

h,w = map(int,input().split())
tizu = [list(input()) for _ in range(h)]

for i in range(h):
    for j in range(w):
        if tizu[i][j] == "s":
            sx, sy = i,j


# 深さ優先探索
def dfs(x,y):
    # 範囲外や壁の場合は終了
    if y >= w or y < 0 or x >= h or x < 0 or tizu[x][y] == "#":
        return

    # ゴールに辿り着けば終了
    if tizu[x][y] == "g":
        print('Yes')
        exit()

    tizu[x][y] = "#"

    dfs(x+1,y)
    dfs(x-1,y)
    dfs(x,y+1)
    dfs(x,y-1)

dfs(sx,sy)
print('No')