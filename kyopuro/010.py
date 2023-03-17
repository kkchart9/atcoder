import io
import sys

_INPUT = """\
1
1 100
3
1 1
1 1
1 1
"""
sys.stdin = io.StringIO(_INPUT)

# 累積和
n = int(input())

one = [0]*(n+1)
two = [0]*(n+1)
one_cnt = 0
two_cnt = 0

# 先に0を代入することでindex out of errorを解決できる。
for i in range(1, n+1):
    c, p = map(int, input().split())
    if c == 1:
        one_cnt += p
        one[i] = one_cnt
        two[i] = two_cnt
    else:
        two_cnt += p
        one[i] = one_cnt
        two[i] = two_cnt

q = int(input())

for i in range(q):
    l, r = map(int, input().split())
    one_ans = one[r] - one[l-1]
    two_ans = two[r] - two[l-1]
    print(one_ans, two_ans)
