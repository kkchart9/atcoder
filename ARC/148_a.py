import io
import sys

_INPUT = """\
10
3785 5176 10740 7744 3999 3143 9028 2822 4748 6888
"""
sys.stdin = io.StringIO(_INPUT)

n = int(input())
a = list(map(int,input().split()))

li = set()

for i in a:
    mod = i % n
    li.add(mod)

print(li)