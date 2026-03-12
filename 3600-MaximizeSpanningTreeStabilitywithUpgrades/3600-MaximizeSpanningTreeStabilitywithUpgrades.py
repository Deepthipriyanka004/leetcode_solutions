# Last updated: 3/12/2026, 10:41:13 PM
1class UnionFind:
2    def __init__(self, n):
3        self.p = list(range(n))
4        self.size = [1] * n
5        self.cnt = n
6
7    def find(self, x):
8        if self.p[x] != x:
9            self.p[x] = self.find(self.p[x])
10        return self.p[x]
11
12    def union(self, a, b):
13        pa, pb = self.find(a), self.find(b)
14        if pa == pb:
15            return False
16        if self.size[pa] > self.size[pb]:
17            self.p[pb] = pa
18            self.size[pa] += self.size[pb]
19        else:
20            self.p[pa] = pb
21            self.size[pb] += self.size[pa]
22        self.cnt -= 1
23        return True
24
25
26class Solution:
27    def maxStability(self, n: int, edges: List[List[int]], k: int) -> int:
28        def check(lim: int) -> bool:
29            uf = UnionFind(n)
30            for u, v, s, _ in edges:
31                if s >= lim:
32                    uf.union(u, v)
33            rem = k
34            for u, v, s, _ in edges:
35                if s * 2 >= lim and rem > 0:
36                    if uf.union(u, v):
37                        rem -= 1
38            return uf.cnt == 1
39
40        uf = UnionFind(n)
41        mn = 10**6
42        for u, v, s, must in edges:
43            if must:
44                mn = min(mn, s)
45                if not uf.union(u, v):
46                    return -1
47        for u, v, _, _ in edges:
48            uf.union(u, v)
49        if uf.cnt > 1:
50            return -1
51        l, r = 1, mn
52        while l < r:
53            mid = (l + r + 1) >> 1
54            if check(mid):
55                l = mid
56            else:
57                r = mid - 1
58        return l