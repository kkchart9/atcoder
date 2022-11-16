import io
import sys

_INPUT = """\
5 3
1 2 2 4 5
"""
sys.stdin = io.StringIO(_INPUT)

n, k = map(int, input().split())
P = list(map(int, input().split()))

# pの期待値
p_ex = []
# 累積和のための配列
p_ex_Cum = []
cnt = 0


for i in range(n):
    p_ex.append((P[i]+1)/2)
    cnt += (P[i]+1)/2
    p_ex_Cum.append(cnt)

ans = -10**15

for i in range(n-k+1):
    if i == 0:
        ans_tmp = p_ex_Cum[i+k-1]
    else:
        ans_tmp = p_ex_Cum[i+k-1] - p_ex_Cum[i-1]

    ans = max(ans, ans_tmp)

print(ans)
