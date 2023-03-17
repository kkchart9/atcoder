import io
import sys

_INPUT = """\
10 10
83 86 77 65 93 85 86 92 99 71
62 77 90 59 63 76 90 76 72 86
61 68 67 79 82 80 62 73 67 85
79 52 72 58 69 67 93 56 61 92
79 73 71 69 84 87 98 74 65 70
63 76 91 80 56 73 62 70 96 81
55 75 84 77 86 55 96 79 63 57
74 95 82 95 64 67 84 64 93 50
87 58 76 78 88 84 53 51 54 99
82 60 76 68 89 62 76 86 94 89
"""
sys.stdin = io.StringIO(_INPUT)


h, w = map(int, input().split())
h_list = []
w_list = [0]*w
li = []

for i in range(h):
    a = list(map(int, input().split()))
    li.append(a)
    h_list.append(sum(a))
    for j in range(w):
        w_list[j] += a[j]

ans = []
for i in range(h):
    tmp = []
    for j in range(w):
        tmp.append(str(h_list[i] + w_list[j] - li[i][j]))
    ans.append(tmp)

for i in range(len(ans)):
    print(' '.join(ans[i]))

