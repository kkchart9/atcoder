import io
from re import X
import sys

_INPUT = """\
ooo???xxxx
"""
sys.stdin = io.StringIO(_INPUT)

S = list(input())
O = []
X = []


# Sの文字列の中で、条件に合致するのか確認
def judge(s):
    # 値の中に必ず含まれていないといけないもの
    for i in O:
        if i not in s:
            return False

    # 値の中に含まれていたらダメなもの
    for i in X:
        if i in s:
            return False

    return True



ans = 0

for i,char in enumerate(S):
    if char == "o":
        O.append(str(i))
    
    elif char == "x":
        X.append(str(i))

# print(O,X)


for i in range(10000):
    s = str(i).zfill(4)
    if judge(s):
        ans += 1

print(ans)