# Last updated: 11/28/2025, 9:08:35 AM
1class Solution:
2  def maxKDivisibleComponents(
3      self,
4      n: int,
5      edges: list[list[int]],
6      values: list[int],
7      k: int,
8  ) -> int:
9    ans = 0
10    graph = [[] for _ in range(n)]
11
12    def dfs(u: int, prev: int) -> int:
13      nonlocal ans
14      treeSum = values[u]
15
16      for v in graph[u]:
17        if v != prev:
18          treeSum += dfs(v, u)
19
20      if treeSum % k == 0:
21        ans += 1
22      return treeSum
23
24    for u, v in edges:
25      graph[u].append(v)
26      graph[v].append(u)
27
28    dfs(0, -1)
29    return ans