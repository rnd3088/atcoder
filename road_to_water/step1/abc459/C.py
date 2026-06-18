class Fenwick:
    def __init__(self, n):
        self.n = n
        self.bit = [0] * (n + 1)

    def add(self, i, x):
        i += 1
        while i <= self.n:
            self.bit[i] += x
            i += i & -i

    def sum(self, i):
        # 0 〜 i までの合計
        i += 1
        res = 0
        while i > 0:
            res += self.bit[i]
            i -= i & -i
        return res


N, Q = map(int, input().split())

MAX = Q + 1

raw = [0] * N
fw = Fenwick(MAX)

fw.add(0, N)

base = 0
ans = []

for _ in range(Q):
    t, v = map(int, input().split())

    if t == 1:
        x = v - 1

        old = raw[x]
        raw[x] = old + 1

        fw.add(old, -1)
        fw.add(raw[x], 1)

        if fw.sum(base) - fw.sum(base - 1) == 0:
            base += 1

    else:
        y = v
        need = base + y

        if need >= MAX:
            ans.append(0)
        else:
            less = fw.sum(need - 1)
            ans.append(N - less)

print(*ans, sep="\n")