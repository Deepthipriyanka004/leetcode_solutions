# Last updated: 12/11/2025, 9:58:45 PM
1class Solution:
2    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
3        g1 = defaultdict(list)
4        g2 = defaultdict(list)
5        for x, y in buildings:
6            g1[x].append(y)
7            g2[y].append(x)
8        for x in g1:
9            g1[x].sort()
10        for y in g2:
11            g2[y].sort()
12        ans = 0
13        for x, y in buildings:
14            l1 = g1[x]
15            l2 = g2[y]
16            if l2[0] < x < l2[-1] and l1[0] < y < l1[-1]:
17                ans += 1
18        return ans