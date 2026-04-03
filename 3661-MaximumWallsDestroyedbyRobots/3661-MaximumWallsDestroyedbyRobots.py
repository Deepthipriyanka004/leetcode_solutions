# Last updated: 4/3/2026, 7:41:07 PM
1class Solution:
2    def maxWalls(self, robots: List[int], distance: List[int], walls: List[int]) -> int:
3        n = len(robots)
4        arr = sorted(zip(robots, distance), key=lambda x: x[0])
5        walls.sort()
6
7        @cache
8        def dfs(i: int, j: int) -> int:
9            if i < 0:
10                return 0
11            left = arr[i][0] - arr[i][1]
12            if i > 0:
13                left = max(left, arr[i - 1][0] + 1)
14            l = bisect_left(walls, left)
15            r = bisect_left(walls, arr[i][0] + 1)
16            ans = dfs(i - 1, 0) + r - l
17            right = arr[i][0] + arr[i][1]
18            if i + 1 < n:
19                if j == 0:
20                    right = min(right, arr[i + 1][0] - arr[i + 1][1] - 1)
21                else:
22                    right = min(right, arr[i + 1][0] - 1)
23            l = bisect_left(walls, arr[i][0])
24            r = bisect_left(walls, right + 1)
25            ans = max(ans, dfs(i - 1, 1) + r - l)
26            return ans
27
28        ans = dfs(n - 1, 1)
29        dfs.cache_clear()
30        return ans