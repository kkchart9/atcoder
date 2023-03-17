import io
import sys

_INPUT = """\
123456789012345
"""
sys.stdin = io.StringIO(_INPUT)


from collections import deque
#　素数を求める
def enum_primes(n):
    prime_flag = [1] * (n + 1)
    prime_flag[0] = 0
    prime_flag[1] = 0

    i = 2
    while i * i <= n:
        if prime_flag[i]:
            for j in range(2 * i, n + 1, i):
                prime_flag[j] = 0
        i += 1
    return [i for i in range(n + 1) if prime_flag[i]]


N = int(input())
ans = 0
primes = enum_primes(10 ** 6 + 5)  # 素数が小さい順に入っています
M = len(primes)

for i in range(M):
    t = primes[i] ** 3  # 重い t = q ** 3を先に計算します
    for j in range(i):  # primes[i]未満の素数を小さい順に全探索
        if t * primes[j] > N:
           break
        ans += 1

print(ans)
