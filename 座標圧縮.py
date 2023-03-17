import io
import sys

_INPUT = """\
4 5 2
3 2
2 5
"""
sys.stdin = io.StringIO(_INPUT)

H, W, N = map(int, input().split())
R = []
C = []

for _ in range(N):
    r, c = map(int, input().split())
    R.append(r)
    C.append(c)

print(R, C)

Rs = sorted(set(R))  # `set`で重複を省いてソートしたリスト`Rs`
Cs = sorted(set(C))

print(Rs, Cs)

# Rd = {Rs[i]: i+1 for i in range(len(Rs))} と同じです
Rd = {x: i for i, x in enumerate(Rs, 1)}
Cd = {x: i for i, x in enumerate(Cs, 1)}

print(Rd, Cd)

for r, c in zip(R, C):
    print(Rd[r], Cd[c])