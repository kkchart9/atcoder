class UnionFind():
    from collections import defaultdict
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

    def henn(self, x, y):
        if self.issame(x, y):
            self.cnt[self.root(x)] += 1

# 要素数 N の Union-Find を用意する
uf = UnionFind(N)

# 各辺 (a, b) に対して unite(a, b) を実行
for i in range(M):
    # 辺 (a, b) の入力
    a, b = map(int, input().split())
    a -= 1
    b -= 1

    # unite
    uf.unite(a, b)
    uf.henn(a, b)
