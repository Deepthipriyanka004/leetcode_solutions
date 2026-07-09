# Last updated: 7/9/2026, 7:12:03 PM
1class UnionFind:
2  def __init__(self, n: int):
3    self.id = list(range(n))
4    self.rank = [0] * n
5
6  def unionByRank(self, u: int, v: int) -> None:
7    i = self.find(u)
8    j = self.find(v)
9    if i == j:
10      return
11    if self.rank[i] < self.rank[j]:
12      self.id[i] = j
13    elif self.rank[i] > self.rank[j]:
14      self.id[j] = i
15    else:
16      self.id[i] = j
17      self.rank[j] += 1
18
19  def find(self, u: int) -> int:
20    if self.id[u] != u:
21      self.id[u] = self.find(self.id[u])
22    return self.id[u]
23
24
25class Solution:
26  def pathExistenceQueries(
27      self,
28      n: int,
29      nums: list[int],
30      maxDiff: int,
31      queries: list[list[int]]
32  ) -> list[bool]:
33    uf = UnionFind(n)
34
35    for i in range(1, n):
36      if abs(nums[i] - nums[i - 1]) <= maxDiff:
37        uf.unionByRank(i, i - 1)
38
39    return [uf.find(u) == uf.find(v)
40            for u, v in queries]