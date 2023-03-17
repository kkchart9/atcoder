import io
import sys

_INPUT = """\
17 9
-905371741 -999219903 969314057 -989982132 -87720225 -175700172 -993990465 929461728 895449935 -999016241 782467448 -906404298 578539175 9684413 -619191091 -952046546 125053320
-440503430 -997661446 -912471383 -995879434 932992245 -928388880 -616761933 929461728 210953513 -994677396 648190629 -530944122 578539175 9684413 595786809 -952046546 125053320
2 10
6 12
9 11
11 5
7 6
3 15
3 1
1 9
10 4
"""
sys.stdin = io.StringIO(_INPUT)

n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

from collections import defaultdict

class UnionFind():
    # 初期化
    def __init__(self, n):
        self.par = [-1] * n
        self.rank = [0] * n
        self.siz = [1] * n
        self.cnt = [0] * n

    # 根を求める
    def root(self, x):
        if self.par[x] == -1:
            return x  # x が根の場合は x を返す
        else:
            self.par[x] = self.root(self.par[x])  # 経路圧縮
            return self.par[x]

    # x と y が同じグループに属するか (根が一致するか)
    def issame(self, x, y):
        return self.root(x) == self.root(y)

    # x を含むグループと y を含むグループを併合する
    def unite(self, x, y):
        # x 側と y 側の根を取得する
        rx = self.root(x)
        ry = self.root(y)
        if rx == ry:
            return False  # すでに同じグループのときは何もしない
        # union by rank
        if self.rank[rx] < self.rank[ry]:  # ry 側の rank が小さくなるようにする
            rx, ry = ry, rx
        self.par[ry] = rx  # ry を rx の子とする
        if self.rank[rx] == self.rank[ry]:  # rx 側の rank を調整する
            self.rank[rx] += 1
        self.siz[rx] += self.siz[ry] # rx 側の siz を調整する
        return True

    # x を含む根付き木のサイズを求める
    def size(self, x):
        return self.siz[self.root(x)]

    def all_group_members(self):
        """
        全てのグループの要素情報を辞書で返す
        """
        group_members = defaultdict(list)
        for member in range(n):
            group_members[self.root(member)].append(member)
        return group_members


uf = UnionFind(n)


for i in range(m):
    c, d = map(int, input().split())
    c -= 1
    d -= 1
    uf.unite(c, d)

flag = True

for c in uf.all_group_members().values():
    if sum(a[i] for i in c) != sum(b[i] for i in c):
        print('No')
        exit()
print('Yes')




# print(uf.all_group_members())



