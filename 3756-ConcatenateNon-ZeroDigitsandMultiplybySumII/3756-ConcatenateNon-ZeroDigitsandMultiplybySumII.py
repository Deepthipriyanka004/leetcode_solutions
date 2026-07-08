# Last updated: 7/8/2026, 7:31:24 PM
1mx = 10**5 + 1
2mod = 10**9 + 7
3pow10 = [1] * mx
4for i in range(1, mx):
5    pow10[i] = pow10[i - 1] * 10 % mod
6
7
8class Solution:
9    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
10        n = len(s)
11        sum_d = [0] * (n + 1)
12        cnt_n0 = [0] * (n + 1)
13        p = [0] * (n + 1)
14        for i, d in enumerate(map(int, s), 1):
15            sum_d[i] = sum_d[i - 1] + d
16            cnt_n0[i] = cnt_n0[i - 1] + int(d > 0)
17            p[i] = (p[i - 1] * 10 + d) % mod if d else p[i - 1]
18
19        ans = []
20        for l, r in queries:
21            n0 = cnt_n0[r + 1] - cnt_n0[l]
22            sd = sum_d[r + 1] - sum_d[l]
23            x = p[r + 1] - p[l] * pow10[n0] % mod
24            ans.append(x * sd % mod)
25        return ans