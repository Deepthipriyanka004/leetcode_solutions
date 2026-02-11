# Last updated: 2/11/2026, 11:37:33 AM
1class Solution:
2    def longestBalanced(self, nums: List[int]) -> int:
3        n = len(nums)
4
5        class Node:
6            __slots__ = ("l", "r", "mn", "mx", "lazy")
7            def __init__(self):
8                self.l = self.r = 0
9                self.mn = self.mx = 0
10                self.lazy = 0
11
12        tr = [Node() for _ in range((n + 1) * 4)]
13
14        def build(u: int, l: int, r: int):
15            tr[u].l, tr[u].r = l, r
16            tr[u].mn = tr[u].mx = tr[u].lazy = 0
17            if l == r:
18                return
19            mid = (l + r) >> 1
20            build(u << 1, l, mid)
21            build(u << 1 | 1, mid + 1, r)
22
23        def apply(u: int, v: int):
24            tr[u].mn += v
25            tr[u].mx += v
26            tr[u].lazy += v
27
28        def pushdown(u: int):
29            if tr[u].lazy:
30                apply(u << 1, tr[u].lazy)
31                apply(u << 1 | 1, tr[u].lazy)
32                tr[u].lazy = 0
33
34        def pushup(u: int):
35            tr[u].mn = min(tr[u << 1].mn, tr[u << 1 | 1].mn)
36            tr[u].mx = max(tr[u << 1].mx, tr[u << 1 | 1].mx)
37
38        def modify(u: int, l: int, r: int, v: int):
39            if tr[u].l >= l and tr[u].r <= r:
40                apply(u, v)
41                return
42            pushdown(u)
43            mid = (tr[u].l + tr[u].r) >> 1
44            if l <= mid:
45                modify(u << 1, l, r, v)
46            if r > mid:
47                modify(u << 1 | 1, l, r, v)
48            pushup(u)
49
50        def query(u: int, target: int) -> int:
51            if tr[u].l == tr[u].r:
52                return tr[u].l
53            pushdown(u)
54            if tr[u << 1].mn <= target <= tr[u << 1].mx:
55                return query(u << 1, target)
56            return query(u << 1 | 1, target)
57
58        build(1, 0, n)
59
60        last = {}
61        now = ans = 0
62
63        for i, x in enumerate(nums, start=1):
64            det = 1 if (x & 1) else -1
65            if x in last:
66                modify(1, last[x], n, -det)
67                now -= det
68            last[x] = i
69            modify(1, i, n, det)
70            now += det
71            pos = query(1, now)
72            ans = max(ans, i - pos)
73
74        return ans