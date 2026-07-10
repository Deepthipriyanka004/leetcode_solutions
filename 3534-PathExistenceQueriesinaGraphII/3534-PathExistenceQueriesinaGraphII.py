# Last updated: 7/10/2026, 8:57:21 PM
1class Solution:
2    def pathExistenceQueries(
3        self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]
4    ) -> List[int]:
5        pairs = sorted((x, i) for i, x in enumerate(nums))
6        m = 20
7        f = [[0] * m for _ in range(n)]
8        r = n - 1
9        for l in range(n - 1, -1, -1):
10            while pairs[r][0] - pairs[l][0] > maxDiff:
11                r -= 1
12            i, j = pairs[l][1], pairs[r][1]
13            f[i][0] = j
14            for k in range(1, m):
15                f[i][k] = f[f[i][k - 1]][k - 1]
16
17        ans = []
18        for i, j in queries:
19            if nums[i] > nums[j]:
20                i, j = j, i
21            if i == j:
22                ans.append(0)
23                continue
24            if nums[i] == nums[j]:
25                ans.append(1)
26                continue
27            d = 0
28            for k in range(m - 1, -1, -1):
29                if nums[f[i][k]] < nums[j]:
30                    d |= 1 << k
31                    i = f[i][k]
32            if nums[f[i][0]] < nums[j]:
33                ans.append(-1)
34            else:
35                ans.append(d + 1)
36        return ans