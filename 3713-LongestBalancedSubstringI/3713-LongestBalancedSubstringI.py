# Last updated: 2/12/2026, 9:37:42 AM
1class Solution:
2    def longestBalanced(self, s: str) -> int:
3        n = len(s)
4        ans = 0
5        for i in range(n):
6            cnt = Counter()
7            mx = v = 0
8            for j in range(i, n):
9                cnt[s[j]] += 1
10                mx = max(mx, cnt[s[j]])
11                if cnt[s[j]] == 1:
12                    v += 1
13                if mx * v == j - i + 1:
14                    ans = max(ans, j - i + 1)
15        return ans