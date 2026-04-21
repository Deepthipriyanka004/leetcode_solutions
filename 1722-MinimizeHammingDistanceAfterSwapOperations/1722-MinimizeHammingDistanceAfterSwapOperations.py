# Last updated: 4/21/2026, 10:01:58 AM
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
26  def minimumHammingDistance(
27      self,
28      source: list[int],
29      target: list[int],
30      allowedSwaps: list[list[int]],
31  ) -> int:
32    n = len(source)
33    ans = 0
34    uf = UnionFind(n)
35    groupIdToCount = [collections.Counter() for _ in range(n)]
36
37    for a, b in allowedSwaps:
38      uf.unionByRank(a, b)
39
40    for i in range(n):
41      groupIdToCount[uf.find(i)][source[i]] += 1
42
43    for i in range(n):
44      groupId = uf.find(i)
45      count = groupIdToCount[groupId]
46      if target[i] not in count:
47        ans += 1
48      else:
49        count[target[i]] -= 1
50        if count[target[i]] == 0:
51          del count[target[i]]
52
53    return ans