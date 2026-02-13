# Last updated: 2/13/2026, 8:27:42 AM
1class Solution:
2    def longestBalanced(self, s: str) -> int:
3        def calc1(s: str) -> int:
4            res = 0
5            i, n = 0, len(s)
6            while i < n:
7                j = i + 1
8                while j < n and s[j] == s[i]:
9                    j += 1
10                res = max(res, j - i)
11                i = j
12            return res
13
14        def calc2(s: str, a: str, b: str) -> int:
15            res = 0
16            i, n = 0, len(s)
17            while i < n:
18                while i < n and s[i] not in (a, b):
19                    i += 1
20                pos = {0: i - 1}
21                d = 0
22                while i < n and s[i] in (a, b):
23                    d += 1 if s[i] == a else -1
24                    if d in pos:
25                        res = max(res, i - pos[d])
26                    else:
27                        pos[d] = i
28                    i += 1
29            return res
30
31        def calc3(s: str) -> int:
32            pos = {(0, 0): -1}
33            cnt = Counter()
34            res = 0
35            for i, c in enumerate(s):
36                cnt[c] += 1
37                k = (cnt["a"] - cnt["b"], cnt["b"] - cnt["c"])
38                if k in pos:
39                    res = max(res, i - pos[k])
40                else:
41                    pos[k] = i
42            return res
43
44        x = calc1(s)
45        y = max(calc2(s, "a", "b"), calc2(s, "b", "c"), calc2(s, "a", "c"))
46        z = calc3(s)
47        return max(x, y, z)