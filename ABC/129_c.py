import io
import sys

_INPUT = """\
100 5
1
23
45
67
89
"""
sys.stdin = io.StringIO(_INPUT)

n, m = map(int, input().split())
MOD = 1000000007
broken = [True] * (n+1)

dp = [0] * (n+1)
dp[0] = 1

for i in range(m):
    a = int(input())
    broken[a] = False


for i in range(n+1):
    if i+1 <= n:
        if broken[i+1]:
            dp[i+1] += dp[i]


    if i+2 <= n:
        if broken[i+2]:
            dp[i+2] += dp[i]




print(dp[n] % MOD)



